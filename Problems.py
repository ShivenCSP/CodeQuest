cases = int(input())

for i in range(cases):
    line = input().strip()
    V_str, X_str = line.split(":")
    V = float(V_str)
    X = float(X_str)

    if V == 0:
        print("SAFE")
    else:
        time = X / V

        if time <= 1:
            print("SWERVE")
        elif time <= 5:
            print("BRAKE")
        else:
            print("SAFE")