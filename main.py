from stats import get_chars_stat, get_num_words
from stats import get_num_chars

def main():
    book_path = "books/frankenstein.txt"
    nums_word = get_num_words(book_path)
    nums_char = get_num_chars(book_path)
    chars_stat = get_chars_stat(nums_char)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}... ")
    print("----------- Word Count ----------")
    print(f"Found {nums_word} total words")
    print("Found 75767 total words")
    print("--------- Character Count -------")
    for item in chars_stat:
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["num"]}")
    print("============= END ===============")

main()
