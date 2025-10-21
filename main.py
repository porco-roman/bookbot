import sys 
from stats import *

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

book_path = sys.argv[1]

def get_book_text(book_path): 
    with open(book_path, mode="r", encoding="utf-8") as f:
        return f.read()

def main():
    body = get_book_text(book_path)
    message = f"Found {num_of_words(body)} total words"
    count = character_count(body)
    sorted_dict = sorted_list(count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path} ...")
    print( "----------- Word Count ----------")
    print(message)
    print("--------- Character Count -------")

    for item in sorted_dict:
        ch = item["char"]
        if ch.isalpha():
            print(f"{ch}: {item['num']}")
 
    print("============= END ===============")
    
if __name__ == "__main__":                  
    main()