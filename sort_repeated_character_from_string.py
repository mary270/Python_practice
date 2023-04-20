try:
    string = input("Enter a string: ")
    # Remove all non-alphabetic characters from the string
    string = ''.join(filter(str.isalpha, string))
    # Convert the string to lowercase
    string = string.lower()
    # Create a dictionary to store the frequency of each character in the string
    char_freq = {}
    for char in string:
        if char in char_freq:
            char_freq[char] += 1
        else:
            char_freq[char] = 1
    # Sort the dictionary by frequency in descending order
    sorted_char_freq = sorted(char_freq.items(), key=lambda x: x[1], reverse=True)
    # Print the sorted characters and their frequencies
    print("Sorted characters and their frequencies:")
    for char, freq in sorted_char_freq:
        if freq > 1:
            print(char, freq)
except Exception as e:
    print("An error occurred:", e)
