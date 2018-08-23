'''Matrix addition and multiplication
'''
def mult_matrix(mat_1, mat_2):
    '''
        check if the matrix1 columns = matrix2 rows
        mult the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for mult
        and return None
        error message should be "Error: Matrix shapes invalid for mult"
    '''
    multi_mat = []
    if len(mat_1[0]) != len(mat_2):
        print("Error: Matrix shapes invalid for mult")
        return None
    row_m = []
    mat_mul = []
    for i in range(len(mat_1)):
        for j in range(len(mat_2[0])):
            sums = 0
            for k in range(len(mat_2)):
                sums += mat_1[i][k]*mat_2[k][j]
            row_m.append(sums)
        mat_mul.append(row_m)
        row_m = []
    return mat_mul

def add_matrix(mat_1, mat_2):
    '''
        check if the matrix shapes are similar
        add the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for addition
        and return None
        error message should be "Error: Matrix shapes invalid for addition"
    '''
    sum_m = []
    if len(mat_1) == len(mat_2) and len(mat_1[0]) == len(mat_2[0]):
        for i in range(len(mat_1)):
            for j in range(len(mat_1[i])):
                sum_m.append(mat_1[i][j] + mat_2[i][j])
        return [sum_m[cnt:cnt+len(mat_1[0])] for cnt in range(0, len(sum_m), len(mat_1[0]))]
    else:
        print("Error: Matrix shapes invalid for addition")
        return None

def read_matrix():
    '''
        read the matrix dimensions from input
        create a list of lists and read the numbers into it
        in case there are not enough numbers given in the input
        print an error message and return None
        error message should be "Error: Invalid input for the matrix"
    '''
    mat = []
    list_inp = input().split(',')
    r, c = int(list_inp[0]), int(list_inp[1])
    for i in range(r):
        l_mat_r = input().split(' ')
        if c == len(l_mat_r):
            mat.append([int(i) for i in l_mat_r])
        else:
            print("Error: Invalid input for the matrix")
            return 0
    return mat

def main():
    # read matrix 1
    mat_one = read_matrix()
    # read matrix 2
    mat_two = read_matrix()
    if mat_one != 0 and mat_two != 0:
        print(add_matrix(mat_one, mat_two))
        print(mult_matrix(mat_one, mat_two))
    else:
        None
    # add matrix 1 and matrix 2
    # multiply matrix 1 and matrix 2
if __name__ == '__main__':
    main()
