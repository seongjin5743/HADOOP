#!/usr/bin/env python3

import sys

# 정렬이 되서 들어온다.

current_movie = None
current_sum = 0
current_count = 0

for line in sys.stdin:
    movie_id, rating = line.split('\t')
    try:
        rating = float(rating)
    except:
        continue

    if current_movie == movie_id:
        current_count += 1
        current_sum += rating
    else:
        if current_movie is not None:
            print(f'{current_movie}\t{current_sum / current_count}')
        current_movie = movie_id
        current_sum = rating
        current_count = 1

if current_movie == movie_id:
    print(f'{current_movie}\t{current_sum / current_count}')