# Parse text, print error if invalid format gets passed in.
file_contents = ""
try:
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
except Exception as e:
    print(f"An error has occured {e}")

# Return number of words in the text.
def count_words(text):
    return len(text.split())

# Count and return the characters in the text.
def count_char(text):
    lowered_string = text.lower()
    char_dict = {}
    for char in lowered_string:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict.update({char : 1})
    return char_dict

# Convert dictionary to alphabetical list
def alphgabetical_sort(dict_of_chars):
    list_of_chars = []
    for char in dict_of_chars:
        if char.isalpha():
            list_of_chars.append(char)
    sorted_list = sorted(list_of_chars)
    return sorted_list

# Display the results
def display(number_of_words, dict_of_chars, list_of_chars):
    
    print("\n--- Begin report of books/frankenstein.txt ---\n")
    print(f"{number_of_words} words found in the document\n")
    for char in list_of_chars:
        print(f"The {char} character was found {dict_of_chars[char]} times")
    print("\n--- End report ---\n")

# Main to run local.
if __name__ == "__main__":
    char_counts = count_char(file_contents)
    sorted_chars = alphgabetical_sort(char_counts)
    num_words = count_words(file_contents)
    display(num_words, char_counts, sorted_chars)