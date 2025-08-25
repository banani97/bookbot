from stats import file_word_number, char_number

def main():
    path="books/frankenstein.txt"
    num_words=file_word_number(path)
    print(f"{num_words} words found in the document")
    print (char_number(path))


main()