def add_keyvalue_to_list():

    while len(my_list) < 10:
        try:
            key = input("Enter key: ")
            if key in [x[0] for x in my_list]: # check if key is filles already
                print("Key already filled. Please choose another key.")
                continue
            value = input("Enter value: ")
            my_list.append((key, value))
            print("Value added successfully.")
        except Exception as e:
            print(f"An error occurred: {str(e)}")
    print("List is full.")

my_list = []
add_keyvalue_to_list()







