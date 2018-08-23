def mult_matrix(m1, m2):
    '''
        check if the matrix1 columns = matrix2 rows
        mult the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for mult
        and return None
        error message should be "Error: Matrix shapes invalid for mult"
    '''
    pass

def add_matrix(m1, m2):
    '''
        check if the matrix shapes are similar
        add the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for addition
        and return None
        error message should be "Error: Matrix shapes invalid for addition"
    '''



def read_matrix(num):
    '''
        read the matrix dimensions from input
        create a list of lists and read the numbers into it
        in case there are not enough numbers given in the input
        print an error message and return None
        error message should be "Error: Invalid input for the matrix"
    '''
    mat = []
    for j in range(len(num)+1,2):
        for i in range(len(num[j])):
            list_mat = input().split(' ')
            mat.append(list_mat)
    mat_n = []
    for j in range(len(mat)):
        mat_n.append([int(i) for x in mat[j]])
    return mat_n

def main():
    # read matrix 1
    size_1 = input()
    mat_1 = read_matrix(size_1)
    print(mat_1)
    # read matrix 2
    size_2 = input()
    mat_2 = read_matrix(size_2)
    print(mat_2)
    # add matrix 1 and matrix 2

    # multiply matrix 1 and matrix 2
    pass

if __name__ == '__main__':
    main()
