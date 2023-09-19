#Formating String
age=18
x=19
print("Sunil has Completed" + str(age) + "years")

txt = "Sunil has completed {} years. And entered in {}"
print(txt.format(age,x))

txt = "Sunil has completed {1} years. And entered in {0}"
print(txt.format(age,x))

txt = "Sunil has completed {a} years. And entered in {b}"
print(txt.format(a=age,b=x))

txt = "Sunil has completed {1} years. And entered in {0:.2f}"
print(txt.format(age,x))

