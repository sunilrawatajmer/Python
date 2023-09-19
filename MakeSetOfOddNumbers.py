#Make Set of Odd Numbers And print Them and Do Operation(add,remove) on set
set={31}
for i in range(30,50):
    if i%2!=0:
        set.add(i)
print(set)

removeNum = int(input("Enter a Elemet : "))
set.remove(removeNum)
print(set)

# len=len(set)
# for i in range(len):
#     if removeNum in set:
#         set.remove(removeNum)
# print(set)