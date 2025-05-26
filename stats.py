def get_num_words(text):
    words = text.split()
    return len(words)

def count_letters(text):
    result = {}
    for symbol in text:
        symbol = symbol.lower()
        if symbol.isalpha():
            if symbol in result:
                result[symbol] += 1
            else:
                result[symbol] = 1
    return result

def sort_on(dict):
    return dict["num"]

def sort_dict(result):
    new_list = []
    for char, count in result.items():
        new_dict = {"char":char, "num": count}
        new_list.append(new_dict)
    new_list.sort(key=sort_on, reverse=True)
    return new_list
