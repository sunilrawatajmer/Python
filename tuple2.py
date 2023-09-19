 #Covert Tuple to list And prit its reverse------------------
# t = (1,2,3,4)
# lst=[]
# l=len(t)
# i=l-1
# while 0<=i:
#     lst.append(t[i])
#     i-=1
# print(lst)


#print Prime Elements list from tuple----------------------
t = (1,2,3,5,4,7,8,9,10)
l=len(t)
i=0
lst=[]
for i in range(l):
    flag=0
    for j in range(2,t[i]):
        if t[i]%j==0:
            flag+=1
    if flag==0:
        lst.append(t[i])
    i+=1

print(lst)

