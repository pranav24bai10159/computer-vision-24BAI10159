import os
import sys

# Add project root to sys.path
project_root = os.path.dirname(os.path.abspath(__file__))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

# Register MSYS2 UCRT64 bin directory for OpenCV DLLs on Windows
if sys.platform == "win32":
    msys_bin = "C:/msys64/ucrt64/bin"
    if os.path.isdir(msys_bin):
        try:
            os.add_dll_directory(msys_bin)
        except (AttributeError, OSError):
            pass
