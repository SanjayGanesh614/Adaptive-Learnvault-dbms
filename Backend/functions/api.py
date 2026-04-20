import sys
import os

# Get the directory of the current file (functions/)
# Its parent is the root of our backend
BACKEND_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if BACKEND_ROOT not in sys.path:
    sys.path.insert(0, BACKEND_ROOT)

from mangum import Mangum
from main import app

handler = Mangum(app, lifespan="off")
