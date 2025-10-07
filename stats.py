def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
    
def count_words(book_text):
    split_text = book_text.split()
    return len(split_text)

def count_char(book_text):
    chars = list(book_text.lower())
    char_dict = {}

    for c in chars:
        if c in char_dict:
            char_dict[c] += 1
        else:
            char_dict[c] = 1

    return char_dict

def char_list(char_count_dict):
    sorted_list = []

    for c in char_count_dict:
        if c.isalpha():
            char_dict = {"char": c, "num": char_count_dict[c]}
            sorted_list.append(char_dict)

    return sorted(sorted_list, key=lambda d: d["num"], reverse=True)