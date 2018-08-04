'''
# Write a python program to find the square root of the given number
# using approximation method
@author: gangadharsingh
# testcase 1
# input: 25
# output: 4.999999999999998

# testcase 2
# input: 49
# output: 6.999999999999991
'''
def main():
	'''
	# epsilon and step are initialized
	# don't change these values
	# your code starts here
	'''
	s_inp = input()
	epsilon = 0.01
	guess_a = s_inp/2.0
	guess_b = 0
	while abs(guess_a*guess_a - s_inp) >= epsilon:
		guess_a =guess_a - (((guess_a**2) - s_inp)/(2*guess_a))
	print(str(guess_a))


if __name__== "__main__":
	main()
