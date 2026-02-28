import sys
import string
import math
import decimal

cases = int(sys.stdin.readline().rstrip()) 

for i in range(cases): 
    teams = int(sys.stdin.readline().rstrip())

    total_grains = 0

    for t in range(teams):
        grains = int(sys.stdin.readline().rstrip())
        total_grains += grains 

print(total_grains)

    