#!/usr/bin/env python3
import sys
from collections import defaultdict

word_count = defaultdict(int)

for line in sys.stdin:
    line = line.strip()
    word, count = line.split('\t', 1)
    try:
        count = int(count)
    except ValueError:
        continue
    word_count[word] += count

for word in sorted(word_count):
    print(f'{word}\t{word_count[word]}')
