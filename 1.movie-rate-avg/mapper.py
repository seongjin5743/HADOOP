#!/usr/bin/env python3

import sys

for line in sys.stdin:
    line = line.strip()
    fields = line.split(',')

    movie_id = fields[1]
    rating = fields[2]

    print(f'{movie_id}\t{rating}')