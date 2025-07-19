def get_num_words(str):
    total = 0

    words = str.split()
    for word in words:
        total += 1

    return total

def get_num_characters(str):
    dict = {}

    for char in str:
        char = char.lower()
        if char not in dict:
            dict[char] = 1
        else:
            dict[char] += 1
    
    return dict

def num(e):
    return e["num"]

def sort_dict(dict):
    dict_list = []

    for char, count in dict.items():
        dict_list.append({"char": char, "num": count})

    dict_list.sort(reverse=True, key=num)

    return dict_list