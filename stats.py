def get_num_words(filepath):
    with open(filepath) as f:
        file_content = f.read()
        words_count = len(file_content.split())
        return words_count
