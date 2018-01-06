# Character Picture Grid
# Simplified ver 1

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

def rotated_list(the_list):
    # loops as many times as long is the inner list
    for i in range(len(the_list[0])):
        # loops as many times as many inner list contains main list
        for j in range(len(the_list)):
            print(the_list[j][i], end = '')
        print("")

rotated_list(grid)

    
