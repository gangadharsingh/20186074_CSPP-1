'''
# Exercise: Assignment-2
# Write a Python function, sumofdigits, that takes
in one number and returns the sum of digits of given number.
# This function takes in one number and returns one number.
@author: gangadharsingh
'''

def sumof_digits(num_inp):
    '''
    n is positive Integer

    returns: a positive integer, the sum of digits of n.
    '''
    # Your code here
    if num_inp >= 1:
        return num_inp % 10 + sumof_digits(num_inp // 10)
    return n 

def main():
    '''sum of digits of given number
    '''
    inp_a = input()
    print(sumof_digits(int(inp_a)))

if __name__ == "__main__":
    main()

