num1 = int(input("enter 1st number "))
num2 = int(input("enter 2nd number "))
num3 = int(input("enter 3rd number "))
print("largest======")

if(num1>num2):
    if(num1>num3):
        print(num1)
    else:
        print(num3)
else:
    if(num2>num3):
        print(num2)
    else:
        print(num3)