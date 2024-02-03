L1 = float(input("enter line 1: "))
L2 = float(input("enter line 2: "))
L3 = float(input("enter line 3: "))

if L1 < L2 + L3 and L2 < L1 + L3 and L3 < L2 + L1:
    print("possible to draw")
else: print("impossible to draw")