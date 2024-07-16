def main():
    book_path = "books/frankenstein.txt"
    text = read_book_text(book_path)
    word_count = count_words(text)
    character_count = count_characters(text)
    sorted_count = sort_list_of_dicts(character_count)
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document")
    for dict in sorted_count:
        print(f"The {dict["char"]} character was found {dict["count"]} times")
    print("--- End report ---")


def read_book_text(book_path):
    with open(book_path) as f:
        return f.read()


def count_words(text):
    return len(text.split())


def convert_dict_list(dict):
    list = []
    for entry in dict:
        list.append({'char': entry, 'count': dict[entry]})
    return list


def count_characters(text):
    word_dict = {}
    normalized_text = text.lower()
    for character in normalized_text:
        if not character.isalpha():
            continue
        if character in word_dict:
            word_dict[character] += 1
        if character not in word_dict:
            word_dict[character] = 1

    return convert_dict_list(word_dict)


def sort_on(dict):
    return dict["count"]


def sort_list_of_dicts(list):
    list.sort(key=sort_on, reverse=True)
    return list


main()
