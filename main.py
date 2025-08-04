from stats import get_num_words

def main():
    nums_word = get_num_words("books/frankenstein.txt")
    print(f"{nums_word} words found in the document")

main()
