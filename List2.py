# list1 = ['aa','bb','cc','dd','ee']
# print(list1)#['aa', 'bb', 'cc', 'dd', 'ee']

# list1[1:3] = ['r','t']
# print(list1)#['aa', 'r', 't', 'dd', 'ee']

# list1[1:3] = ['r','t','s','c','v']
# print(list1)#['aa', 'r', 't', 's', 'c', 'v', 'dd', 'ee']

# list1.insert(2,"Sunil")
# print(list1)#['aa', 'r', 'Sunil', 't', 's', 'c', 'v', 'dd', 'ee']

# list1.remove('t')
# print(list1)#['aa', 'r', 'Sunil', 's', 'c', 'v', 'dd', 'ee'] 

#Extend--------------------------
# list1 = ['a','b','c']
# list2 = ['a','b','c']
# list1.extend(list2)#extend = badha dena(jodnaa)
# print(list1)#['a', 'b', 'c', 'a', 'b', 'c']

#copy one list to second list-------------
# list3 = list1
# list1[2] = "rawat"
# print(list1)#['a', 'b', 'rawat', 'a', 'b', 'c']
# print(list3)#['a', 'b', 'rawat', 'a', 'b', 'c']

#Pop Using------------------------
#pop() =>fatch the last element of list and delete it
# list1 = ['sunil','rawat','suraj','rakesh','mohan']
# print(list1.pop())#Mohan  
# print(list1.pop(0))#Sunil
# print(list1)#['a', 'b', 'rawat', 'a', 'b']  


#Sorting------------
# list1 = ['sunil','rawat','suraj','Sunil','rakesh','mohan']
# list1.sort()
# print(list1)#['mohan', 'rakesh', 'rawat', 'sunil', 'suraj']
# list2 = [1,5,6,7,3,1]
# list2.sort()
# print(list2)#[1, 1, 3, 5, 6, 7]



#Reverse List--------------------------------
# list1 = ['sunil','rawat','suraj','Sunil','rakesh','mohan']
# list1.reverse()
# print(list1)#['mohan', 'rakesh', 'Sunil', 'suraj', 'rawat', 'sunil']

#Copy Method --------------------
list1 = ['sunil','rawat','suraj','Sunil','rakesh','mohan']
list2 = list1.copy()
print(list2)#['sunil', 'rawat', 'suraj', 'Sunil', 'rakesh', 'mohan']