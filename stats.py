def get_num_words(book_as_string):
    num_words = len(book_as_string.split())
    return num_words

def get_char_count(book_as_string):
    unique_chars = {}
    for a in book_as_string:
        a = a.lower()
        if a not in unique_chars:
            unique_chars[a] = 1
        else:
            unique_chars[a] += 1
    return unique_chars

def convert_dict(chars_dict):
    new_dict = []
    for a,b in chars_dict.items():
        if a.isalpha():
            new_dict.append({"char":a,"num":b})
    
    new_dict.sort(reverse=True, key=sort_on)
    return new_dict

def sort_on(items):
    return items["num"]