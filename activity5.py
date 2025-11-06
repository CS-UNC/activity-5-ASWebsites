def more_than_20(file):
    long_words = []
    words_file = open('CROSSWD.txt', 'r')
    for line in words_file:
        word = line.strip()
        if len(word) > 20:
            long_words.append(word)
    return long_words
print(more_than_20('CROSSWD.txt'))

def has_no_e(word):
    return 'e' not in word
print(has_no_e('CROSSWD.txt'))

def uses_only(word, letters):
    for ch in word:
        if ch not in letters:
            return False
    return True
print(uses_only('CROSSWD.txt', 'abra'))

def all_uses_only(file, letters):
    valid_words = []
    words_file = open('CROSSWD.txt', 'r')
    for line in words_file:
        word = line.strip()
        if uses_only(word, letters):
            valid_words.append(word)
    return valid_words
print(all_uses_only('CROSSWD.txt', 'abrz'))
