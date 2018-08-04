'''
# Write a python program to find if the given number is\
a perfect cube or not
# using guess and check algorithm
# testcase 1
# Input: 24389
# Output: 24389 is a perfect cube
# testcase 2
# Input: 21950
# Output: 21950 is not a perfect cube
@author: gangadharsingh
'''
def main():
    # input is captured in s
    # watch out for the data type of value stored in s
    # your code starts here
    s = int(input())
    inp = 0
    guess = 1
    for i in range(s):
        if(i**3 == s):
            guess =i
            inp =1
    if (inp == 1):
        print(s,"is a perfect cube")
    else:
        print(s,"is not a perfect cube")


if __name__ == "__main__":
    main()
