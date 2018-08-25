'''
Write a function to clean up a given string by removing the special characters and retain 
alphabets in both upper and lower case and numbers.
'''
import re
def clean_string(string):
	str_new = re.sub('[^a-zA-Z]','', string)
	return str_new
def main():
    string = input()
    print(clean_string(string))

if __name__ == '__main__':
    main()
