def number_of_words(file_contents):
    words = file_contents.split()
    return len(words)

# This functions counts the number of times each character appears in the text
def number_of_characters(file_contents):
    # Create a dictionary to store the character counts
    char_count = {}
    # Loop through each character in the file contents
    for char in file_contents.lower():
        if char != " ":    
            # If the character is not already in the dictionary, add it with a count of 1
            if char not in char_count:
                char_count[char] = 1
            # If the character is already in the dictionary, increment its count by 1
            else:
                char_count[char] += 1
    return char_count

# This function takes in char_count and sorts it by the number of occurrences greatest to least in a virtical list
def sort_char_count(char_count):
    # Sort the dictionary by value (character count) in descending order
    sorted_char_count = dict(sorted(char_count.items(), key=lambda item: item[1], reverse=True))
    # Create a string to store the sorted character counts
    sorted_count_str = ""
    # Loop through the sorted character counts and add them to the string
    for char, count in sorted_char_count.items():
        sorted_count_str += f"{char}: {count}\n"
    return sorted_count_str
    