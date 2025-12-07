def stats(book):
    length = len(book.split())
    return length

def char_count(text):
    new_dict={}
    lower_text=text.lower()
    new_text=list(lower_text)
    for char in new_text:
        if char in new_dict:
            new_dict[char]+=1
        else:
            new_dict[char]=1
    return new_dict

def sort_on(dic):
    return dic["num"]

def sorted_dict(dic):
    structured_list = [
        {
            "char": key,
            "num": value
        }
        for key, value in dic.items()]
    structured_list.sort(reverse=True, key=sort_on)
    return structured_list


