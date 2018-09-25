from deuces import *
import deuces
import random
from math import *
from deuces.evaluator import *


class player:
    def __init__(self, hand):
        self.hand = hand
        self.pocket = 5000.0
        self.lastplay = ''


class PokerState:
    "A state in poker game"
    def __init__(self, players,deck,board):
        self.playerJustMoved = 2
        self.deck = deck
        self.board = board
        self.players = list(players)
        self.pot = 0
        self.eval = Evaluator()

    def Clone(self):
        st = PokerState(self.players,self.deck,self.board)
        st.playerJustMoved = self.playerJustMoved
        st.board = self.board[:]
        return st

    def DoMove(self, move):
        self.playerJustMoved = 3 - self.playerJustMoved
        atual = self.players[self.playerJustMoved-1]
        assert atual.pocket > 0

        if move[0] == 'fold':
            self.players = self.players[3 - atual - 1]
        if move[0] == 'raise ' and atual.pocket >= 10:
            self.pot += 10.0
            atual.pocket -= 10.0
        if self.players[3 - self.playerJustMoved - 1].lastplay == 'check':
            pass
        else:
            atual.pocket -= 5.0
            self.pot += 5.0


    def GetMoves(self):
        return ['fold', 'raise', 'bet', 'check']

    def GetResult(self, playerjm):
        p1 = self.eval.evaluate(self.players[0].hand, self.board)
        p2 = self.eval.evaluate(self.players[1].hand, self.board)
        if p1 < p2:
            return 1.0
        elif p1 == p2:
            return 0.0
        return -1


class Node:
    """ A node in the game tree. Note wins is always from the viewpoint of playerJustMoved.
        Crashes if state not specified.
    """

    def __init__(self, move=None, parent=None, state=None):
        self.move = move  # the move that got us to this node - "None" for the root node
        self.parentNode = parent  # "None" for the root node
        self.childNodes = []
        self.wins = 0
        self.visits = 0
        self.untriedMoves = state.GetMoves()  # future child nodes
        self.playerJustMoved = state.playerJustMoved  # the only part of the state that the Node needs later

    def UCTSelectChild(self):
        """ Use the UCB1 formula to select a child node. Often a constant UCTK is applied so we have
            lambda c: c.wins/c.visits + UCTK * sqrt(2*log(self.visits)/c.visits to vary the amount of
            exploration versus exploitation.
        """
        s = sorted(self.childNodes, key=lambda c: c.wins / c.visits + sqrt(2 * log(self.visits) / c.visits))[-1]
        return s

    def AddChild(self, m, s):
        """ Remove m from untriedMoves and add a new child node for this move.
            Return the added child node
        """
        n = Node(move=m, parent=self, state=s)
        self.untriedMoves.remove(m)
        self.childNodes.append(n)
        return n

    def Update(self, result):
        """ Update this node - one additional visit and result additional wins. result must be from the viewpoint of playerJustmoved.
        """
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
    """ Conduct a UCT search for itermax iterations starting from rootstate.
        Return the best move from the rootstate.
        Assumes 2 alternating players (player 1 starts), with game results in the range [0.0, 1.0]."""

    rootnode = Node(state=rootstate)

    for i in range(itermax):
        node = rootnode
        state = rootstate.Clone()

        # Select
        while node.untriedMoves == [] and node.childNodes != []:  # node is fully expanded and non-terminal
            node = node.UCTSelectChild()
            state.DoMove(node.move)

        # Expand
        if node.untriedMoves != []:  # if we can expand (i.e. state/node is non-terminal)
            m = random.choice(node.untriedMoves)
            state.DoMove(m)
            node = node.AddChild(m, state)  # add child and descend tree

        # past = set()
        # Rollout - this can often be made orders of magnitude quicker using a state.GetRandomMove() function

        rolloutMoves = state.GetMoves()

        while rolloutMoves != []:  # while state is non-terminal
            move =random.choice(rolloutMoves)
            rolloutMoves.remove(move)
            state.DoMove(move)

        # Backpropagate
        while node != None:  # backpropagate from the expanded node and work back to the root node
            node.Update(state.GetResult(
                node.playerJustMoved))  # state is terminal. Update node with result from POV of node.playerJustMoved
            node = node.parentNode

    # Output some information about the tree - can be omitted
    if (verbose):
        print rootnode.TreeToString(0)
    else:
        print rootnode.ChildrenToString()

    return sorted(rootnode.childNodes, key=lambda c: c.visits)[-1].move  # return the move that was most visited


def UCTPlayGame():
    """ Play a sample game between two UCT players where each player gets a different number
        of UCT iterations (= simulations = tree nodes).
    """
    # state = OthelloState(4) # uncomment to play Othello on a square board of the given size
    # state = OXOState() # uncomment to play OXO
    deck = Deck()
    p1 = player(deck.draw(2))
    p2 = player(deck.draw(2))
    state = PokerState([p1,p2],deck,deck.draw(3))  # uncomment to play Nim with the given number of starting chips
    # while (p1.pocket > 0 and p2.pocket > 0):
    print str(state)
    if state.playerJustMoved == 1:
        m = UCT(rootstate=state, itermax=50, verbose=False)  # play with values for itermax and verbose = True
    else:
        m = UCT(rootstate=state, itermax=20, verbose=False)
    print "Best Move: " + str(m) + "\n"
    state.DoMove(m)
    if state.GetResult(state.playerJustMoved) == 1.0:
        print "Player " + str(state.playerJustMoved) + " wins!"
    elif state.GetResult(state.playerJustMoved) == 0.0:
        print "Player " + str(3 - state.playerJustMoved) + " wins!"
    else:
        print "Nobody wins!"


if __name__ == "__main__":
    """ Play a single game to the end using UCT for both players. 
    """
    UCTPlayGame()
