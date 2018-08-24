'''checking validation and then who wins the game
'''
def main():
    '''tic tac toe game
    '''
    #making tictactoe
    empt_tic = empt_tictactoe()
    #checking input is valid or not
    if inp_validation(empt_tic) == True:
        print(win_tictactoe(empt_tic))
    else:
        print(inp_validation(empt_tic))

def empt_tictactoe():
    '''creating empty tic tac toe
    '''
    tic_tactoe = []
    for _ in range(3):
        list_temp = input().split()
        tic_tactoe.append(list_temp)
    return tic_tactoe
    #either x or y count should not be greater than 5

def inp_validation(tic_tactoe):
    '''checking whether tic tac toe is valid or not
    '''
    if sum(i.count('x') for i in tic_tactoe) > 5 or sum(i.count('o') for i in tic_tactoe) > 5:
        return "invalid game"
    for i in range(len(tic_tactoe)):
        for j in tic_tactoe[i]:
            if j not in 'xo.':
                return "invalid input"
    return True

def win_tictactoe(tic_tactoe):
    '''checking wining team
    '''
    c_x = sum([i.count('x') for i in tic_tactoe])
    c_o = sum([i.count('o') for i in tic_tactoe])
    if c_x == 3 and c_o == 3:
        return 'invalid game'
    elif c_x == 3:
        return 'x'
    elif c_o == 3:
        return 'o'
    elif tic_tactoe[0][0] == tic_tactoe[1][1] == tic_tactoe[2][2]:
        return tic_tactoe[0][0]
    elif tic_tactoe[0][2] == tic_tactoe[1][1] == tic_tactoe[2][0]:
        return tic_tactoe[0][2]
    if c_x+c_o == 9:
        return 'draw'
main()
