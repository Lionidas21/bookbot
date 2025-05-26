import sys
from stats import count_letters
from stats import get_num_words
from stats import sort_dict

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def main():
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    count_symbols = count_letters(text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    sorting = sort_dict(count_symbols)
    for item in sorting:
        print(item["char"]+":",item["num"])
    print("============= END ===============")

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()
