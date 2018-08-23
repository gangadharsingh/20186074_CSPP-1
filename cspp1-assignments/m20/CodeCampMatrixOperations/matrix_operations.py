'''Matrix addition and multiplication
'''
def mult_matrix(m1, m2):
    '''
        check if the matrix1 columns = matrix2 rows
        mult the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for mult
        and return None
        error message should be "Error: Matrix shapes invalid for mult"
    '''
    multi_mat = []
    if len(m1[0]) != len(m2):
        print("Error: Matrix shapes invalid for mult")
        return None
    else:
        r = []
        m = []
        for i in range(len(m1)):
            for j in range(len(m2[0])):
                sums= 0
                for k in range(len(m2)):
                    sums += m1[i][k]*m2[k][j]
                r.append(sums)
            m.append(r)
            r = []
        return m
    
def add_matrix(m1, m2):
    '''
        check if the matrix shapes are similar
        add the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for addition
        and return None
        error message should be "Error: Matrix shapes invalid for addition"
    '''
    sum_m = []
    if len(m1) == len(m2) and len(m1[0]) == len(m2[0]):
        for i in range(len(m1)):
            for j in range(len(m1[i])):
                sum_m.append(m1[i][j] + m2[i][j])
        return [sum_m[cnt:cnt+len(m1[0])] for cnt in range(0, len(sum_m), len(m1[0]))]
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
    list_inp= input().split(',')
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
