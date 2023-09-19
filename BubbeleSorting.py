lst1 = [11, 49, 6, 57, 9, 3, 7]
print(lst1)
n = len(lst1)

for i in range(n - 1):
    for j in range(0, n - i - 1):
        if lst1[j] > lst1[j + 1]:
            lst1[j], lst1[j + 1] = lst1[j + 1], lst1[j]

print(lst1)