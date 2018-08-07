'''
# Exercise: PowerIter
# Write a Python function, iterPower(base, exp), that takes in two
numbers and returns the base^(exp) of given base and exp.
# This function takes in two numbers and returns one number.
@author: gangadharsingh
'''
def iter_power(base, exp):
    '''
    base: int or float.
    exp: int >= 0
    returns: int or float, base^exp
    '''
    # Your code here
    return base ** exp

def main():
    '''main function starts here
    '''
    data = input()
    data = data.split()
    print(iter_power(float(data[0]), int(data[1])))

if __name__ == "__main__":
    main()
