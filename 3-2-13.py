import sys
import re

for line in sys.stdin:
    line = re.sub(r"\ba+\b", "argh", line.rstrip(), 1, flags=re.IGNORECASE)
    print(line)
    
    
    
import re
import sys

for line in sys.stdin:
    print(re.sub(r'\b[Aa]+\b', 'argh', line.strip(), 1))
