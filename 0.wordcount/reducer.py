#!/usr/bin/env python3

import sys

# 정렬이 되서 들어온다.

last_word = None
total_count = 0

for line in sys.stdin:
    word, value = line.split('\t')
    value = int(value)
    if last_word == word:
        total_count += value
    else:
        if last_word is not None:
            print(f'{last_word}\t{total_count}')
        last_word = word
        total_count = value
if last_word == word:
    print(f'{last_word}\t{total_count}')