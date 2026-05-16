my_dict = {}

my_dict = {1: "Blueberry", 2: "Tennis"}

my_dict = {"name" : "Uzy", 1: [2,4,3]}

my_dict = {"name" : "Uzayr", "age" : 9}

print(my_dict['name'])
print(my_dict.get('age'))

my_dict["age"] = 10
print(my_dict)

my_dict["address"] = "Mirpur 6"
print(my_dict)

print("Address :", my_dict.get('address'))

my_dict.clear()
print(my_dict)