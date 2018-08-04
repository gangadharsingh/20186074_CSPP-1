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
	s_inp = int(input())
	step_inp = 0.1
	epsilon = 0.01
	gues_a = 0
	flag = 1
	if flag == 1:
		while abs(gues_a**2 - s_inp) > epsilon:
			if gues_a < s_inp:
				gues_a += step_inp
			else:
				flag =0
	if abs(gues_a**2 - s_inp) < epsilon:
		print(str(gues_a))
	else:
		print("failed")

	

if __name__== "__main__":
	main()
