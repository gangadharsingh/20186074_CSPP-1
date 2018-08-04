'''
Given a  number int_input, find the product of all the digits
example: 
	input: 123
	output: 6
'''
def main():
    '''
    Read any number from the input, store it in variable int_input.
    '''
    int_input = str(123)#int(input())
    
    prod_op = 1
    
    for i in int_input:
    	prod_op = int(i)*prod_op
    print(prod_op)

if __name__ == "__main__":
    main()
