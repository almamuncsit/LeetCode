#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict, Counter

# Complete the freqQuery function below.
def freqQuery(queries):
    output = []
    frequency = {}
    frequency_number = defaultdict(set)
    for query, value in queries:
        if query == 1:
            if value in frequency:
                frequency_number[frequency[value]].discard(value)
            frequency[value] = frequency.get(value, 0) + 1
            frequency_number[frequency[value]].add(value)
        elif query == 2:
            if value in frequency and frequency[value] > 0:
                frequency_number[frequency[value]].discard(value)
                frequency[value] -= 1
                if frequency_number[value] == 0:
                    del frequency_number[value]
                else:
                    frequency_number[frequency[value]].add(value)
        elif query == 3:
            if value in frequency_number and len(frequency_number[value]) > 0:
                output.append(1)
            else:
                output.append(0)
            
    return output

            

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())
    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)
    print(ans)
    # fptr.write('\n'.join(map(str, ans)))
    # fptr.write('\n')

    # fptr.close()
