def order(sentence: str):
    """ Function that reorders a list based on the numerical info present 
    in the strings """

    n = len(sentence.split())
    result = [''] * n # initializing an empty list with 4 positions
    
    # going over the elements of the string
    for word in sentence.split():
        print(word)
        for letter in word:  
            # checking which value is digit          
            if letter.isdigit():
                # conversion to integer
                idx = int(letter) - 1
                # mapping the new result values to their correct positions
                result[idx] = word
    return ' '.join(result)