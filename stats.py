def num_words(text):
    return len(text.split())

def  num_char(text):
    char_count = {}
    for char in text:
        if char.isalpha() == True:
            char = char.lower()
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
        else:
            continue
    return char_count

def sort_on(item):
    return item["num"]

def sorted_list(char_count):
    sorted_list = []
    for ch, cnt in char_count.items():
        if ch.isalpha():
            sorted_list.append({"char": ch, "num": cnt})
    sorted_list.sort(key=sort_on, reverse=True)       
    return sorted_list