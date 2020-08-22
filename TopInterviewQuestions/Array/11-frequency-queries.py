#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the freqQuery function below.
def freqQuery(queries):
    output = []
    frequency = {}
    for query in queries:
        if query[0] == 1:
            frequency[query[1]] = frequency.get(query[1], 0) + 1
        elif query[0] == 2:
            if query[1] in frequency and frequency[query[1]] > 0:
                frequency[query[1]] -= 1
        elif query[0] == 3:
            length = len(output)
            for value in frequency.values():
                if value == query[1]:
                    output.append(1)
                    break
            if length == len(output):
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
