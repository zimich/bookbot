import sys
from stats import convert_dict, get_char_count, get_num_words



def get_book_text(rel_path):
    with open(rel_path) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    full_book = get_book_text(sys.argv[1])
    num_words = get_num_words(full_book)
    unique_chars = get_char_count(full_book)
    sorted_dict = convert_dict(unique_chars)
    print(f'Found {num_words} total words')
    # print(unique_chars)
    # print(sorted_dict)
    for k in sorted_dict:
        print(f"{k['char']}: {k['num']}" )

main()