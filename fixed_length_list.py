def add_to_list(value, lst):
    try:
        # Try to convert the user's input to a number
        value = int(value)
    except ValueError:
        # If the input cannot be converted to a number, print an error message and return
        print("Error: Invalid input. Please enter a number.")
        return

    # If the list already has 5 values, remove the oldest value the one at the bottom of the list using stack
    if len(lst) >= 5:
        lst.pop(0)

    # Add the new value to the top of the list  
    lst.append(value)

    return lst


#usage of method
my_list = []
my_list = add_to_list("1", my_list)
my_list = add_to_list("2", my_list)
my_list = add_to_list("3", my_list)
my_list = add_to_list("4", my_list)
my_list = add_to_list("0", my_list)
my_list = add_to_list("8", my_list)
my_list = add_to_list("9", my_list)


print(my_list)  # Output: [3,4,0,8,9]