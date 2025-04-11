#!/usr/bin/env python3

import sys
import re

timePattern = re.compile(r':(\d{2}):(\d{2}):(\d{2})')

for line in sys.stdin:
    line = line.strip()
    match = timePattern.search(line)
    
    if match:
        # group(0)은 전체를 의미
        hour = match.group(1)
        print(f'{hour}\t1')
    