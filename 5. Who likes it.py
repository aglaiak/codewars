def likes(names):
    n = len(names)
    remainder = n - 2
    result = ''
    if n == 0:
        result += f'no one likes this'
    if n == 1:
        result += f'{names[0]} likes this'
    if n == 2:
        result += f'{names[0]} and {names[1]} like this'
    if n == 3:
        result += f'{names[0]}, {names[1]} and {names[2]} like this'
    if n > 3:
        result += f'{names[0]}, {names[1]} and {remainder} others like this'
    return result