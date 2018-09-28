from deuces import *
import deuces
import random
from math import *
from deuces.evaluator import *


class PokerState:
    "A state in poker game"
    def __init__(self,qntd_players):
        # self.game_deck = deuces.deck
        # self.player_turn = 0
        # self.state = 0
        # self.game = game(qntd_players)
        # self.game.board = self.game.game_deck.draw(5)
        # self.game.players = [self.game.game_deck.draw(2),self.game.game_deck.draw(2)]
        # self.players_list = self.game.player_on

        self.game_deck = deuces.Deck()
        self.game_players = [self.game_deck.draw(2), self.game_deck.draw(2)]
        self.last_act = [1,1]
        self.board = self.game_deck.draw(5)
        self.player_turn = 0
        self.state = 1
        self.eval = deuces.Evaluator()

    def Clone(self):
        st = PokerState(self)
        st.player_turn = int(self.player_turn)
        st.state= self.state
        st.eval = self.eval
        st.last_act = self.last_act[:]
        st.game_players= self.game_players[:]
        st.board = self.board[:]

        return st



    def GetMoves(self):

        if(self.state >= 3) : return []

        if self.last_act[abs(self.player_turn-1)] == 'fold':return []

        return ['call', 'fold','bet','raise']


    def GetResult(self,pt):
        if self.last_act[pt] == 'fold':
            return 1.0
        elif self.last_act[(pt+1)%2] == 'fold':
            return 0.0
        else:
            p1 = self.eval.evaluate(self.game_players[abs(pt-1)], self.board[:(2+self.state)])
            p2 = self.eval.evaluate(self.game_players[pt], self.board[:(2 + self.state)])
            if p1 < p2:
                return 1.0
            else:
                return 0.0



    def prox_valido(self,indice):
        return (indice+1)%2




    def DoMove(self, move):

        if move == 'fold':

            self.last_act[self.player_turn] = 'fold'

        if (move == 'bet'):

            self.last_act[self.player_turn] = 'bet'



        if (move == 'check'):
            self.last_act[self.player_turn] = 'check'
        self.player_turn = abs(self.player_turn - 1)

        if self.player_turn - 1 == 0 :
            self.state += 1



class Node:
    """ A node in the game tree. Note wins is always from the viewpoint of playerJustMoved.
        Crashes if state not specified.
    """

    def __init__(self, move=None, parent=None, state=None):
        self.move = move
        self.parentNode = parent
        self.childNodes = []
        self.wins = 0
        self.visits = 0
        self.untriedMoves = state.GetMoves()
        self.playerJustMoved = state.player_turn

    def UCTSelectChild(self):

        s = sorted(self.childNodes, key=lambda c: c.wins / c.visits + sqrt(2 * log(self.visits) / c.visits))[-1]
        return s

    def AddChild(self, m, s):

        n = Node(move=m, parent=self, state=s)
        self.untriedMoves.remove(m)
        self.childNodes.append(n)
        return n

    def Update(self, result):

        self.visits += 1
        self.wins += result

    def __repr__(self):
        return "[M:" + str(self.move) + " W/V:" + str(self.wins) + "/" + str(self.visits) + " U:" + str(
            self.untriedMoves) + "]"

    def TreeToString(self, indent):
        s = self.IndentString(indent) + str(self)
        for c in self.childNodes:
            s += c.TreeToString(indent + 1)
        return s

    def IndentString(self, indent):
        s = "\n"
        for i in range(1, indent + 1):
            s += "| "
        return s

    def ChildrenToString(self):
        s = ""
        for c in self.childNodes:
            s += str(c) + "\n"
        return s


def UCT(rootstate, itermax, verbose=False):


    rootnode = Node(state=rootstate)

    for i in range(itermax):
        node = rootnode
        state = rootstate.Clone()

        # Select
        while node.untriedMoves == [] and node.childNodes != []:
            node = node.UCTSelectChild()
            state.DoMove(node.move)

        # Expand
        if node.untriedMoves != []:
            m = random.choice(node.untriedMoves)
            state.DoMove(m)
            node = node.AddChild(m, state)


        rolloutMoves = state.GetMoves()

        while rolloutMoves != []:
            move =random.choice(rolloutMoves)
            rolloutMoves.remove(move)
            state.DoMove(move)

        # Backpropagate
        while node != None:
            node.Update(state.GetResult(
                node.playerJustMoved))
            node = node.parentNode

    if (verbose):
        print rootnode.TreeToString(0)
    else:
        print rootnode.ChildrenToString()

    return sorted(rootnode.childNodes, key=lambda c: c.visits)[-1].move  # return the move that was most visited


def UCTPlayGame():
    state = PokerState(2)  # uncomment to play Nim with the given number of starting chips
    print str(state)
    while (state.GetMoves() != []):
        if state.player_turn == 0:
            m = UCT(rootstate=state, itermax=1000, verbose=True)  # play with values for itermax and verbose = True
        else:
            m = UCT(rootstate=state, itermax= 1000, verbose=True)
        print "Best Move: " + str(m) + "\n"
        state.DoMove(m)
    if state.GetResult(state.player_turn) == 1.0:
        print "Player " + str(state.player_turn) + " wins!"
    else:
        print "player 2 wins!"


if __name__ == "__main__":
    """ Play a single game to the end using UCT for both players. 
    """
    UCTPlayGame()
