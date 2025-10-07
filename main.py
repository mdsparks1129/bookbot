import sys
from stats import num_words, num_char, sorted_list

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    text = get_book_text(sys.argv[1])
    print("============ BOOKBOT ============")
    print("Analyzing book found at " + sys.argv[1])
    print("----------- Word Count ----------")
    print(f"Found {num_words(text)} total words")
    print("--------- Character Count -------")
    char_count = num_char(text)
    sorted_char_count = sorted_list(char_count)
    for item in sorted_char_count:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")
    
main()