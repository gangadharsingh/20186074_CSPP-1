'''
# Exercise: GCDIter
# Write a Python function, gcdIter(a, b), that takes in two numbers
and returns the GCD(a,b) of given a and b.
# This function takes in two numbers and returns one number.
@author: gangadharsingh
'''

def gcd_iter(a_inp, b_inp):
    '''
    a, b: positive integers
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    while b_inp != 0:
        rem = a_inp % b_inp
        a_inp = b_inp
        b_inp = rem
    return a_inp
def main():
    '''input: int value
       output: gcd value
    '''
    data = input()
    data = data.split()
    print(gcd_iter(int(data[0]), int(data[1])))

if __name__ == "__main__":
    main()
