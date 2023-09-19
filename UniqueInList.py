lst1 = [1, 2, 2, 3, 4, 4, 5]
unique = []
[unique.append(x) for x in lst1 if x not in unique]
print(unique)