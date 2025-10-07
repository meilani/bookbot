import sys
from stats import *
    
def main():
    if len(sys.argv) != 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)

    book_path = sys.argv[1]
    book_contents = get_book_text(book_path)
    num_words = count_words(book_contents)
    num_char = count_char(book_contents)
    sorted_list = char_list(num_char)

    print('============ BOOKBOT ============')
    print(f'Analyzing book found at {book_path}...')
    print('----------- Word Count ----------')
    print(f'Found {num_words} total words')
    print('--------- Character Count -------')

    for c in sorted_list:
        print(f'{c["char"]}: {c["num"]}')

    print('============= END ===============')

main()