'''
    Sudoku is a logic-based, combinatorial number-placement puzzle.
    The objective is to fill a 9×9 grid with digits so that
    each column, each row, and each of the nine 3×3 subgrids that compose the grid
    contains all of the digits from 1 to 9.

    Complete the check_sudoku function to check if the given grid
    satisfies all the sudoku rules given in the statement above.
'''

def check_sudoku(sudoku):
    '''
        Your solution goes here. You may add other helper functions as needed.
        The function has to return True for a valid sudoku grid and false otherwise
    '''
    for j in range(len(sudoku)):
        if sum([int(sudoku[j][i]) for i in range(0, len(sudoku))]) != 45:
            return 'False'
    sudoku_transpose = transpose_matrix(sudoku)
    for j in range(len(sudoku_transpose)):
        if sum([int(sudoku_transpose[j][i]) for i in range(0, len(sudoku_transpose))]) != 45:
            return 'False'
    return 'True'
def transpose_matrix(sudoku):
    tran_mat = [[sudoku[j][i] for j in range(len(sudoku))] for i in range(len(sudoku[0]))]
    trans_new = []
    for trans in tran_mat:
        trans_new.append(trans)
    return trans_new
def main():
    '''
        main function to read input sudoku from console
        call check_sudoku function and print the result to console
    '''
    
    # initialize empty list
    sudoku = []

    # loop to read 9 lines of input from console
    for i in range(9):
        # read a line, split it on SPACE and append row to list
        row = input().split(' ')
        sudoku.append(row)
    # call solution function and print result to console
    print(check_sudoku(sudoku))

if __name__ == '__main__':
    main()