'''
# Exercise: PowerRecr
# Write a Python function, recurPower(base, exp),
that takes in two numbers and returns the base^(exp) of given base and exp.
# This function takes in two numbers and returns one number.
@author: gangadharsingh
'''
def recur_power(base, exp):
    '''
    base: int or float.
    exp: int >= 0
    returns: int or float, base^exp
    '''
    # Your code here
    if exp == 0:
        return 1
    return recur_power(base, exp-1) * base
def main():
    '''This will take input.
    '''
    data = input()
    data = data.split()
    print(recur_power(float(data[0]), int(data[1])))

if __name__ == "__main__":
    main()
