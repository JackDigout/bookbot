def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = count_letters(text)
    list_of_dicts = [{"letter": key, "count": value} for key, value in chars_dict.items()]

    list_of_dicts.sort(reverse=True, key=sort_on)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document")
    
    for dict in list_of_dicts:
        if dict["letter"].isalpha():
            print(f"The '{dict['letter']}' character was found {dict["count"]} times")


    
    

    

def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()



def count_letters(text):
    chars = {}
    for c in text:
        lowered = c.lower()

        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    
    return chars

def sort_on(dict):
    return dict["count"]


main()  
