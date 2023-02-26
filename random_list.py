def add_to_list(random_list, new_value):
    if new_value in random_list:
        print("Value already in the list.")
    else:
        random_list.append(new_value)
        index = random_list.index(new_value)
        print(random_list[:index+1])

# create a list of random numbers
my_list = [4, 2,1,5,0,8,6]

# add a new value to the list
add_to_list(my_list, 7)
# Output: [4, 2,1,5,0,8,6,7]

# add a new value to the list
add_to_list(my_list, 2)
# Output: Value already in the list.
