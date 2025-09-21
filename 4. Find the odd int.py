def find_it(seq): 
    """ Function that returns the number that appears an odd amount of times"""
    count_dict = {} # dictionary that saves the number instances
    seen = [] # the list with the already seen numbers
    # populating the count_dict dictionary
    for number in seq:
        if number not in seen:
            seen.append(number)
            count_dict.update({number: 1})
        else:
            count_dict[number] += 1
    # checking which key has an odd value and returning the corresponding key
    for key, value in count_dict.items():
        if value % 2 != 0:
            return key
        