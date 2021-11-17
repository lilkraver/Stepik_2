import re
import sys

p = r'human'
for line in sys.stdin:
    print(re.sub(p, 'computer', line.rstrip()))
