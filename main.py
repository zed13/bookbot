def get_book_text(filepath):
    with open(filepath) as f:
        file_content = f.read()
        return file_content

def main():
    content = get_book_text("books/frankenstein.txt")
    words_count = len(content.split())
    print(f"{words_count} words found in the document")

main()
