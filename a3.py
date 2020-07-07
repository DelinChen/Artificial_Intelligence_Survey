# a3.py

# game board
# 0 1 2
# 3 4 5
# 6 7 8

import random
import operator

class ticTacToe:
    def __init__(self):
        self.currentPlayer = 1
        self.gameBoard = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.AI = 1

    # getter and setter for AI
    def getAI(self):
        return self.AI

    def setAI(self, order):
        self.AI = order
        return self.AI

    def getGameBoard(self):
        return self.gameBoard

    def currentPlayer(self):
        return self.currentPlayer

    # return a copy of current game state
    def copyGame(self):
        copy = ticTacToe()
        copy.currentPlayer = self.currentPlayer
        copy.gameBoard = self.gameBoard[:]
        copy.AI = self.AI
        return copy

    def switchPlayer(self):
        if (self.currentPlayer == 1):
            self.currentPlayer = 2
        if (self.currentPlayer == 2):
            self.currentPlayer = 1
        return self.currentPlayer

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
        moves = []
        for i in range(9):
            if self.gameBoard[i] == 0:
                moves.append(i)
        return moves

    # if there's 0 in numArr, return False, else return True
    def noZeroCheck(self, numArr):
        for x in numArr:
            if self.gameBoard[x] == 0:
                return False
        return True

    # to check current state win or lose or draw
    # return -1 if not finished yet, return 0 if draw
    # return 1 if player 1 wins, return 2 if player 2 wins
    def winLoseDraw(self):
        winState = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
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
        string = ''
        for i in range(9):
            if self.gameBoard[i] == 1:
                string +='X '
            elif self.gameBoard[i] == 2:
                string += 'O '
            else:
                string += '_ '

            if i == 2 or i == 5:
                string += '\n'

        print(string)
    
# read https://towardsdatascience.com/monte-carlo-tree-search-158a917a8baa for help with Monte Carlo Tree Search
class monteCarloTreeSearch:
    def __init__(self, game):
        self.game = game
        self.board = self.game.getGameBoard()
        self.state = self.game.inGame()
        self.randNum = 1000

    def doMove(self):
        legalMoves = self.game.legalMoves()
        winCounts = {}

        # for each legal move, do a number of random play, and store the value in winCounts
        for move in legalMoves:
            winCounts[move] = 0;
            for i in range(self.randNum): 
                winCounts[move] += self.randomPlayOuts(move)

        # learned from https://stackoverflow.com/questions/268272/getting-key-with-maximum-value-in-dictionary
        optChoice = max(winCounts.items(), key = operator.itemgetter(1))[0]

        self.game.doMove(int(optChoice), self.game.currentPlayer)

    def randomPlayOuts(self, move):
        # get copy a copy of game, and set it as game here
        game = self.game.copyGame()
        game.doMove(move, game.currentPlayer)
        while game.inGame() == True:
            game.switchPlayer()
            legalMoves = game.legalMoves()

            randMove = random.choice(legalMoves)
            game.doMove(randMove, game.currentPlayer)

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
    AI = monteCarloTreeSearch(game)
    gameState = game.inGame()

    # user guide
    print('\nNumbers for the positions:\n')
    print('0 1 2 \n3 4 5 \n6 7 8\n')
    order = input('Do you want to go first? (Y for yes, and N for no): ')

    if (order.upper() == 'N'):
        print("You are Player 2 (O)")

        AI.doMove()
        game.switchPlayer()
        game.display()

        choice = input('Please enter your next move: ')
        game.doMove(int(choice), game.currentPlayer)
    else:
        print("You are Player 1 (X)")

        game.setAI(2)
        game.display()

        choice = input('Please enter your next move: ')
        game.doMove(int(choice), game.currentPlayer)

    while gameState:
        game.switchPlayer()
        AI.doMove()

        gameState = game.inGame()
        game.switchPlayer()
        if gameState:
            
            game.display()
            choice = input('Please enter your next move: ')
            game.doMove(int(choice), game.currentPlayer)

            copy = game.copyGame()
            copy.doMove(int(choice), copy.currentPlayer)
            gameState = copy.inGame()

    # when game comes to an end
    game.doMove(int(choice), game.currentPlayer)    
    game.display()
    print("Game Over")
    
if __name__ == '__main__':
  play_a_new_game()
