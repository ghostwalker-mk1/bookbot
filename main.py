from stats import get_num_words
from stats import get_num_characters
from stats import sort_dict
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():

    if len(sys.argv) != 2:

        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    else:
        inp = sys.argv[1]
        book = get_book_text(inp)
        num_words = get_num_words(book)
        num_chars = get_num_characters(book)
        sorted_dict = sort_dict(num_chars)

        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {inp}...")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")
        
        for dict in sorted_dict:
            if dict['char'].isalpha():
                print(f"{dict['char']}: {dict['num']}")
            else:
                pass

        print("============= END ===============")
            
main()