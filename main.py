def get_book_text(filepath):
    with open(filepath) as f:
        file_content = f.read()
        print(file_content)

def main():
    get_book_text("books/frankenstein.txt")

main()
