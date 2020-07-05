

# a3.py

# How to play it: place your X or O on a empty tile`
# Legal moves: any empty tile
# Win: you reach 3 in a row before they do
# Loss: they reach 3 in a row before you do
# Draw: none of you reach 3 in a row when all 9 tiles is filled

# 1) make a list of legal moves
# 2) for each moves in moveList
#   do x number of random play out

# 3) choose the move that result in the greatet number of win

# Random play out:
#   play the game by choosing random moves
#   play till it wins, lose or draw
#   record the result

import random


class ticTacToe:
    def __init__(self):
        self.activePlayer = 1
        self.gameBoard = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.AI = 1

    # game board index
    # 0 1 2
    # 3 4 5
    # 6 7 8

    def getAI(self):
        return self.AI

    def setAI(self, order):
        self.AI = order
        return self.AI

    def copyGameState(self):
        copyGame = ticTacToe()
        copyGame.activePlayer = self.activePlayer
        copyGame.gameBoard = self.gameBoard[:]
        copyGame.AI = self.AI
        return copyGame

    def getGameBoard(self):
        return self.gameBoard

    def currentPlayer(self):
        return self.activePlayer

    def switchPlayer(self):
        if (self.activePlayer == 2):
            self.activePlayer = 1
        else:
            self.activePlayer = 2
        return self.activePlayer

    def doMove(self, index, player):
        self.gameBoard[index] = player
        return self.gameBoard

    # Game ends when someone wins (in which there is gonna be left over 0, or there is no more 0)
    # so you should first check if smoeone win the game first

    def inGame(self):
        if self.winLoseDraw() == -1:
            return True
        return False

    # if there's 0 on numArr, return False, else return True
    def zeroCheck(self, numArr):
        for x in numArr:
            if self.gameBoard[x] == 0:
                return False
        return True

    def winLoseDraw(self):
        # return -1 if not finished yet
        # return 0 if draw
        # return 1 if player 1 wins
        # return 2 if player 2 wins

        winState = [[0,3,6], [1,4,7], [2,5,8], [0,1,2], [3,4,5], [6,7,8], [0,4,8], [2,4,6]]
        for i in range(8):
            if self.gameBoard[winState[i][0]] == self.gameBoard[winState[i][1]] and self.gameBoard[winState[i][0]] == self.gameBoard[winState[i][2]] and self.zeroCheck(winState[i]):
                if self.gameBoard[winState[i][0]] == 1:
                    return 1
                elif self.gameBoard[winState[i][0]] == 2:
                    return 2
        if 0 not in self.gameBoard:
            return 0
        return -1

    def display(self):
        # display init
        display = ['_ ', '_ ', '_ ', '_ ', '_ ', '_ ', '_ ', '_ ', '_ ']
        displayString = ''
        for i in range(9):
            if self.gameBoard[i] == 1:
                display[i] = 'X '
            if self.gameBoard[i] == 2:
                display[i] = 'O '
            if i == 2 or i == 5:
                displayString += (display[i] + '\n')
            else:
                displayString += display[i]

        print(displayString)

    
    def displayEndGame(self):
        display = ['_ ', '_ ', '_ ', '_ ', '_ ', '_ ', '_ ', '_ ', '_ ']
        displayString = ''
        for i in range(9):
            if self.gameBoard[i] == 1:
                display[i] = 'X '
            if self.gameBoard[i] == 2:
                display[i] = 'O '
            if i == 2 or i == 5:
                displayString += (display[i] + '\n')
            else:
                displayString += display[i]

        print(displayString)

        print('\nGame Over!\n')
        if(self.winLoseDraw == 1):
            print('Player 1 wins!')
        elif(self.winLoseDraw == 2):
            print('Player 2 wins!')
        else:
            print("It's a draw!")
    
    def legalMoves(self):
        legalIndex = []
        for i in range(9):
            if self.gameBoard[i] == 0:
                legalIndex.append(i)
        return legalIndex


class monteCarloTreeSearch:
    def __init__(self, game, randPlayNum):
        self.game = game
        self.board = self.game.getGameBoard()
        self.state = self.game.inGame()
        self.randPlayNum = randPlayNum

    def makeMove(self):
        legalMoves = self.game.legalMoves()
        # print('list of legal moves: ', legalMoves)
        # print('gameboard: ', self.game.getGameBoard())
        moveWinCounts = {}

        for m in legalMoves:
            moveWinCounts[m] = 0
            for i in range(self.randPlayNum):  # do a set number of random play out
                # and store the result when each random playout is over
                moveWinCounts[m] += self.randomPlayOut(m)
        movechoice = legalMoves[0]
        choiceWinCount = moveWinCounts[movechoice]
        for win in moveWinCounts:
            if moveWinCounts[win] >= choiceWinCount:
                movechoice = win
                choiceWinCount = moveWinCounts[win]
        self.game.doMove(int(movechoice), self.game.activePlayer)
        # print('list of legal moves (after): ', self.game.legalMoves())
        # print('moveWinCounts = :', moveWinCounts)
        # print('movechoice:', movechoice)


# The idea is as follows. When it’s the computers turn to make a move, 
# it makes a list of all legals moves. Then for each of these moves it does some number of random playouts. 
# A random playout is when the computer simulates playing the game — using randomly chosen moves — until it is over, 
# i.e. a win, loss, or draw is reached. It records the result (a win, loss, or draw), and then does some more random playouts. 
# It does random playouts for every possible move, and when they’re done it choses the move that resulted in the greatest number of wins.

    def randomPlayOut(self, move):
        game = self.game.copyGameState()
        game.doMove(move, game.activePlayer)  # make the move
        game.switchPlayer()  # switch player
        while game.inGame() == True:
            legalMoves = game.legalMoves()
            randMove = random.randint(0, 8)
            while(randMove not in legalMoves):
                randMove = random.randint(0, 8)
            game.doMove(randMove, game.activePlayer)
            game.switchPlayer()
            game.state = game.inGame()
        if game.getAI() == 1:
            if game.winLoseDraw() == 2:
                return -2
            elif game.winLoseDraw() == 1:
                return 2
            else:
                return 1
        else:
            if game.winLoseDraw() == 2:
                return 2
            elif game.winLoseDraw() == 1:
                return -2
            else:
                return 1


def play_a_new_game():
    game = ticTacToe()
    aiMonte = monteCarloTreeSearch(game, 100)
    gameState = game.inGame()
    choice = ''

    # user guide
    print('\nHere is the number for the corresponding tile:\n')
    print('0 1 2 \n3 4 5 \n6 7 8\n')

    order = input('Do you want to go first? (type Y or N): ')

    # if the
    if (order.upper() == 'N'):
        print("You are Player 2 (O)")
        aiMonte.makeMove()
        game.switchPlayer()
        game.display()
        choice = input('Choose your next move... ')
    else:
        print("You are Player 1 (X)")
        game.setAI(2)
        game.display()
        choice = input('Choose your next move... ')
    while gameState == True:
        game.doMove(int(choice), game.activePlayer)
        
        game.switchPlayer()
        aiMonte.makeMove()

        gameState = game.inGame()
        if gameState == True:
            game.switchPlayer()
            game.display()
            choice = input('Choose your next move... ')
            gameCheck = game.copyGameState()
            gameCheck.doMove(int(choice), gameCheck.activePlayer)
            gameState = gameCheck.inGame()

    # when game comes to an end
    game.switchPlayer()
    game.doMove(int(choice), game.activePlayer)    
    game.displayEndGame()

if __name__ == '__main__':
  play_a_new_game()

