def solution(mtrx):    
    
    arrows = ['^', '>', 'v', '<']
    # finding the position of the x and arrow
    
    
    for idx, row in enumerate(mtrx):
        for i in range(len(mtrx)):
            if row[i] in arrows:
                arrow_row = idx
                arrow_col = i
            if row[i] == 'x':
                x_row = idx
                x_col = i
            
       
    if arrow_row == x_row and arrow_col < x_col:
        if mtrx[arrow_row][arrow_col] == '>':
            return True
        else:
            return False
    if arrow_row == x_row and arrow_col > x_col:
        if mtrx[arrow_row][arrow_col] == '<':
            return True
        else:
            return False
    if arrow_col == x_col and arrow_row < x_row:
        if mtrx[arrow_row][arrow_col] == 'v':
            return True
        else:
            return False
    if arrow_col == x_col and arrow_row > x_row:
        if mtrx[arrow_row][arrow_col] == '^':
            return True
        else:
            return False
    return False