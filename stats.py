def get_num_words(filepath):
    with open(filepath) as f:
        file_content = f.read()
        words_count = len(file_content.split())
        return words_count

def get_num_chars(filepath):
    stats = {}
    with open(filepath) as f:
        for char in f.read():
           norm_char = char.lower()
           if norm_char not in stats:
             stats[norm_char] = 0
           stats[norm_char] += 1
    return stats
