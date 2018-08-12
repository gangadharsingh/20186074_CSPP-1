#Exercise: Assignment-4
#We are now ready to begin writing the code that interacts with the player.
'''We'll be implementing the playHand function. This function allows the user to play out
a single hand. First, though, you'll need to implement the helper calculateHandlen function,
which can be done in under five lines of code.
@author: gangadharsingh
'''

def calculate_hand_len(hand):
    """
    Returns the length (number of letters) in the current hand.
    hand: dictionary (string int)
    returns: integer
    """
    cnt = 0
    for i in hand:
        cnt += hand[i]
    return cnt

def main():
    '''main function
    '''
    n_inp = input()
    adict = {}
    for data in range(int(n_inp)):
        data = input()
        l_inp = data.split()
        adict[l_inp[0]] = int(l_inp[1])
    print(calculate_hand_len(adict))

if __name__ == "__main__":
    main()
