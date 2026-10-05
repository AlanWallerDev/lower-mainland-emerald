@echo off
rem Pokemon BC launcher: builds the game from this folder's source and starts it in mGBA.
rem Double-click to play. The repository never holds a ROM; this builds one on your machine.
rem Needs WSL (Windows Subsystem for Linux, see INSTALL.md) and mGBA (https://mgba.io).
rem Your save lives next to the game in play\ and survives rebuilds.
setlocal EnableExtensions
title Pokemon BC
cd /d "%~dp0"
set "ROM=%CD%\play\Pokemon BC.gba"

echo.
echo   ==== Pokemon BC ====
echo.

rem ---- 1. WSL ---------------------------------------------------------------------------------
wsl -- true >nul 2>&1
if errorlevel 1 goto :nowsl

rem ---- 2. Build tools (offered once) ----------------------------------------------------------
wsl -- sh -c "command -v arm-none-eabi-gcc && command -v make && test -e /usr/include/png.h" >nul 2>&1
if not errorlevel 1 goto :update
echo The build tools are not installed in WSL yet.
choice /C YN /M "Install them now (asks for your WSL password)"
if errorlevel 2 goto :notools
wsl -- sh -c "sudo apt-get update && sudo apt-get install -y build-essential git gcc-arm-none-eabi binutils-arm-none-eabi libpng-dev"
if errorlevel 1 goto :notools

rem ---- 3. Latest changes ----------------------------------------------------------------------
:update
echo Getting the latest version...
wsl --cd "%CD%" -- git pull --ff-only
if errorlevel 1 echo   Could not update; playing the copy on this computer.

rem ---- 4. Build -------------------------------------------------------------------------------
echo Building the game (the first build takes a few minutes)...
wsl --cd "%CD%" -- sh -c "make modern -j$(nproc) >build_log.txt 2>&1"
if errorlevel 1 goto :buildfail
if not exist "%CD%\play" mkdir "%CD%\play"
copy /Y "%CD%\pokeemerald_modern.gba" "%ROM%" >nul
if errorlevel 1 goto :buildfail
echo   Built: play\Pokemon BC.gba

rem A copy for phones (Delta on iPhone opens it from the Files app) when iCloud for Windows is set up.
set "PHONE=%USERPROFILE%\iCloudDrive"
if exist "%PHONE%" (
	if not exist "%PHONE%\Pokemon BC" mkdir "%PHONE%\Pokemon BC"
	copy /Y "%ROM%" "%PHONE%\Pokemon BC\Pokemon BC.gba" >nul && echo   Copied to iCloud Drive\Pokemon BC for your phone.
)

rem ---- 5. Start mGBA --------------------------------------------------------------------------
set "EMU="
if defined MGBA if exist "%MGBA%" set "EMU=%MGBA%"
if not defined EMU if exist "%CD%\mGBA\mGBA.exe" set "EMU=%CD%\mGBA\mGBA.exe"
if not defined EMU if exist "%ProgramFiles%\mGBA\mGBA.exe" set "EMU=%ProgramFiles%\mGBA\mGBA.exe"
if not defined EMU if exist "%ProgramFiles(x86)%\mGBA\mGBA.exe" set "EMU=%ProgramFiles(x86)%\mGBA\mGBA.exe"
if not defined EMU if exist "%LOCALAPPDATA%\mGBA\mGBA.exe" set "EMU=%LOCALAPPDATA%\mGBA\mGBA.exe"
if not defined EMU for /f "delims=" %%E in ('where mGBA.exe 2^>nul') do if not defined EMU set "EMU=%%E"
if defined EMU (
	start "" "%EMU%" "%ROM%"
	exit /b 0
)
rem No mGBA found: use whatever program opens .gba files, if any.
assoc .gba >nul 2>&1
if not errorlevel 1 (
	start "" "%ROM%"
	exit /b 0
)
echo.
echo mGBA was not found. Install it from the page that opens now, then run this again.
echo (Or put mGBA.exe in an "mGBA" folder next to this file, or set MGBA to its path.)
echo The game is ready at: %ROM%
start "" "https://mgba.io/downloads.html"
pause
exit /b 1

:nowsl
echo WSL is not set up on this computer. The game is built inside WSL.
echo Open PowerShell as administrator, run:  wsl --install
echo then restart and run this file again. Details: INSTALL.md, "Windows 10/11 (WSL1)".
pause
exit /b 1

:notools
echo The build tools are needed to make the game. In WSL, run:
echo   sudo apt-get install build-essential git gcc-arm-none-eabi binutils-arm-none-eabi libpng-dev
pause
exit /b 1

:buildfail
echo.
echo The build failed. The last lines of build_log.txt:
wsl --cd "%CD%" -- tail -n 15 build_log.txt
pause
exit /b 1
