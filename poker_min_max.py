from deuces import *
import deuces
import random
from math import *
from deuces.evaluator import *


class PokerState:
    "A state in poker game"

    def __init__(self, qntd_players):

        self.game_deck = deuces.Deck()
        self.game_players = [self.game_deck.draw(2), self.game_deck.draw(2)]
        self.last_act = [1, 1]
        self.board = self.game_deck.draw(5)
        self.player_turn = 0
        self.state = 1
        self.eval = deuces.Evaluator()

    def Clone(self):
        st = PokerState(self)
        st.player_turn = int(self.player_turn)
        st.state = self.state
        st.eval = self.eval
        st.last_act = self.last_act[:]
        st.game_players = self.game_players[:]
        st.board = self.board[:]

        return st

    def GetMoves(self):

        if (self.state >= 3): return []

        if self.last_act[abs(self.player_turn - 1)] == 'fold': return []

        return ['call', 'fold', 'bet', 'raise']

    def GetResult(self, pt):
        if self.last_act[pt] == 'fold':
            return 1.0
        elif self.last_act[(pt + 1) % 2] == 'fold':
            return 0.0
        else:
            p1 = self.eval.evaluate(self.game_players[abs(pt - 1)], self.board[:(2 + self.state)])
            p2 = self.eval.evaluate(self.game_players[pt], self.board[:(2 + self.state)])
            if p1 < p2:
                return 1.0
            else:
                return 0.0

    def prox_valido(self, indice):
        return (indice + 1) % 2

    def DoMove(self, move):

        if move == 'fold':
            self.last_act[self.player_turn] = 'fold'

        if (move == 'bet'):
            self.last_act[self.player_turn] = 'bet'

        if (move == 'check'):
            self.last_act[self.player_turn] = 'check'
        self.player_turn = abs(self.player_turn - 1)

        if self.player_turn - 1 == 0:
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


def min_max(rootstate, tree_depth, actual_depth, max_or_min, move, verbose=False):
    if actual_depth == tree_depth:
        return max_or_min

    rootnode = Node(state=rootstate)
    node = rootnode
    state = rootstate.Clone()
    all_values = []

    for node_move in state.GetMoves():
        if max_or_min == 1:
            all_values.insert(0, min_max(rootstate, tree_depth, actual_depth+1, 0, node_move))
        elif max_or_min == 0:
            all_values.insert(0, min_max(rootstate, tree_depth, actual_depth+1, 1, node_move))

    if max_or_min == 1:
        return all_values.min
    elif max_or_min == 0:
        return all_values.max

    return all_values


def UCTPlayGame():
    state = PokerState(2)  # uncomment to play Nim with the given number of starting chips
    print str(state)
    x = 3
    Card.print_pretty_cards(state.board[:x])
    Card.print_pretty_cards(state.game_players[0])
    while (state.GetMoves() != []):
        if state.player_turn == 0:
            m = raw_input("digite jogada: call, raise, fold, bet")  # play with values for itermax and verbose = True
            x += 1
            Card.print_pretty_cards(state.board[:x])
        else:
            m = min_max(rootstate=state, m_index=1, verbose=False)
        print "Best Move: " + str(m) + "\n"
        state.DoMove(m)
    Card.print_pretty_cards(state.game_players[1])
    if state.GetResult(state.player_turn) == 1.0:
        print "Player " + str(state.player_turn) + " wins!"
    else:
        print "player 2 wins!"


if __name__ == "__main__":
    """ Play a single game to the end using UCT for both players. 
    """
    UCTPlayGame()
