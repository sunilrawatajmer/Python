#Prime or not prime
num = int(input("Enter number : "))
i=2
c=0
while num>i:
    if num%i==0:
        c=c+1
    i=i+1
if c>0:
    print("not prime")
else:
    print(" prime")