'''
Write a function to print a dictionary with the keys in sorted order along with the
frequency of each word. Display the frequency values using “#” as a text based graph
'''

def frequency_graph(dictionary):
    '''printing ## number of times the value of dictionary
    '''
    for i in sorted(dictionary):
        print('%s - %s' % (i, dictionary[i]*'#'))

def main():
    '''Printing values # instead of ditionary values
    '''
    dictionary = eval(input())
    frequency_graph(dictionary)

if __name__ == '__main__':
    main()
