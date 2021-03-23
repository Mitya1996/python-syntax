def print_upper_words(words, must_start_with):
    """
    docstring
    """
    for word in words: 
        first_letter = word[0].lower()

        for letter in must_start_with:
            if first_letter == letter:
                print(word.upper())


def print_upper_words_refactored(words, must_start_with):
    """
    docstring
    """
    for word in words: 
        for letter in must_start_with:
            if word.startswith(letter):  #found out about startswith method
                print(word.upper())
                break
