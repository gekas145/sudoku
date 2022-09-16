import numpy as np
import sys

def main():
    def validate_row(i, x):
        return ~np.isin(x, sudoku_plane[i])

    def validate_column(j, x): 
        return ~np.isin(x, sudoku_plane[:,j])

    def get_square_start(pos):
        return 3*(pos[0]//3), 3*(pos[1]//3)

    def validate_square(pos, x):
        square_start = get_square_start(pos)
        return ~np.isin(x, sudoku_plane[square_start[0]:square_start[0]+3, 
                                        square_start[1]:square_start[1]+3])

    def validate(pos, k):
        return validate_column(pos[1], k) and validate_row(pos[0], k) and validate_square(pos, k)

    def solve():
        empty = np.where(np.isnan(sudoku_plane))
        if len(empty[0]) == 0:
            print(sudoku_plane)
            return
        for i in empty[0]:
            for j in empty[1]:
                if np.isnan(sudoku_plane[i][j]):
                    inserted = False
                    for k in range(1, 10):
                        if validate([i, j], k):
                            inserted = True
                            sudoku_plane[i][j] = k
                            solve()
                            sudoku_plane[i][j] = np.nan
                    if ~inserted:
                        return
    
    if len(sys.argv) == 1:
        sudoku_file = 'sudoku.txt'
    else:
        sudoku_file = sys.argv[1]

    with open(sudoku_file, 'r') as f:
        sudoku_plane =  f.readlines()
        f.close()
    
    sudoku_plane = [[int(line[i]) for i in range(9)] for line in sudoku_plane]

    sudoku_plane = np.array(sudoku_plane, dtype=np.float16)
    sudoku_plane[sudoku_plane == 0] = np.nan

    print(sudoku_plane)

    solve()


if __name__ == '__main__':
    main()

