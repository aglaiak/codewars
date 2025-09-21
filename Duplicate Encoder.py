def duplicate_encode(word):
    # collect the letters in a list
    word_count = {}
    seen = []
    result = []
    
    letters = [letter.lower() for letter in word]
    
    for letter in letters:
        if letter not in seen:
            seen.append(letter)
            word_count.update({letter:1})
        else:
            word_count[letter] += 1
    
    for letter in letters:
        for keys, values in word_count.items():
            if letter == keys and values == 1:
                result.append('(')
            if letter == keys and values > 1:
                result.append(')')
    return ''.join(result)