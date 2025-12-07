import sys
from stats import *

def get_book_text(path):
    # The 'with' statement ensures the file is automatically closed
    with open(path) as f:
        book_text = f.read()
        return book_text


def main ():
    try:
        filepath=sys.argv[1]
        contents=get_book_text(filepath)
        length=stats(contents)
        count=char_count(contents)
        chars=sorted_dict(count)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {filepath}")
        print("----------- Word Count ----------")
        print(f"Found {length} total words")
        print("--------- Character Count -------")
        for i in range (0,len(chars)):
            char_value = chars[i]["char"]
            if char_value.isalpha():
                print(f"{chars[i]["char"]}: {chars[i]["num"]}")
        print ("============= END ===============")
    except Exception as e:
        print("- 'Usage: python3 main.py <path_to_book>'")
        sys.exit(1)




main()