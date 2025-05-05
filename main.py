import sys
from stats import get_num_words, count_characters, sort_on

def get_book_text(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        return file.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
    filepath = sys.argv[1]
    book_text = get_book_text(filepath)
    num_words = get_num_words(book_text)
    print(f"Found {num_words} total words")

    char_count = count_characters(book_text)
    sorted_characters = sort_on(char_count)

    print("Characted frequency report (letters only):")
    for item in sorted_characters:
        print(f"{item['char']}: {item['num']}")

# Call main to execute the program
if __name__ == '__main__':
    main()