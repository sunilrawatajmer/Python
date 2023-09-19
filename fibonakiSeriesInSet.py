#FibonaKiSeries-----------------------

# set = {1}
# a=0
# b=1
# c=0
# limit = int(input("Enter The Limit For Series : "))
# for i in range(limit):
#     c=a+b
#     a=b
#     b=c
#     set.add(b)
# print(set)


#Print Series Of Squares of Number---------------------------
set = {1}
limit = int(input("Enter The Limit For Series : "))
for i in range(limit):
    sqr = i * i
    set.add(sqr)
print(set)