from stats import file_word_number, char_number, sort
import sys

def main():
    if len(sys.argv)<2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print("============ BOOKBOT ============")
    path=sys.argv[1]
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    num_words=file_word_number(path)
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    dict_list=sort(char_number(path))
    for i in range (0,len(dict_list)):
        print(f"{dict_list[i]["char"]}: {dict_list[i]["num"]}")
    print("============= END ===============")


main()