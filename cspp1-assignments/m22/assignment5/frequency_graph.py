'''
Write a function to print a dictionary with the keys in sorted order along with the
frequency of each word. Display the frequency values using “#” as a text based graph
'''

def frequency_graph(dictionary):
	str_temp = ''
    for i in sorted(dictionary):
        str_temp += '%s - %s' % (i, dictionary[i])
    print(str_temp)

def main():
    dictionary = eval(input())
    frequency_graph(dictionary)

if __name__ == '__main__':
    main()
