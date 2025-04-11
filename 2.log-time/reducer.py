#!/usr/bin/env python3

import sys

# 정렬이 되서 들어온다.

last_hour = None
total_count = 0

for line in sys.stdin:
    hour, value = line.split('\t')
    value = int(value)
    if last_hour == hour:
        total_count += value
    else:
        if last_hour is not None:
            print(f'{last_hour}\t{total_count}')
        last_hour = hour
        total_count = value
print(f'{last_hour}\t{total_count}')