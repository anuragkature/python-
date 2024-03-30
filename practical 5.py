# Creating a list and performing the required methods
my_list = []
n = int(input("How many elements do you want to insert in the list? "))
for i in range(n):
    val = int(input("Enter the value: "))
    my_list.insert(i, val)

print("List after inserting elements: ", my_list)

val = int(input("Enter the value to be removed: "))
my_list.remove(val)
print("List after removing the value: ", my_list)

my_list.append(n*10)
print("List after appending: ", my_list)

my_list.sort()
print("Sorted list: ", my_list)

my_list.pop()
print("Popped value: ", my_list.pop())
print("List after popping: ", my_list)

my_list.clear()

# Creating a dictionary and performing the required methods
my_dict = {}
num_keys = int(input("How many keys do you want to add in the dictionary? "))

for i in range(num_keys):
    key = input(f"Enter the key {i+1}: ")
    value = input(f"Enter the value {i+1}: ")
    my_dict[key] = value

print("Dictionary after adding elements: ", my_dict)

print(f"Value of 'key1': {my_dict.get('key1')}")

my_dict['key1'] = 'new_value'

print("Dictionary after changing a value: ", my_dict)

print(f"Number of key-value pairs: {len(my_dict)}")

# Creating a tuple and performing the required methods
my_tuple = tuple(range(1, 11))

num_elems = int(input("How many elements do you want to add in the tuple? "))

new_tuple = ()

for i in range(num_elems):
    val = int(input(f"Enter the value {i+1}: "))
    new_tuple = new_tuple + (val,)

my_tuple = my_tuple + new_tuple

print("Tuple after adding elements: ", my_tuple)

print(f"Number of elements: {len(my_tuple)}")

val_check = int(input("Enter the value to check in the tuple: "))

if val_check in my_tuple:
    print(f"Value {val_check} is present in the tuple")
else:
    print(f"Value {val_check} is not present in the tuple")

print("Accessing the 5th element: ", my_tuple[4])