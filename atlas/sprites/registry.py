"""Collects rigs and species specs from the rig_* and specs_* modules."""
import importlib
import pkgutil
import os

from . import engine

RIGS = {}
SPECS = {}
_here = os.path.dirname(__file__)
for m in pkgutil.iter_modules([_here]):
    if not m.name.startswith(('rigs_', 'specs_')):
        continue
    mod = importlib.import_module(__package__ + '.' + m.name)
    if m.name.startswith('rigs_'):
        names = getattr(mod, '__all__', [k for k, v in vars(mod).items() if callable(v) and not k.startswith('_')])
        RIGS.update({k: getattr(mod, k) for k in names})
    elif m.name.startswith('specs_'):
        SPECS.update(mod.SPECS)


def draw(sid, back=False):
    """Render one species (front or back) as a 64x64 'P' image with its palette; None if no spec."""
    sp = SPECS.get(sid)
    if not sp:
        return None
    art = engine.Art()
    RIGS[sp['rig']](art, sp, engine.rng(sid))
    im = art.render(back=back)
    if back:
        im = engine.flip(im)
    return im


def palettes(sid):
    sp = SPECS[sid]
    return engine.palette(sp), engine.palette(sp, shiny=True)
