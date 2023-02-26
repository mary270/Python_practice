def create_multi_array(first_size, assoc_size):
    # Initialize empty array
    multi_array = []

    # Create first list
    first_list = list(range(first_size))

    # Create associative list for each value in first list
    for val in first_list:
        assoc_list = [f"{val},{i}" for i in range(assoc_size)]
        multi_array.append(assoc_list)

    # Display array in table format
    for row in multi_array:
        print("|", end="")
        for col in row:
            print(f" {col} |", end="")
        print()


# Call method with user input for list sizes
first_size = int(input("Enter size of first list: "))
assoc_size = int(input("Enter size of associative list: "))
create_multi_array(first_size, assoc_size)
