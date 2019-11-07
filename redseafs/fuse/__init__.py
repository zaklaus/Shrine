import sys
from os.path import dirname
pyver = sys.version_info[0:2]

sys.path.append(dirname(__file__))

if pyver <= (2, 4):
    from fuse24 import *
elif pyver >= (3, 0):
    from fuse3 import *
else:
    from fuse import *
