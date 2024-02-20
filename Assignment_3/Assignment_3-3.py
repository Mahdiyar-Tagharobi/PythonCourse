lst = list(map(int, input("please enter numbers in your list to review(enter space between them): ").split()))

checker = True
print(lst)
for i in range(len(lst) - 1):
    if lst[i] > lst[i + 1]:
        checker = False

if checker:
  print("True")
else:
  print("False")
