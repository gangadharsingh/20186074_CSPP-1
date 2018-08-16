'''
    Write a program to evaluate poker hands and determine the winner
    Read about poker hands here.
    https://en.wikipedia.org/wiki/List_of_poker_hands
'''
D_INP = {'A':14, 'K':13, 'Q':12, 'J':11, 'T':10, '9':9, '8':8, '7':7, '6':6,\
 '5':5, '4':4, '3':3, '2':2}

def is_fiveof_akind(hand):
    card_values = set(['--23456789TJQKA'.index(c) for c, s in hand])
    return len(card_values) == 1

def is_straight(hand):
    '''
        How do we find out if the given hand is a straight?
        The hand has a list of cards represented as strings.
        There are multiple ways of checking if the hand is a straight.
        Do we need both the characters in the string? No.
        The first character is good enough to determine a straight
        Think of an algorithm: given the card face value how to check if it a straight
        Write the code for it and return True if it is a straight else return False
    '''
    if all(True if c in "2345A" else False for c, s in hand):
        return True
    card_values = set(['--23456789TJQKA'.index(c) for c, s in hand])
    #"--" indicate 0,1: set is for no duplicate
    return len(card_values) == 5 and (max(card_values) - min(card_values) == 4)

def is_flush(hand):
    '''
        How do we find out if the given hand is a flush?
        The hand has a list of cards represented as strings.
        Do we need both the characters in the string? No.
        The second character is good enough to determine a flush
        Think of an algorithm: given the card suite how to check if it is a flush
        Write the code for it and return True if it is a flush else return False
    '''
    suit = hand[0]
    for i in hand:
        if suit[1] != i[1]:
            return False
    return True

def four_ofakind(hand):
    '''when four of same kind and one other of other rank
    '''
    list_em =[]
    list_chec = []
    cnt1 = 0
    cnt2 = 0
    for i in hand:
        list_em.append(i[0])
    card_values = set(['--23456789TJQKA'.index(c) for c, s in hand])
    list_chec = list(card_values)
    if len(list_chec) == 2:    
        cnt1 += list_em.count(str(list_chec[0]))
        cnt2 += list_em.count(str(list_chec[1]))
        return cnt1 == 4 or cnt2 == 4
    return False

def full_house(hand):
    list_em = []
    list_chec = []
    cnt1 = 0
    cnt2 = 0
    for i in hand:
        list_em.append(i[0])
    card_values = set(['--23456789TJQKA'.index(c) for c, s in hand])
    list_chec = list(card_values)
    if len(list_chec) == 2:    
        cnt1 += list_em.count(str(list_chec[0]))
        cnt2 += list_em.count(str(list_chec[1]))
        return cnt1 == 3 or cnt2 == 3
    return False
def three_ofakind(hand):
    '''when three of same kind and two of other of other rank
    '''
    list_em = []
    list_chec = []
    cnt1 = 0
    cnt2 = 0
    cnt3 = 0
    for i in hand:
        list_em.append(i[0])
    card_values = set(['--23456789TJQKA'.index(c) for c, s in hand])
    list_chec = list(card_values)
    if len(list_chec) == 3:    
        cnt1 += list_em.count(str(list_chec[0]))
        cnt2 += list_em.count(str(list_chec[1]))
        cnt3 += list_em.count(str(list_chec[2]))
        return cnt1 == 3 or cnt2 == 3 or cnt3 == 3
    return False

def twopair_ofakind(hand):
    '''when two of same kind and three other of other rank
    '''
    list_em = []
    list_chec = []
    cnt1 = 0
    cnt2 = 0
    cnt3 = 0
    for i in hand:
        list_em.append(i[0])
    card_values = set(['--23456789TJQKA'.index(c) for c, s in hand])
    list_chec = list(card_values)
    if len(list_chec) == 3:    
        cnt1 += list_em.count(str(list_chec[0]))
        cnt2 += list_em.count(str(list_chec[1]))
        cnt3 += list_em.count(str(list_chec[2]))
        return cnt1 == 2 or cnt2 == 2 or cnt3 == 2
    return False

def one_pair(hand):

    card_values = set(['--23456789TJQKA'.index(c) for c, s in hand])
    return len(card_values) == 4



def hand_rank(hand):
    '''
        You will code this function. The goal of the function is to
        return a value that max can use to identify the best hand.
        As this function is complex we will progressively develop it.
        The first version should identify if the given hand is a straight
        or a flush or a straight flush.
    '''


    # By now you should have seen the way a card is represented.
    # If you haven't then go the main or poker function and print the hands
    # Each card is coded as a 2 character string. Example Kind of Hearts is KH
    # First character for face value 2,3,4,5,6,7,8,9,T,J,Q,K,A
    # Second character for the suit S (Spade), H (Heart), D (Diamond), C (Clubs)
    # What would be the logic to determine if a hand is a straight or flush?
    # Let's not think about the logic in the hand_rank function
    # Instead break it down into two sub functions is_straight and is_flush

    # check for straight, flush and straight flush
    # best hand of these 3 would be a straight flush with the return value 3
    # the second best would be a flush with the return value 2
    # third would be a straight with the return value 1
    # any other hand would be the fourth best with the return value 0
    # max in poker function uses these return values to select the best hand
    cnt = 0
    if is_fiveof_akind(hand):
        cnt = 9
    elif is_straight(hand) and is_flush(hand):
        cnt = 8
    elif four_ofakind(hand):
        cnt = 7
    elif full_house(hand):
        cnt = 6
    elif is_flush(hand):
        cnt = 5
    elif is_straight(hand):
        cnt = 4
    elif three_ofakind(hand):
        cnt = 3
    elif twopair_ofakind(hand):
        cnt = 2
    elif one_pair(hand):
        cnt = 1
    else:
        cnt = 0
    return cnt

def poker(hands):
    '''
        This function is completed for you. Read it to learn the code.

        Input: List of 2 or more poker hands
               Each poker hand is represented as a list
               Print the hands to see the hand representation

        Output: Return the winning poker hand
    '''

        #hand_rank = hand_rank(hands[i])

    # the line below may be new to you
    # max function is provided by python library
    # learn how it works, in particular the key argument, from the link
    # https://www.programiz.com/python-programming/methods/built-in/max
    # hand_rank is a function passed to max
    # hand_rank takes a hand and returns its rank
    # max uses the rank returned by hand_rank and returns the best hand
    return max(hands, key=hand_rank)

if __name__ == "__main__":
    # read the number of test cases
    COUNT = int(input())
    # iterate through the test cases to set up hands list
    HANDS = []
    for x in range(COUNT):
        line = input()
        ha = line.split(" ")
        HANDS.append(ha)
    # test the poker function to see how it works
    print(' '.join(poker(HANDS)))