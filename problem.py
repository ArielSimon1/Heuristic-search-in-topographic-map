# this class defines the Problem object.
# it gets the start point. goal point, size of board, board and algorithm, and build a problem object that the agent can work with.

class Problem:

    #constructor of the class
    def __init__(self, s_start, board_n, goal, graph, algo):
        self.s_start = s_start
        self.n = board_n
        self.goal = goal
        self.graph = graph
        self.algo = algo
        self.moves = {
            # this code defindes all the allowed movements between the nodes.
            # we want to preserve the borders of the board, and consider the rule of (-1) as it defined in the instructions.
            'RD': lambda x: x[1] + 1 < (self.n) and x[0] + 1 < self.n and (self.graph[x[0]][x[1] + 1] != -1 and self.graph[x[0] + 1][x[1]] != -1
                        and self.graph[x[0] + 1][x[1] + 1] != -1),
            'RU': lambda x: x[1] +1 < self.n and (x[0] -1 > -1) and
                            (self.graph[x[0]-1][x[1]+1] != -1 and self.graph[x[0]-1][x[1]] != -1
                                                                     and self.graph[x[0]][x[1]+1] != -1),
            'LD': lambda x: x[1] -1 > -1 and x[0] +1 < self.n and (self.graph[x[0]+1][x[1]-1] != -1 and self.graph[x[0]][x[1]-1] != -1
                                                                     and self.graph[x[0]+1][x[1]] != -1),
            'LU': lambda x: x[1] -1 > -1 and x[0] -1 > -1 and (self.graph[x[0]-1][x[1]-1] != -1 and self.graph[x[0]][x[1]-1] != -1
                                                                     and self.graph[x[0]-1][x[1]] != -1),
            'R': lambda x: x[1] + 1 < (self.n) and (self.graph[x[0]][x[1] + 1] != -1),
            'L': lambda x: x[1] - 1 > -1 and (self.graph[x[0]][x[1] - 1] != -1),
            'D': lambda x: x[0] + 1 < self.n and (self.graph[x[0] + 1][x[1]] != -1),
            'U': lambda x: x[0] - 1 > -1 and (self.graph[x[0] - 1][x[1]] != -1)
        }
        self.transitions = {
            'L': -1,
            'R': +1,
            'U': -1,
            'D': +1,
        }

    # this function returns all the legal moves from state s, based on self.moves() i defined above.
    def actions(self, s):
        return [m for (m, f) in self.moves.items() if f(s)]

    # this function returns the new s we get if we do action a from current state s
    def succ(self, s, a):
        # check what is the next allowed movement.
        # a is an action() parameter, s is a state point.
        if a in self.moves:
            if (a == 'R'):
                    return [s[0], s[1] + 1]
            elif (a =='L'):
                    return [s[0], s[1] - 1]
            elif (a == 'U'):
                    return [s[0] - 1, s[1]]
            elif (a == 'D'):
                    return [s[0] + 1, s[1]]
            elif (a == 'RU'):
                    return [s[0] - 1, s[1] + 1]
            elif (a == 'LU'):
                 return [s[0] - 1, s[1] - 1]
            elif (a == 'RD'):
                    return [s[0] + 1, s[1] + 1]
            elif (a == 'LD'):
                  return [s[0] + 1, s[1] - 1]
        raise ValueError(f'No route from {s} to {a}')

    # returns the value inside a current node index.
    def step_cost(self, s, a):
        # cost = the int value of the current panel
        val = self.succ(s,a)
        return (self.graph[val[0]][val[1]])

    # boolian function, checks if current node is the goal node.
    def is_goal(self, s):
        return (s == self.goal)

    # returns current state.
    def state_str(self, s):
        return s