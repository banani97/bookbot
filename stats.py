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
