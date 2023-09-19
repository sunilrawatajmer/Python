#List        =>   ordered, mutable, duplicate allowed 
#Tuple       =>   ordered, Unmutable, duplicate allowed 
#Set         =>   Unordered, Unmutable but can add/remove, duplicate not allowed 
#Dictionary  =>   Ordered , Mutable, Duplicate not allowed{Key : Value}

#Make Dictionary-------------------------------------------------------
d = {"rollno":101, "name":'Sunil', "class":9}
print(d)#{'rollno': 101, 'name': 'Sunil', 'class': 9}
print(d['name'])#Sunil
print(d.keys())#dict_keys(['rollno', 'name', 'class'])
print(d.values())#dict_values([101, 'Sunil', 9])
print(d.items())#dict_items([('rollno', 101), ('name', 'Sunil'), ('class', 9)])