'''
Write a python program to read multiple lines of text input and store the input into a string.
'''

def main():
    '''read string
    '''
    num = int(input())
    str_emp = []
    for i in range(num):
        str_emp.append(input())
    for j in str_emp:
        print(j)

if __name__ == '__main__':
    main()
