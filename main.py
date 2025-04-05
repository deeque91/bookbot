from stats import word_count, letter_count, sort
import sys

def main():
    
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    frankenstein_read = get_book_text(book_path)
    words_count = word_count(frankenstein_read)
    library_dict = letter_count(frankenstein_read)
    sorted_list = sort(library_dict)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {words_count} total words")
    print("--------- Character Count -------")
    for item in sorted_list:
        char = item["name"]
        if char.isalpha():
            print(f"{char}: {item['num']}")
    print("============= END ===============")
    
    


def get_book_text(path):
    with open(path) as f:
        return f.read()
    






main()