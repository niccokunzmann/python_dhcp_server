"""Run the app.

On macos, we might not be able to import anything.
"""
import sys
import os
from pathlib import Path

HERE = Path(__file__).parent

sys.path.append(str(HERE.parent))

# We should not save the files next to the app.
# CWD = Path(sys.executable).parent.parent.parent.parent
# They should be in $HOME/Library/Caches
CWD = Path.home() / "Library" / "Caches" / "eu.quelltext.dhcp"
CWD.mkdir(parents=True, exist_ok=True)

f = open(CWD / "Simple DHCP Server.log", "w")

print("cwd", os.getcwd(), file=f)
print("here", str(HERE) , file=f)
print("executable", sys.executable, file=f)
print("cwd", CWD, file=f)

os.chdir(str(CWD))

try:
    from simple_dhcp_server.tk import main
    main()
except:
    import traceback
    traceback.print_exc(file=f)
