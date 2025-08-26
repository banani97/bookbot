def get_book_text(file_path):
    with open(file_path) as f:
        file_contents=f.read()
    return file_contents

def file_word_number(file_path):
    word_list=get_book_text(file_path).split()
    return (len(word_list))

def char_number(file_path):
    number_letters={}
    word_list=(get_book_text(file_path).lower()).split()
    for word in word_list:
        for letter in word:
            if letter in number_letters:
                number_letters[letter]+=1
            else:
                number_letters[letter]=1
    return number_letters

def helper_sort(items):
    return items["num"]

def sort(char_dict):
    char_dict_list=[]
    for i in char_dict:
        single_char_dict={}
        single_char_dict["char"]=i
        single_char_dict["num"]=char_dict[i]
        if i.isalpha():
            char_dict_list.append(single_char_dict)
    char_dict_list.sort(reverse=True, key=helper_sort)
    return char_dict_list
