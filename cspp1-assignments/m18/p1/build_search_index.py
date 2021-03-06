'''
    Tiny Search Engine - Part 1 - Build a search index

    In this programming assingment you are given with some text documents as input.
    Complete the program below to build a search index. Don't worry, it is explained below.
    A search index is a python dictionary.
    The keys of this dictionary are words contained in ALL the input text documents.
    The values are a list of documents such that the key/word appears in each document atleast once.
    The document in the list is represented as a tuple.
    The tuple has 2 items. The first item is the document ID.
    Document ID is represented by the list index.
    For example: the document ID of the third document in the list is 2
    The second item of the tuple is the frequency of the word occuring in the document.

    Here is the sample format of the dictionary.
    {
        word1: [(doc_id, frequency),(doc_id, frequency),...],
        word2: [(doc_id, frequency),(doc_id, frequency),...],
        .
        .
    }
'''
import re

# helper function to load the stop words from a file
def load_stopwords(filename):
    '''
        loads stop words from a file and returns a dictionary
    '''
    stopwords = {}
    with open(filename, 'r') as filename1:
        for line in filename1:
            stopwords[line.strip()] = 0
    return stopwords

def word_list(text):
    '''
        Change case to lower and split the words using a SPACE
        Clean up the text by remvoing all the non alphabet characters
        return a list of words
    '''
    # words = inp_1.lower().strip().replace('\'', '')
    words = re.sub('[^a-z]', " ", text.lower().replace('\'' '')).split()
    # words = regex.sub(" ", words).split(" ")
    stopwords = (load_stopwords("stopwords.txt"))
    words = [word.strip() for word in words not in stopwords and len(word) > 0]
    return words
def build_search_index(docs):
    '''
        Process the docs step by step as given below
    '''
    search_index = {}
    # initialize a search index (an empty dictionary)
    for doc_id, doc in enumerate(docs):
    # iterate through all the docs
    # keep track of doc_id which is the list index corresponding the document
    # hint: use enumerate to obtain the list index in the for loop
        word_doc_list = word_list(doc)
        # clean up doc and tokenize to words list
        for word in word_doc_list:
            if word not in search_index:
                search_index[word] = []
                search_index[word].append((doc_id, word_doc_list.count(word)))
            else:
                if (doc_id, word_doc_list.count(word) not in search_index[word]):
                    search_index[word].append((doc_id, word_doc_list.count(word)))   

        # add or update the words of the doc to the search index
    return search_index
    # return search index

# helper function to print the search index
# use this to verify how the search index looks
def print_search_index(index):
    '''
        print the search index
    '''
    dict_prnt = {}
    keys = sorted(index.keys())
    for key in keys:
        print(key, " - ", index[key])

# main function that loads the docs from files
def main():
    '''
        main function
    '''
    # empty document list
    documents = []
    # iterate for n times
    lines = int(input())
    # iterate through N times and add documents to the list
    for i in range(lines):
        documents.append(input())
        i += 1

    # call print to display the search index
    print_search_index(build_search_index(documents))

if __name__ == '__main__':
    main()
