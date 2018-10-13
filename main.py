from math import inf as infinity
import random
from random import choice

class Board:
    player1 = 1
    player2 =2
    COMP = -1             #when chosen To play with AI player2==COMP
    player1key='O'
    player2key='X'
    player1score=-1
    player2score=1

    def __init__(self):
        self.board_mat = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
        print (' TIc -TAc-TOe')
        print(1, '|', 2, '|', 3)
        print(4, '|', 5, '|', 6)
        print(7, '|', 8, '|', 9)
        print('\n')
        print('You can choose a number in the given matrix to place your key')
        print('\n')


    def reset (self):
        self.board_mat = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
        game_Board.player2=2                                   #to initializze value if any change brought to value of player2 mainfile prev game



    def display(self):
        print(self.board_mat[0], '|', self.board_mat[1], '|', self.board_mat[2])
        print(self.board_mat[3], '|', self.board_mat[4], '|', self.board_mat[5])
        print(self.board_mat[6], '|', self.board_mat[7], '|', self.board_mat[8])
        print('\n')

    def update(self, player, chosen_spot):                     #updates and gives status if the operation is performed or not
        if player == self.player1 and self.board_mat[chosen_spot - 1] == ' ':
            self.board_mat[chosen_spot - 1] = 'O'
            return 1

        if player == self.player2 and self.board_mat[chosen_spot - 1] == ' ':
            self.board_mat[chosen_spot - 1] = 'X'
            return 1
        else:
            return 0

    def empty_cell_index(self):                               #return list containing indexes of empty cell
        cell_index=[]
        for i in range(0,9):
            if self.board_mat[i]==' ':
                cell_index.append(i)
        return cell_index

    def aichoice(self,player,height):
        depth= 9- height
        if depth== 9:                                         #if the board is completely empty then it choses a random spot
            return random.choice(self.empty_cell_index())     #if minmax regulated mainfile depth = 9 it will always give the first
                                                              #index so to avoid this random value is taken
        else: return self.minimax(player,depth)[0]
        return self.minimax(player,depth)[0]

    def minimax(self,player,depth):                           #real depth mainfile range(1,9)(=9 - step,where eff.steo mainfile range(1,9))
        score= self.check()

        if player==self.player1:best=[-1,+infinity]
        if player==self.COMP:best=[-1,-infinity]

        if depth==0 or not score==0:                          #at the node termination return
            return [-1,score]                                 #depth = 0 means the node has no branches because the space
                                                              # being filled
                                                              #score==1 or -1 means either of the two has won

        for index in self.empty_cell_index():
            if player == self.player1:
                self.board_mat[index]=self.player1key
            else :self.board_mat[index]=self.player2key
            rec = self.minimax(-player,depth-1)               #recursion for each node
            self.board_mat[index]=' '                         #reset
            rec[0]=index

            if player==self.COMP:
                if rec[1]>best[1]:best =rec
            if player==self.player1:
                if rec[1]<best[1]:best=rec

        return best

    def get_input(self,player,height):
        if not player==self.COMP:
            while True:                                          #exception handling block
                try:
                    chosen_spot = input('choose your spot')
                    val = int(chosen_spot)
                except ValueError:
                    print("That's not an int!")
                    continue
                if val not in range(0,10):
                    print('enter a value between 0-9')
                elif not self.update(player,val):
                    print('Chose an empty spot')
                else :break

        else:
            val=self.aichoice(player,height)                     #this returns a value 0-8
            return self.update(player,val + 1)                   #to give potion is value from 1-9 1 is added



    def get_pref(self):
        while True:                                              #exception handling block
            try:
                chosen_turn = input('Player1,choose your turn(1/2)')
                val = int(chosen_turn) -1
            except ValueError:
                print("That's not an int!")
                continue
            if val not in (0,1):
                print('enter a value among 1 or 2')
            else:
                break
        return val


    def iswithai(self):
        while True:                                                #exception handling block
            try:
                choice = input('1.Two players 2.Play single')
                val = int(choice)-1
            except ValueError:
                print("That's not an int!")
                continue
            if val not in (0,1):
                print('Chose among 1 or 2')
            else:
                break
        return val


    def check(self):
        for player in (self.player1,self.player2):
            if player==self.player1:
                playerkey = self.player1key
                score=self.player1score      #-1

            else:
                playerkey=self.player2key
                score=self.player2score      #1

            if self.board_mat[0]==self.board_mat[1]==self.board_mat[2]==playerkey or\
                self.board_mat[3]==self.board_mat[4]==self.board_mat[5]==playerkey or\
                self.board_mat[3]==self.board_mat[4]==self.board_mat[5]==playerkey or\
                self.board_mat[6]==self.board_mat[7]==self.board_mat[8]==playerkey or\
                self.board_mat[0]==self.board_mat[3]==self.board_mat[6]==playerkey or\
                self.board_mat[1]==self.board_mat[4]==self.board_mat[7]==playerkey or\
                self.board_mat[2]==self.board_mat[5]==self.board_mat[8]==playerkey or\
                self.board_mat[0]==self.board_mat[4]==self.board_mat[8]==playerkey or\
                self.board_mat[2]==self.board_mat[4]==self.board_mat[6]==playerkey:
                return score

        else: return 0


def game (game_Board):
    while 1:
        playgame = input('Would  you like  to play a game (Y/N)?').upper()
        if playgame=='Y':
            if game_Board.iswithai():
                setcomp=game_Board.get_pref()#1 for  ai first
                game_Board.player2=game_Board.COMP
            else: setcomp=0

            for step in range(0,9):
                if not (step+setcomp)%2:
                    player=game_Board.player1
                    print('player1\'s turn')
                else:
                    player=game_Board.player2
                    if not game_Board.player2==game_Board.COMP:
                        print('player2\'s turn')
                    
                game_Board.get_input(player,step)
                game_Board.display()
                score=game_Board.check()
                if not game_Board.player2==game_Board.COMP :
                    if score==game_Board.player1score:
                       print('Player1 wins')
                       break

                    elif score==game_Board.player2score:
                       print('player2 wins')
                       break

                else:
                    if score==game_Board.player1score:
                            print('You win')
                            break

                    elif score==game_Board.player2score:
                            print('You lose')
                            break

            if step==8 and score==0:
                print ('DRAW')

        elif playgame == 'N':
            quit()

        else:print ('Enter a Y or N')

        game_Board.reset()


game_Board=Board()  #prepares the board
game (game_Board)   #initiates the game using the board















