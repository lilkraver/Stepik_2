import sys
import re

for line in sys.stdin:
    line = line.rstrip()
    if re.search(r'\b(cat)\b', line):
        print(line)
