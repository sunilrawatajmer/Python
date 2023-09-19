txt ="SunilL"
# print(txt.count("l"))#1
# print(txt.lower().count("l"))#2

# print(txt.endswith("ll"))#False
# print(txt.startswith("Su"))#True

x=txt.index("il")
print(x)
y=txt.rindex("l")
print(y)

a1="sunil"
a2="123"
a3=" "
print(a1.isalpha())#true
print(a2.isalpha())#false
print(a1.isnumeric())#false
print(a2.isnumeric())#true
print(a3.isspace())#true
