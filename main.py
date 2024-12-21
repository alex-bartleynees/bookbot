BOOKS_DIRECTORY = "./books"
SELECTED_BOOK = "frankenstein.txt"

def read_file(path):
    with open(path) as f:
        return f.read()

def get_word_count(text):
    return len(text.split())

def character_count(text):
    char_map = {}
    for char in text:
        if char.isalpha():
            lowered = char.lower()
            if lowered in char_map:
                char_map[lowered] += 1
            else:
                char_map[lowered] = 1
    return char_map
        

file_contents = read_file(f"{BOOKS_DIRECTORY}/{SELECTED_BOOK}")
word_count = get_word_count(file_contents)
char_count = character_count(file_contents)
char_count_sorted = sorted(char_count.items(), key=lambda x: x[1], reverse=True)
print(f"--- Begin report of {BOOKS_DIRECTORY}/{SELECTED_BOOK} ---")
print(f"{word_count} words found in the document")
for key, value in char_count_sorted:
    print(f"The {key} character was found {value} times")
