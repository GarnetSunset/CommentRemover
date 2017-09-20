import os
import re
import sys

owd = os.getcwd()

if not os.path.exists("DoYaThing"):
    os.makedirs("DoYaThing")
    print("Put Files In \"DoYaThing\" Please")
    sys.exit()

for dname, dirs, files in os.walk("DoYaThing"):
    for fname in files:
        fpath = os.path.join(dname, fname)
        with open(fpath) as f:
            s = f.read()
        s = re.sub(re.compile("/\*.*?\*/",re.DOTALL ) ,"" ,s)
        s = re.sub(re.compile("//.*?\n" ) ,"" ,s)
        with open(fpath, "w") as f:
            f.write(s)
