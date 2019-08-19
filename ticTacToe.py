theBoard = {
    'top-L':' ','top-M':' ','top-R':' ',
    'mid-L':' ','mid-M':' ','mid-R':' ',
    'low-L':' ','low-M':' ','low-R':' '
}
def printBoard(board):
    print(board['top-L'] + '|' + board['top-M']+'|'+board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
turn = 'X'
for i in range(9):
    printBoard(theBoard)
    print("Turn for "+turn+'.Move on which space?')
    move = input()
    if theBoard[move]==' ':
        theBoard[move]= turn
    else:
        print('please chose the blank space and input again')
        move = input()
        theBoard[move] = turn
    if turn=='X':
        turn='O'
    else:
        turn='X'
    if theBoard['top-L']==theBoard['top-M']==theBoard['top-R']!=' '\
            or theBoard['mid-L']==theBoard['mid-M']==theBoard['mid-R']!=' '\
            or theBoard['low-L']==theBoard['low-M']==theBoard['low-R']!=' '\
            or theBoard['top-L']==theBoard['mid-L']==theBoard['low-L']!=' '\
            or theBoard['top-M'] == theBoard['mid-M'] == theBoard['low-M']!=' '\
            or theBoard['top-R'] == theBoard['mid-R'] == theBoard['low-R']!=' '\
            or theBoard['top-L'] == theBoard['mid-M'] == theBoard['low-R']!=' '\
            or theBoard['top-R'] == theBoard['mid-M'] == theBoard['low-L']!=' ':

        print('win')
        break
printBoard(theBoard)