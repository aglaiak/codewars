def spin_words(sentence):
    
    n = len(sentence.split()) # amount of words
    result = []
    
    for word in sentence.split():
        if len(word) >= 5:
            # appending the reversed variations
            result.append(word[::-1])
        else:
            result.append(word)
    return ' '.join(result)