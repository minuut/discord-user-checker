import os
import re

def split_lines(filename):
    file_path = os.path.join("wordlists", filename)

    try:
        with open(file_path, 'r') as file:
            words = file.read().split()
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return

    if not words:
        print(f"Error: File '{file_path}' is empty.")
        return

    filtered_words = []
    for word in words:
        filtered_word = re.sub(r'[^a-zA-Z]', '', word)
        filtered_words.append(filtered_word)

    with open(file_path, 'w') as file:
        for word in filtered_words:
            file.write(word + '\n')

def filter_words(filename, length):
    pattern = re.compile(r'^[a-zA-Z]{%d}$' % length)
    file_path = os.path.join("wordlists", filename)

    try:
        with open(file_path, 'r') as file:
            words = file.read().split()
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return

    filtered_words = [word for word in words if re.match(pattern, word)]

    with open(file_path, 'w') as file:
        for word in filtered_words:
            file.write(word + '\n')

def filter_words_and_save_by_length(filename):
    file_path = os.path.join("wordlists", filename)

    try:
        with open(file_path, 'r') as file:
            words = file.read().split()
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return

    word_dict = {}
    for word in words:
        word_length = len(word)
        pattern = re.compile(r'^[a-zA-Z]{%d}$' % word_length)
        if re.match(pattern, word):
            if word_length not in word_dict:
                word_dict[word_length] = []
            word_dict[word_length].append(word)

    for word_length, words in word_dict.items():
        output_file_path = os.path.join("wordlists", f'{word_length}char.txt')
        with open(output_file_path, 'w') as file:
            for word in words:
                file.write(word + '\n')


def main():

    print("""
    Option 1: Splits words into separate lines by removing any non-alphabetic characters.
    Option 2: Filters the words in the file to a specific length input by the user.
    Option 3: Filters the words in the file by their length and saves them into separate files named according to their length 
    (i.e., 4-letter words will be saved in a file named '4char.txt', 5-letter words in '5char.txt', and so on)
    this can be useful when you have a gigantic wordlist.
    """)

    filename = input("Enter the name of the file to process: ")

    print("Select an option:")
    print("1. Split words into separate lines")
    print("2. Filter word length in wordlist")
    print("3. Filter word length in wordlist and save to separate files")

    option = input("Enter your choice (1, 2 or 3): ")

    if option == "1":
        split_lines(filename)
        print("Words have been split into separate lines.")
    elif option == "2":
        length = int(input("Enter the desired word length: "))
        filter_words(filename, length)
        print("Words have been filtered to length %d." % length)
    elif option == "3":
        filter_words_and_save_by_length(filename)
        print("Words have been filtered by length and saved to separate files.")
    else:
        print("Invalid option. Please select either 1, 2 or 3.")

if __name__ == "__main__":
    main()
