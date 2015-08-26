import sys

# Easy way to detect Python Version
MAJOR, MINOR, _, _, _ = sys.version_info

if MAJOR >= 3 or (MAJOR == 2 and MINOR >= 7):
    print("We are running python3")
else:
    print("We are running python2")
