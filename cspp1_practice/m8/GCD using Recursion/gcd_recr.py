'''
# Exercise: GCDRecr
# Write a Python function, gcdRecur(a, b), that takes in two
numbers and returns the GCD(a,b) of given a and b.
# This function takes in two numbers and returns one number.
'''
def gcd_recur(a_inp, b_inp):
    '''
    a, b: positive integers
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    if a_inp == 0 or b_inp == 0:
        return 0
    elif a_inp % b_inp == 0:
        return b_inp
    elif b_inp % a_inp == 0:
        return a_inp
    elif a_inp > b_inp:
        return gcd_recur(a_inp, a_inp % b_inp)
    else:
        return gcd_recur(a_inp, b_inp % a_inp)

def main():
    '''To find gcd b recursion
    '''
    data = input()
    data = data.split()
    print(gcd_recur(int(data[0]), int(data[1])))

if __name__ == "__main__":
    main()
