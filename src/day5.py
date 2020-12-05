def codeToId(code):
    row = code[:7] # F/B
    col = code[7:] # L/R

    row_range = [0, 127]
    col_range = [0, 7]

    for val in row:
        mid_row = (row_range[1] - row_range[0] + 1)//2
        if val == 'B':
            row_range[0] += mid_row
        else:
            row_range[1] -= mid_row
    
    for val in col:
        mid_col = (col_range[1] - col_range[0] + 1)//2
        if val == 'R':
            col_range[0] += mid_col
        else:
            col_range[1] -= mid_col
    
    return row_range[0]*8 + col_range[0]

seat_codes = open('input/day5', 'r').readlines()
seat_ids = [codeToId(x) for x in seat_codes]
ids_set = set(seat_ids)

max_seat_id = 127 * 8 + 7

for i in range(max_seat_id):
    if i+1 in ids_set and i-1 in ids_set and i not in ids_set:
        print(i)