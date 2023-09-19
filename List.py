#List = items are ordered, changable(mutable) and allow duplicate values

list1=[0,1,2,3,4,5,6,7,8]

print(list1)#[0, 1, 2, 3, 4, 5, 6, 7, 8]
print(list1[:6:1])#[0, 1, 2, 3, 4, 5]
print(list1[:6:2])#[0, 2, 4]
print(list1[:6:3])#[0, 3]

print(list1[::1])#[0, 1, 2, 3, 4, 5, 6, 7, 8]
print(list1[::2])#[0, 2, 4, 6, 8]
print(list1[::])#[0, 1, 2, 3, 4, 5, 6, 7, 8]
print(list1[::-1])#[8, 7, 6, 5, 4, 3, 2, 1, 0]
print(list1[::-2])#[8, 6, 4, 2, 0]


list2 = ['a','b',19]
print(type(list2))

#changing value
list2[1]="ss"
print(list2)

#adding items
list2.append("ppp")
print(list2)