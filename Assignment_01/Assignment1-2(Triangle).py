L1 = float(input("Enter line 1: "))
L2 = float(input("Enter line 2: "))
L3 = float(input("Enter line 3: "))

if L1 < L2 + L3 and L2 < L1 + L3 and L3 < L2 + L1:
    print("Possible to draw")
else: print("Impossible to draw")