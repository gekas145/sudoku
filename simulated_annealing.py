import sys
import numpy as np


def main():

    def fill_plane():
        missing = [[x for x in range(1, 10) if x not in sudoku_plane[i]] for i in range(9)]
        for i in range(9):
            np.random.shuffle(missing[i])
        
        for i in range(9):
            missing_idxs = np.where(sudoku_plane[i] == 0)[0]
            sudoku_plane[i][missing_idxs] = missing[i]



    if len(sys.argv) == 1:
        sudoku_file = 'sudoku.txt'
    else:
        sudoku_file = sys.argv[1]

    with open(sudoku_file, 'r') as f:
        sudoku_plane =  f.readlines()
        f.close()
    
    sudoku_plane = [[int(line[i]) for i in range(9)] for line in sudoku_plane]

    sudoku_plane = np.array(sudoku_plane, dtype=np.int8)
    print(sudoku_plane[0])

    fill_plane()

    print(sudoku_plane[0])






if __name__ == '__main__':
    main()
