from stats import get_num_words
from stats import get_num_chars

def main():
    nums_word = get_num_words("books/frankenstein.txt")
    nums_char = get_num_chars("books/frankenstein.txt")
    print(f"{nums_word} words found in the document")
    print(nums_char)

main()
