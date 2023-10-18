import re
def normalize_word(word):
    return re.sub(r'[^a-zA-Z]', '', word).lower()
while True:
    input_str = input("please enter two words (or 'done' to exit): ")
    if not input_str or input_str.lower() == 'done':
        break
    words = input_str.split()
    if len(words) != 2:
        print("please enter exactly two words separated by a space.")
    else:
        word1, word2 = words
        normalized_word1 = normalize_word(word1)
        normalized_word2 = normalize_word(word2) 
        if normalized_word1 < normalized_word2:
            print(f"{word1} comes first")
        else:
            print(f"{word2} comes first")
