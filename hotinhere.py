import sys
import string
import math

cases = int(sys.stdin.readline().rstrip()) 

for caseNum in range(cases): 
    temp = str(sys.stdin.readline().rstrip())

    if "F" in temp:
        tempC = float(temp.replace("F",""))
        tempC2 = (5 / 9) * (tempC - 32)
        rounded_tempC2 = round(tempC2, 1)
        print(f"{temp} = {rounded_tempC2} C")
    else:
        tempF = float(temp.replace("C",""))
        tempF2 = (tempF * (9 / 5)) + 32
        rounded_tempF2 = round(tempF2, 1)
        print(f"{temp} = {rounded_tempF2} F")
