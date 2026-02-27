cases = int(input("Enter number of cases: "))

for i in range(cases):
    equation = input("Enter nums and sign (Example: 1 + 1): ")

    parts = equation.split()   # splits into ["1", "+", "1"]

    num1 = int(parts[0])
    sign = parts[1]
    num2 = int(parts[2])

    if sign == "+":
        result = num1 + num2
        resultR = num2 + num1
    elif sign == "-":
        result = num1 - num2
        resultR = num2 - num1
    elif sign == "*":
        result = num1 * num2
        resultR = num2 * num1
    elif sign == "/":
        result = num1 / num2
        resultR = num2 / num1
    else:
        print("Error")
        continue

    print("Result:", result)
    print("Reverse Result:", resultR)