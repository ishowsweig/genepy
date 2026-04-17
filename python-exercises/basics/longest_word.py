def longest_word(text):
    words = text.split()
    longest_word_length = 0
    longest_word = None
    for word in words:
        if len(word) > longest_word_length:
            longest_word = word
            longest_word_length = len(word)
    return longest_word
