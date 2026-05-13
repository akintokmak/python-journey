numbers = [1,2,3]
new_number = [n + 1 for n in numbers]
print(new_number)
#-----------------------------------------------------------------
name = "AKIN"
new_list = [letter for letter in name]
print(new_list)
#-----------------------------------------------------------------
new_list2 = [num * 2  for num in range(1,5)]
print(new_list2)
#-----------------------------------------------------------------
names = ["Akin","Sule","Erenay","Sibel","Ayla"]
short_names = [name for name in names if len(name) <= 4]
print(short_names)
long_names = [name.upper() for name in names if len(name) > 4]
print(long_names)

list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
numbers = [int(num) for num in list_of_strings]
result = [num for num in numbers if num % 2 == 0]
print(result)