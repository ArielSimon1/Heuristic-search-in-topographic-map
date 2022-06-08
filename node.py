from functools import total_ordering
import json
from collections import deque
import heapq
import Internal_functions
import problem

# this class defines the object of node and all the possible actions the agent can do with it.
# the node represent a specific state of the current location on the game_board.
@total_ordering
class node:
    #constructor of the class.
    def __init__(self, state, parent=None, action=None, path_cost=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost
        self.depth = 0
        if parent:
            self.depth = parent.depth + 1

    # this function returns all the legal childs of a current node.
    def expand(self, problem):
        return Internal_functions.ordered_set([self.child_node(problem, action)
                            for action in problem.actions(self.state)], problem.algo)

    # this function defines who are a legal childs of a current node.
    def child_node(self, problem, action):
        next_state = problem.succ(self.state, action)
        next_node = node(next_state, self, action,
                         self.path_cost + problem.step_cost(self.state, action))
        return next_node

    # this function returns all the actions (movements) in a path (useing the path() function).
    # we use this function for getting the whole route of the final solution.
    def solution(self):
        return [node.action for node in self.path()[1:]]

    # this function returns the path-back of a specific node.
    def path(self):
        node, path_back = self, []
        while node:
            path_back.append(node)
            node = node.parent
        return list(reversed(path_back))

    # this function ranking each action (out of 8 possible actions) by clockwise.
    def priority_a(self, action):
        if action == 'R':
            self.priority = 1
        if action == 'RD':
            self.priority = 2
        if action == 'D':
            self.priority = 3
        if action == 'LD':
            self.priority = 4
        if action == 'L':
            self.priority = 5
        if action == 'LU':
            self.priority = 6
        if action == 'U':
            self.priority = 7
        if action == 'RU':
            self.priority = 8
        return self.priority

    # this function helps order the nodes in the queue as we defines it in the instructions of ex1.
    def __lt__(self, node):
        return self.state < node.state and self.priority_a(self.action) < node.priority_a(node.action)

    def __repr__(self):
        return f"<{self.state}>"

    def __eq__(self, other):
        return isinstance(other, node) and self.state == other.state

    def __ne__(self, other):
        return not (self == other)

    def __hash__(self):
        return hash(tuple(self.state))
    # should try to do: hash(tuple(self.state))