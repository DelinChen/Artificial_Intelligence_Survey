import random

# game board
# 0 1 2
# 3 4 5
# 6 7 8

class ticTacToe:
    def __init__(self):
        self.activePlayer = 1
        self.gameBoard = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.AI = 1

    # getter and setter for AI
    def getAI(self):
        return self.AI

    def setAI(self, order):
        self.AI = order
        return self.AI

    # return a copy of current game state
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

    # return true for game continues, false for end
    def inGame(self):
        if self.winLoseDraw() == -1:
            return True
        return False

    # return a list of legal moves available
    def legalMoves(self):
        legalIndex = []
        for i in range(9):
            if self.gameBoard[i] == 0:
                legalIndex.append(i)
        return legalIndex

    # if there's 0 in numArr, return False, else return True
    def noZeroCheck(self, numArr):
        for x in numArr:
            if self.gameBoard[x] == 0:
                return False
        return True

    # to check current state win or lose or draw
    def winLoseDraw(self):
        # return -1 if not finished yet
        # return 0 if draw
        # return 1 if player 1 wins
        # return 2 if player 2 wins

        winState = [(0,3,6), (1,4,7), (2,5,8), (0,1,2), (3,4,5), (6,7,8), (0,4,8), (2,4,6)]
        for i in range(8):
            if (self.gameBoard[winState[i][0]] == self.gameBoard[winState[i][1]]) and (self.gameBoard[winState[i][0]] == self.gameBoard[winState[i][2]]) and self.noZeroCheck(winState[i]):
                if self.gameBoard[winState[i][0]] == 2:
                    return 2
                else:
                    return 1
        if 0 not in self.gameBoard:
            return 0
        else:
            return -1

    def display(self):
        display = ['_ ', '_ ', '_ ', '_ ', '_ ', '_ ', '_ ', '_ ', '_ ']
        dispString = ''
        for i in range(9):
            # if taken already, change
            if self.gameBoard[i] == 1:
                display[i] = 'X '
            if self.gameBoard[i] == 2:
                display[i] = 'O '

            # append to the string
            if i == 2 or i == 5:
                dispString += (display[i] + '\n')
            else:
                dispString += display[i]

        print(dispString)
    

class monteCarloTreeSearch:
    def __init__(self, game, randPlayNum):
        self.game = game
        self.board = self.game.getGameBoard()
        self.state = self.game.inGame()
        self.randPlayNum = randPlayNum

    def makeMove(self):
        # get legal moves first
        legalMoves = self.game.legalMoves()
        winCounts = {}

        # for each legal move, do a number of random play, and store the value in winCounts
        for move in legalMoves:
            winCounts[move] = 0
            for i in range(self.randPlayNum): 
                winCounts[move] += self.randomPlay(move)

        # find the largest choice win count to find the optimal choice
        movechoice = legalMoves[0]
        choiceWinCount = winCounts[movechoice]
        for i in winCounts:
            if winCounts[i] >= choiceWinCount:
                movechoice = i
                choiceWinCount = winCounts[i]

        self.game.doMove(int(movechoice), self.game.activePlayer)


    def randomPlay(self, move):
        # get copy a copy of game, and set it as game here
        game = self.game.copyGameState()
        game.doMove(move, game.activePlayer)
        game.switchPlayer()
        while game.inGame() == True:
            legalMoves = game.legalMoves()
            randMove = random.randint(0, 8)
            while(randMove not in legalMoves):
                randMove = random.randint(0, 8)
            game.doMove(randMove, game.activePlayer)
            game.switchPlayer()
            game.state = game.inGame()

        # if the AI is player 1
        if game.getAI() == 1:
            if game.winLoseDraw() == 2:
                return -3
            elif game.winLoseDraw() == 1:
                return 2
            else:
                return 0
        else:
            if game.winLoseDraw() == 2:
                return 2
            elif game.winLoseDraw() == 1:
                return -3
            else:
                return 0

def play_a_new_game():
    game = ticTacToe()
    aiMonte = monteCarloTreeSearch(game, 1000)
    gameState = game.inGame()
    choice = ''

    # user guide
    print('\nNumber for the corresponding tile:\n')
    print('0 1 2 \n3 4 5 \n6 7 8\n')
    order = input('Do you want to go first? (Y for yes, and N for no): ')

    if (order.upper() == 'N'):
        print("You are Player 2 (O)")

        aiMonte.makeMove()
        game.switchPlayer()
        game.display()

        choice = input('Your next move is: ')
        game.doMove(int(choice), game.activePlayer)

    else:
        print("You are Player 1 (X)")

        game.setAI(2)
        game.display()

        choice = input('Your next move is: ')
        game.doMove(int(choice), game.activePlayer)

    while gameState == True:
        
        game.switchPlayer()
        aiMonte.makeMove()

        gameState = game.inGame()
        game.switchPlayer()
        if gameState == True:
            
            game.display()
            choice = input('Your next move is: ')
            game.doMove(int(choice), game.activePlayer)

            gameCheck = game.copyGameState()
            gameCheck.doMove(int(choice), gameCheck.activePlayer)
            gameState = gameCheck.inGame()

    # when game comes to an end
    game.doMove(int(choice), game.activePlayer)    
    game.display()
    print("Game Over")
    
if __name__ == '__main__':
  play_a_new_game()
