from orange._parser import parse
import sys
import os

filename = sys.argv[1]
if os.path.exists(filename):
    with open(filename, 'r') as f:
        code = f.read()
    
    parse(code)
    sys.exit()

print('file not found')