import os
import re

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
def main():
    filename = input("Enter the name of the file to process: ")

    print("Select an option:")
    print("1. Split words into separate lines")
    print("2. Filter word length in wordlist")

    option = input("Enter your choice (1 or 2): ")

    if option == "1":
        split_lines(filename)
        print("Words have been split into separate lines.")
    elif option == "2":
        length = int(input("Enter the desired word length: "))
        filter_words(filename, length)
        print("Words have been filtered to length %d." % length)
    else:
        print("Invalid option. Please select either 1 or 2.")

if __name__ == "__main__":
    main()
