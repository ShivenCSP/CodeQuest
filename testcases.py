import sys
import math
import string

# Read number of test cases from stdin.
Test_line = sys.stdin.readline().rstrip() # default is a STRING

T = int(Test_line)
print("Number of test cases:", T)

for i in range(T):
    nums = str(sys.stdin.readline().rstrip())
    splits = nums.split()
    num1 = int(splits[0])
    num2 = int(splits[1])
	
    result1 = num1 + num2
    result2 = num1 * num2
	
    print(result1, result2)



