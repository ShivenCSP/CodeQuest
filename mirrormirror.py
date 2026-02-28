import sys
import string
import math

cases = int(sys.stdin.readline().rstrip()) 

for i in range(cases): 
    text = str(sys.stdin.readline().rstrip())

    print(text[::-1])
    