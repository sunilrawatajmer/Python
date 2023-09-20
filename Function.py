# Sum Of Two Numbers -------------------
# def fun(a,b):
#     return (a+b)
# x = fun(10,20)
# print(x)

#Factorial of Given Number------------------
# num = int(input("Enter a NUmber : "))
# def fact(n):
#     f=1
#     while n!=0:
#         f=f*n
#         n=n-1
#     return f
# x = fact(num)
# print(x)


#find number is Armstrong or not -----------------------------
# num = int(input("Enter a Number : "))
# origanal = num
# def Arm(n):
#     sum=0
#     while n>0:
#         r=n%10
#         sum=sum+(r*r*r)
#         n=n//10
#     return sum
    
# # pass number as argument....
# x = Arm(num)
# if x == origanal:
#     print("Armstrong")
# else:
#     print("Not")


#Check Number is Prime or Not--------------------------------------
# num = int(input("Enter a Number : "))
# def prm(n):
#     c=0
#     for i in range(2,n):
#         if n%i==0:
#             c=c+1
#     if c>0:
#         return False
#     else:
#         return True
# # Pass Args...
# x = prm(num)
# if x==True:
#     print("Prime")
# else:
#     print("Not Prime")


#ODd or Even----------------------------------
# num = int(input("Enter a Number : "))
# def EvenOdd(n):
#     if n%2==0:
#         return "Even"
#     else:
#         return "Odd"
    
# result = EvenOdd(num)
# print(result)


#Variable number of Arguments--------------------------------------
# def fun(*a):
#     print(a[1])
#     print(a[0])

# fun('sunil','Rawat','Mohan','Anil')


# Keyword Arguments---------------------------------------------
# def fun(a,b,c):
#     print(a)
#     print(b)
#     print(c)
# fun(c="Sunil",a='Jaipur',b='Kota')


# Empty Function(Pass Statement)-------------------------------------
# def fun():
#     pass
# fun()


# Local Variable--------------------
# def fun():
#     a=10
#     print(a)
# fun()


# Globle Variable-----------------------------------
# x=20
# def fun():
#     print(x)
# fun()

# Change value of globle variable-----------------------------
# x=20
# def fun():
#     global x
#     print(x)
#     x=50
#     print(x)
# fun()


# globals Method--------------------------------------
# a=20
# def fun():
#     a=10
#     print(a)#10
#     print(globals())
#     print(globals()['a'])#20
# fun()


# Recurtion function------------------
# x=1
# def fun():
#     global x
#     print(x,end=" ")
#     x=x+1
#     if x>5:
#         return
#     fun()
# fun()


# Lambda/Anonymous------------------------------
# lamda arguments : expretion
fun = lambda x:x*2
print(fun(5))

