import sys, argparse
import numpy as np
from copy import deepcopy


def main():
    global sudoku_file, temp, temp_decrease_rate, max_iterations

    parser = argparse.ArgumentParser()
    parser.add_argument('--f', type=str, default='sudoku.txt', help='File with sudoku puzzle')
    parser.add_argument('--t', type=float, default=0.5, help='Initial temperature')
    parser.add_argument('--tdr', type=float, default=0.99999, help='Temperature decrease rate')
    parser.add_argument('--maxiter', type=int, default=40000, help='Max number of iterations')
    args = parser.parse_args()

    sudoku_file = args.f
    temp = args.t
    temp_decrease_rate = args.tdr
    max_iterations = args.maxiter

    squares = []
    for i in range(3):
        for j in range(3):
            squares.append((3*i, 3*j))

    def fill_plane(plane):
        missing = [[x for x in range(1, 10) if x not in plane[i]] for i in range(9)]
        for i in range(9):
            np.random.shuffle(missing[i])
            plane[i][missing_idxs[i]] = missing[i]
        return plane


    def count_unique(arr):
        return np.unique(arr).shape[0]
    
    def evaluate(plane):
        score = 162 # 9**2 + 9**2
        score -= np.sum([count_unique(plane[b[0]:b[0]+3, 
                                            b[1]:b[1]+3]) for b in squares])
        
        score -= np.sum([count_unique(plane[:,j]) for j in range(9)])
        
        return score

    def mutate(plane):
        row_num = np.random.randint(0, 9)
        while len(missing_idxs[row_num]) <= 1:
            row_num = np.random.randint(0, 9)

        i, j = np.random.choice(len(missing_idxs[row_num]), size=2, replace=False)
        i, j = missing_idxs[row_num][i], missing_idxs[row_num][j]
        plane[row_num][i], plane[row_num][j] = plane[row_num][j], plane[row_num][i]

        return plane

    def solve(plane):
        global temp

        current_solution = fill_plane(deepcopy(plane))
        current_score = evaluate(current_solution)
        best_solution = deepcopy(current_solution)
        best_score = current_score
        solution_found = False

        for i in range(max_iterations+1):

            if i % 1000 == 0:
                print(f'[Iteration {i}] current score: {current_score}, best score: {best_score}')

            proposal = mutate(deepcopy(current_solution))
            score = evaluate(proposal)
            x = np.random.uniform(0, 1)
            if x < np.exp((current_score - score)/temp):
                current_solution = deepcopy(proposal)
                current_score = score
            
            if current_score < best_score:
                best_score = current_score
                best_solution = deepcopy(current_solution)
            
            if best_score == 0:
                print('Solution found!')
                print(best_solution)
                solution_found = True
                break
            
            temp *= temp_decrease_rate
        
        if not solution_found:
            print('Did not converge :(, please try again')

    with open(sudoku_file, 'r') as f:
        sudoku_plane =  f.readlines()
        f.close()
    
    sudoku_plane = [[int(line[i]) for i in range(9)] for line in sudoku_plane]

    sudoku_plane = np.array(sudoku_plane, dtype=np.int8)

    missing_idxs = [np.ndarray.tolist(np.where(sudoku_plane[i] == 0)[0]) for i in range(9)]


    solve(sudoku_plane)


if __name__ == '__main__':
    main()
