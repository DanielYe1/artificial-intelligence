from math import *
from deuces.card import Card
from deuces.evaluator import Evaluator
from deuces.evaluator import Deck
import random

class PokerState:
    def __init__(self):
        self.playerJustMoved = 2
        self.deck = Deck()
        self.board = self.deck.draw(3)
        self.player1 = self.deck.draw(2)
        self.player2 = self.deck.draw(2)
        self.evaluator = Evaluator()


    def Clone(self):
        st = PokerState()
        st.playerJustMoved = self.playerJustMoved
        st.deck = self.deck
        st.board = self.board
        st.player1 = self.player1
        st.player2 = self.player2
        return st

    def DoMove(self, move):
        """ Update a state by carrying out the given move.
            Must update playerJustMoved.
        """

        self.playerJustMoved = 3 - self.playerJustMoved

    def GetMoves(self):
        return ["aposta", "sai"]

    def GetResult(self, player1):
        p1 = self.evaluator.evaluate(self.player1, self.board)
        p2 = self.evaluator.evaluate(self.player2, self.board)
        if p1 < p2:
            return 1.0



board = [Card.new('Th'),Card.new('Kh'),Card.new('Qh'),Card.new('Jh')]
Card.print_pretty_cards(board)
p1 = [Card.new('8c'), Card.new('9c')]
e = Evaluator()

print e.evaluate(board,p1)