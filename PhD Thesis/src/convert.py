import os
import glob
from __builtin__ import file
from matplotlib.pyplot import margins
import os.path
from subprocess import call

for path in glob.glob('./images/fractals/*/workspace/fractal/0/rep.*.png'):
    
    base, name = os.path.split(path)
    call(["/usr/local/bin/convert", path, "-resize", "20%", base + "/small." + name])
    
for path in glob.glob('./images/fractals/*/workspace/fractal/0/*.png'):

    base, ext = os.path.splitext(path)
    call(["/usr/local/bin/convert", path, base + ".pdf"])
    
for path in glob.glob('./images/fractals/*/workspace/fractal/0/best/*.png'):

    base, ext = os.path.splitext(path)
    call(["/usr/local/bin/convert", path, base + ".pdf"])
