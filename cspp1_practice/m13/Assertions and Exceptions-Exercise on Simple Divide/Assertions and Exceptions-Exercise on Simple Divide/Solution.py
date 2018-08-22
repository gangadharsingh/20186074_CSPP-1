#define the simple_divide function here
def simple_divide(item, denom):
    # start a try-except block
   	try:
   		div = item / denom
   	except ZeroDivisionError:
   		return 0
   	else:
   		return div

def fancy_divide(list_of_numbers, index):
    den = list_of_numbers[index]
    return [simple_divide(i) for i in list_of_numbers]

def main():
	data = input()
	l=data.split()
	l1=[]
	for j in l:
		l1.append(float(j))
	s=input()
	index=int(s)
	print(fancy_divide(l1,index))
	

if __name__== "__main__":
	main()
