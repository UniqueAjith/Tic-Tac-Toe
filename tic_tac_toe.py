the_board = {'1': ' ', '2': ' ', '3': ' ',
             '4': ' ', '5': ' ', '6': ' ',
             '7': ' ', '8': ' ', '9': ' '}

reset = []
for i in the_board:
    reset.append(i)

def printBoard(the_board):
    print(the_board['1'] + '|' + the_board['2'] + '|' + the_board['3'])
    print('-+-+-')
    print(the_board['4'] + '|' + the_board['5'] + '|' + the_board['6'])
    print('-+-+-')
    print(the_board['7'] + '|' + the_board['8'] + '|' + the_board['9'])

def play():
    turn = 'X'
    count = 0
    for i in range(9):
        printBoard(the_board)
        print('Turn for ' + turn + '. Move on which place?')
        move = input()
        
        if the_board[move] == ' ':
            the_board[move] = turn
            count += 1
        else:
            print('Place already occupied!')
             
        if count >= 4:
            if the_board['1']==the_board['2']==the_board['3']!=' ':
                printBoard(the_board)
                print(turn + ' wins!')
                break
            elif the_board['4']==the_board['5']==the_board['6'] != ' ':
                printBoard(the_board)
                print(turn + ' wins!')
                break
            elif the_board['7']==the_board['8']==the_board['9'] != ' ':
                printBoard(the_board)
                print(turn + ' wins!')
                break
            elif the_board['1']==the_board['4']==the_board['7'] != ' ':
                printBoard(the_board)
                print(turn + ' wins!')
                break
            elif the_board['2']==the_board['5']==the_board['8'] != ' ':
                printBoard(the_board)
                print(turn + ' wins!')
                break
            elif the_board['3']==the_board['6']==the_board['9'] != ' ':
                printBoard(the_board)
                print(turn + ' wins!')
                break
            elif the_board['1']==the_board['5']==the_board['9'] != ' ':
                printBoard(the_board)
                print(turn + ' wins!')
                break
            elif the_board['3']==the_board['5']==the_board['7'] != ' ':
                printBoard(the_board)
                print(turn + ' wins!')
                break
            else:
                printBoard(the_board)
                print('Match Draw!')
                
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'
            
    again = input('Do you want to play again? (y/n)')
    if again == 'y' or again == 'Y':
        for i in reset:
            the_board[i] = " "
        play()
    elif again == 'n' or again == 'N':
        print('Thank you for playing!')  
    else:
        print('Invalid input!')
        
if __name__ == '__main__':
    print('Welcome to Tic Tac Toe!')
    play()