def mult_matrix(m1, m2):
    '''
        check if the matrix1 columns = matrix2 rows
        mult the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for mult
        and return None
        error message should be "Error: Matrix shapes invalid for mult"
    '''
    # mul = []
    # if len(m1[0]) == len(m2):
    #     for i in range(len(m1)):
    #         mul.append(sum(m1[i][j]*m2[j][i] for j in range(len(m2[0]))))
    #     return mul
    # else:
    #     print("Error: Matrix shapes invalid for mult")
    #     return None
    # row = len(m1[0])
    # col = len(m2)
    # multi_mat = gnerate_mat(row, col)
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
    # return multi_mat

def gnerate_mat(row, col):
    add_matrix = [[]*col]*row 
    return add_matrix
    
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
    # row = len(m1)
    # col = len(m1[0])
    # add_matrix = gnerate_mat(row, col)
    # sum_mat = []
    # add_matrix.append([(m1[i][j])+(m2[i][j]) for j in range(col) for i in range(row)])
    # return add_matrix

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
    # mat = []
    # for i in range(num):
    #     mat.append(input().split(' '))
    # mat_n = []
    # for j in range(len(mat)):
    #     mat_n.append([int(i) for i in mat[j]])
    # return mat_n

def main():
    # read matrix 1
    mat_one = read_matrix()
    # size = input().split(',')
    # mat_1 = read_matrix(int(size[0]))
    # read matrix 2
    mat_two = read_matrix()
    #print(mat_one,mat_two)
    if mat_one != 0 and mat_two != 0:
        print(add_matrix(mat_one, mat_two))
        print(mult_matrix(mat_one, mat_two))
    else:
        None
    # size1 = input().split(',')
    # mat_2 = read_matrix(int(size1[0]))
    # add matrix 1 and matrix 2
    # if size == size1:
    #print(add_matrix(mat_one, mat_two))
    # multiply matrix 1 and matrix 2
    #print(mult_matrix(mat_one, mat_two))

if __name__ == '__main__':
    main()
