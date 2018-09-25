from deuces import *

class player:
    def __init__(self,buyin):
        self.hand = "12"
        self.pocket = buyin
        self.lastplay = ''
class PokerState:
    "A state in poker game"


    def __init__(self,players):
        self.playerJustMoved = 2
        self.board = [0,0,0,0,0]
        self.playas = players
        self.pot = 0


    def Clone(self):
        st = PokerState(self.playas)
        st.playerJustMoved = self.playerJustMoved
        st.board = self.board[:]
        return st

    def DoMove(self,move):
        self.playerJustMoved = 3 - self.playerJustMoved
        atual = self.playerJustMoved
        assert atual.pocket > 0

        if move[0] == 'fold':
             self.playas = self.playas[3- atual-1]
        if move[0] == 'raise ' and atual.pocket >= 10:
            self.pot += 10.0
            atual.pocket -= 10.0
        if self.playas[3-atual-1].lastPlay == 'check':
            pass
        else:
            atual.pocket  -= 5.0
            self.pot += 5.0
    def GetMoves(self):
        return ['fold','raise','bet','check']


