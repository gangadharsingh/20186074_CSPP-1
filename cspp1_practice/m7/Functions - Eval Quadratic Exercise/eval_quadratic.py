'''
# Exercise: eval quadratic
# Write a Python function, evalQuadratic(a, b, c, x),
that returns the value of the quadratic a . x 2 + b . x + c
# This function takes in four numbers and returns a single number.
@author: gangadharsingh
'''
def eval_quadratic(a_inp, b_inp, c_inp, x_inp):
    '''quadratic equation function
    '''
    return a_inp*(x_inp**2) + b_inp*x_inp + c_inp
def main():
    '''# (a(x**2) + b*x + c)
    '''
    data = input()
    data = data.split(' ')
    data = list(map(float, data))
    for x_inp in range(len(data)):
        temp = str(data[x_inp]).split('.')
        if temp[1] == '0':
            data[x_inp] = int(float(str(data[x_inp])))
        else:
            data[x_inp] = data[x_inp]
    print(eval_quadratic(data[0], data[1], data[2], data[3]))

if __name__ == "__main__":
    main()
