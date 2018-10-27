import numpy as np
from deuces import *
class PokerState:
    def __init__(self):
        self.min = False
        self.max = False
        self.chance = False
        self.deck = Deck()
        self.board = self.deck.draw(5)
        self.players = [self.deck.draw(2),self.deck.draw(2)]
        self.players_in_game = [True for i in range(len(self.players))]
        self.s_b = []
        self.s_p = []
        self.s_mv = []
        self.pot = 0

    def clone(self,state):
        nPS = PokerState()
        nPS.min = state.min
        nPS.max = state.max
        nPS.chance = state.chance
        nPS.deck = state.deck[:]
        nPS.board = state.board[:]
        nPS.players = state.players[:]
        nPS.stack_aposta = state.stack_aposta[:]


    def moves(self):                        #,stack):
         return['bet','cal','fold','raise']

    def doMove(self,move):
        if(move == 'fold'):
            self.s_mv.append('fold')
        elif(self.s_mv.append(move)):



def expectminimax(state,depth,a,b):
    if(depth == 5 ):# max_depth retorna a funcao de utilidade
        return state.value #retorna o valor de utilidade de v
    elif(state.chance): # o estado atual eh um calculo de chance
        d = 1
        s = 0
        #todo  filho de state do
        for i in state.children():
            d = d - P(i)
            e = expectminimax(clone(i),depth+1)
            s = s + p(u)*e

        return s
    elif(state.min):
        e = 99999999

        for i in state.children():
            t = expectminimax(clone(i),depth+1)
            if(t < e) : e = t
        return e
    elif(state.max):

        e = -99999999

        for i in state.children():
            t = expectminimax(clone(i),depth+1)
            if(t > e) : e = t
        return e
