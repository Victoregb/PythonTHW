def break_words(stuff):
    '''This function will break words for us'''
    words = stuff.split(' ')
    return words

def sort_words(words):
    '''Sort the words'''
    return sorted(words)

def print_first_word(words):
    '''Prints the first word after popping it off'''
    word = words.pop(0)
    return print(word)

def print_last_word(words):
    '''Prints the last word after popping it off'''
    word = words.pop(-1)
    return print(word)

def sort_sentence(sentence):
    '''Takes a full sentence and return the sorted words'''
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    '''Prints the first and last words of the sentence.'''
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)
    
def print_first_and_last_sorted(sentence):
    print("Aqui estoy")
    "El problema es que no se importaba correctamente la libreria."
    '''Sorts the words then prinqts the first and last one.'''
    words = sort_sentence(sentence)
    print(words)
    print_first_word(words)
    print_last_word(words)
