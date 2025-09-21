def find_dup(arr):
    result = {}
    seen = []
    for number in arr:
        if number not in seen:
            result.update({number: 1})
            seen.append(number)
        else:
            return number