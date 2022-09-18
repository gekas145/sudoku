import sys
import numpy as np
import itertools as it

def main():

    bytes = ((0, 0), (0, 1), (1, 0), (1, 1))

    def fill_plane():
        missing = [[x for x in range(1, 10) if x not in sudoku_plane[i]] for i in range(9)]
        for i in range(9):
            np.random.shuffle(missing[i])
        
        for i in range(9):
            missing_idxs = np.where(sudoku_plane[i] == 0)[0]
            sudoku_plane[i][missing_idxs] = missing[i]

    def count_unique(arr):
        return len(np.unique(arr))
    
    def evaluate(plane):
        score = 162 # 9**2 + 9**2
        score -= np.sum([count_unique(plane[3*b[0]:3*b[0]+3,
                                            3*b[1]:3*b[1]+3]) for b in bytes])
        
        score -= np.sum([count_unique(plane[:,j]) for j in range(9)])
        
        return score

    
    if len(sys.argv) == 1:
        sudoku_file = 'sudoku.txt'
    else:
        sudoku_file = sys.argv[1]

    with open(sudoku_file, 'r') as f:
        sudoku_plane =  f.readlines()
        f.close()
    
    sudoku_plane = [[int(line[i]) for i in range(9)] for line in sudoku_plane]

    sudoku_plane = np.array(sudoku_plane, dtype=np.int8)

    fill_plane()

    print(evaluate(sudoku_plane))

    print(sudoku_plane)



if __name__ == '__main__':
    main()
