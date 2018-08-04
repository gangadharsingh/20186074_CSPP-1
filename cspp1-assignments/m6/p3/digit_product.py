'''
@author: gangadharsingh
Given a  number int_input, find the product of all the digits
example: 
    input: 123
    output: 6
'''
def main():
    '''
    Read any number from the input, store it in variable int_input.
    '''
    int_input = str(input())
    prod_op = 1
    int_inp = 0
    prod_neg = 1
    if int(int_input) <0:
        int_inp = -int(int_input)
        for j in str(int_inp):
            prod_neg = int(j)*prod_neg
    else:
        for i in int_input:
            prod_op = int(i)*prod_op
    if int(int_input) < 0:
        print("-",prod_neg)
    else:
        print(prod_op)

if __name__ == "__main__":
    main()
