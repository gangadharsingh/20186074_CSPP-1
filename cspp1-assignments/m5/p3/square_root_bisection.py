'''
# Write a python program to find the square root of the given number
# using approximation method
# testcase 1
# input: 25
# output: 4.999999999999998
# testcase 2
# input: 49
# output: 6.999999999999991
@author: gangadhar
'''
def main():
    '''
    # epsilon and step are initialized
    # don't change these values
    # your code starts here
    '''
    s_inp = int(input())
    inp_m = s_inp
    inp_l = 0.0
    epsilon = 0.01
    inp_a = (inp_l + inp_m)/2.0
    while abs(inp_a**2 - s_inp) >= epsilon:
        if inp_a**2 < s_inp:
            inp_l = inp_a
        else:
            inp_m = inp_a
        inp_a = (inp_l + inp_m)/2.0
    print(inp_a)
if __name__ == "__main__":
    main()
