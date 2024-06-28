def khayyam_paskal(n):
    rows = []
    for i in range(n):
        row = []
        i += 1
        for j in range(i):
            if j == 0:
                print("1", end=' ')
                row.append(1)
                continue
            try:
                num = rows[i - 2][j] + rows[i - 2][j - 1]
            except IndexError:
                num = 1
            row.append(num)
            print(f"{num}", end=' ')
        rows.append(row)
        print("")
    return rows


khayyam_paskal(int(input("Enter a number: ")))
