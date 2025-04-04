from stats import number_of_words, number_of_characters, sort_char_count

def get_book_text(file_path):
    with open(file_path) as f:
        # f is a file object
        file_contents = f.read()
    return file_contents

import sys

def main():
    # contents = get_book_text()
    print("============ BOOKBOT ============\n Analyzing book found at books/frankenstein.txt...")
    num_words = number_of_words(file_contents=get_book_text(file_path))
    num_char = number_of_characters(file_contents=get_book_text(file_path))
    sorted_char_count = sort_char_count(char_count=num_char)
    print("--------- Word Count ---------")
    print(f"Found {num_words} total words")
    print("--------- Character Count ---------")
    print(sorted_char_count)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path = sys.argv[1]
    main()