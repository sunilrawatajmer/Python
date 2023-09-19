#print reverse of any number
num = int(input("Enter Any Number : "))
r=0
sum=0
while(num>0):
    r=num%10
    print(r,end="")
    num = num//10