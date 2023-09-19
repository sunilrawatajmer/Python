#Get Type---------------
# t =(1,2,3)
# x=len(t)
# print(x)#3
# print(type(t))#tuple

# t2=(10)
# print(type(t2))#int
# t3=(10,)
# print(type(t3))#tuple

#Using 'in' ------------------
# x= 30 in t #False
# y= 3 in t #True
# print(x)
# print(y)

#Tuple to List Covert---------------------------
#If we Want to changes in tuple then Firstly Should be Convert tuple to List
# t4 = ('Sunil','Anil','Suresh')
# lst = list(t4)
# print(lst)
# lst[1]='Rawat'
# print(lst)

#Concinate Tuple------------------
# t4 = ('Sunil','Anil','Suresh')
# t5 = (1,2,3)
# t6 = t4 + t5
# t7 = t5 + t4
# print(t6)#('Sunil', 'Anil', 'Suresh', 1, 2, 3)
# print(t7)#(1, 2, 3, 'Sunil', 'Anil', 'Suresh')

# del Command-----------------------
# t4 = ('Sunil','Anil','Suresh')
# del t4
#print(t4) compiler gives error because tuple is deleted 

#We can assgn tuple in vaariable-------------------
# t4 = ('Sunil','Anil','Suresh')
# (a,b,c) = t4
# print(b)#Anil
# print(a)#Sunil
# print(c)#Suresh

#b will be Remaining all items----------------------------
# (a,*b) = t4
# print(a)#Sunil
# print(b)#['Anil', 'Suresh']

#Count Elements ------------------
# t = (1,2,3,4,5,1,2,3,2,5,6)
# c = t.count(2)
# print(c)#3

#Index-------------------------------
t = (1,2,3,4,5,1,2,3,2,5,6)
indexEle=t.index(5)
print(indexEle)