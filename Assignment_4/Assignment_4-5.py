before = [1, 1, 2, 2, 3, 3, 3, 3, 4, 5, 6, 6, 6, 6, 6, 6 ]
print(f"Before cleaning {before}")

res = []

for i in range(len(before)):
    if before[i] not in res:
        res.append(before[i])

print(f"After cleaning {res}")