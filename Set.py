#List =>  ordered,Mutable,Duplicated Allowed, []
#Tuple =>  ordered,Immutable,Duplicated Allowed, ()
#Set =>  Unordered,Immutable,Duplicated Not Allowed ,{}

#len,type-----------------------
# set1 = {10,20,'Sunil',True,10,1}
# print(set1)#{True, 10, 20, 'Sunil'} => not print duplicated elements (10,1(True))
# print(len(set1))#4
# print(type(set1))

#If we defined Set without any element ,then it is not set it is by default dictionary--------------
# set2 = {}
# print(type(set2))#dict type

#Access Set Elements By For Loop-----------------------------------------
# set ={'Sunil',10,4,True,10}
# for i in set:
#     print(i)

#add,remove,discard--------------------------------------
# set ={'Sunil',10,4,True,10}
# set.add(30)
# print(set)#{True, 4, 10, 'Sunil', 30}
# set.remove('Sunil')
# print(set)#{True, 4, 10, 30}
# set.discard(30)
# print(set)#{True, 4, 10}
#===================
#discard() => if any Elements Which we Want to delete that and this is not find in our Set,
#           Then Discard method Not return Any Error And Remove method is return an error
#del setname => for delete any set----------


#Pop()-------------------------
# set ={'Sunil',10,4,True,10}
# x=set.pop()
# print(x)
# print(set)

#Union,Update(Combining sets ) or (|) => union method returns new set//update replace current set---------------------------------
# set ={'Sunil',10,4,True,10}
# set2 = {1,2,3,4,5}
# set3 = set.union(set2)
# print(set3)#{True, 2, 3, 4, 5, 10, 'Sunil'}
# #AND SECOND IDEA---
# set4 = set | set2
# print(set4)
# #AND THIRD IDEA---
# set5 = set.update(set2)
# print(set5)


# Intersection(common) => return common elements of sets // diffrence(-)  ------------------
# set1 ={6,7,8,4,3,1}
# set2 = {1,2,3,4,5}

# set3 = set1.intersection(set2)
# set4 = set1 & set2

# print(set1)#{1, 3, 4, 6, 7, 8}
# print(set2)#{1, 2, 3, 4, 5}
# print(set3)#{1, 3, 4}
# print(set4)#{1, 3, 4}

# #Diffrence(-) & symmetric_difference(^)-----------------------
# set5=set1.difference(set2)
# set6 = set2 - set1
# set7 = set1.symmetric_difference(set2)
# print(set5)#{8, 6, 7}
# print(set6)#{2, 5}
# print(set7)#{2, 5, 6, 7, 8}

#copy Method--------------------------
# set1 = {1,2,3}
# s2 = set1.copy()
# print(s2)

#disjoint method--------------------
# set1 = {1,2,3}
# set2 = {1,2,3}
# set3= {11,22,33}
# set4 = set1.isdisjoint(set2)
# set5 = set1.isdisjoint(set3)
# print(set4)#false
# print(set5)#true

#issuperset//issubset------------------------------------------
set1 = {1,2,3}
set2 = {1,2,3}
p=set2.issuperset(set1)#True
q=set2.issubset(set1)#True
print(p)
print(q)


