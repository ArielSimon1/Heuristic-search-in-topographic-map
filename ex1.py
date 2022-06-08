from node import node
import math
import json
from collections import deque
import heapq
import node
from problem import Problem
from PriorityQueue import PriorityQueue
from UCS import *
from IDS import *
from ASTAR import *

# this is the main of ex1.
# here we read the input.txt file, get the values of all parameters and write the answer to output.txt
if __name__ == '__main__':

    # read the input file and set the algorithm, the start point, the goal point and the board size and numbers (prices)
    txt = "input.txt"
    input = open(txt, "r")
    algo = input.readline().rstrip()
    s_start = input.readline().rstrip().split(',')
    goal = input.readline().rstrip().split(',')
    board_n = int(input.readline().rstrip())
    game_board = []
    for index in input:
        sub_board =[]
        for num in index.split(','):
            sub_board.append(int(num))
        game_board.append(sub_board)
    input.close()

    # converting s_start and goal to int index (not a list)
    s_start[0] = int(s_start[0])
    s_start[1] = int(s_start[1])
    #print(s_start)

    goal[0] = int(goal[0])
    goal[1] = int(goal[1])

    # this is the definition of the the heuristic function f - the Chess distance.
    # it takes the diff between the i,j indexes of 2 points (current node and goal node) and returns their maximum.
    def h(node):
        # x is j index, y is i index
        x1, x2 = int(goal[1]),int(node.state[1])
        y1, y2 = int(goal[0]), int(node.state[0])
        Y = abs(y2-y1)
        X = abs(x1-x2)
        return max(X,Y)

    # b is the object of Problem class, that gets all the data from the input.txt file.
    b = Problem(s_start, board_n, goal, game_board, algo)

    # check: if the goal node is (-1), so don't even start to check the routes to get it (because it isnt legal)
    if (game_board[goal[0]][goal[1]] == -1):
        solution = -1
    # check what is the algo we get in the input:
    # if solution == -1, so that's mean there is no path.
    elif (algo == 'UCS'):
        ans = uniform_cost_search(b)
        ans_s = str(ans)
        if not ("None") in ans_s:
            solution, cost, counter = ans
        else:
            solution = -1
    elif (algo == 'IDS'):
        ans = iterative_deepening_search(b)
        ans_s = str(ans)
        if not ("None") in ans_s:
            solution, cost, counter = ans
        else:
            solution = -1
    elif (algo == 'ASTAR'):
        ans = astar_search(b, h)
        ans_s = str(ans)
        if not ("None") in ans_s:
            solution, cost, counter = ans
        else:
            solution = -1
    elif (algo == 'IDASTAR'):
        ans = iterative_deepening_astar_search(b, h)
        ans_s = str(ans)
        if not ("None") in ans_s:
            solution, cost, counter = ans
        else:
            solution = -1

    # if we found a legal solution - we need to split the solution.
    if (solution != -1):
        solution = str(solution)
        solution = solution.replace("', ", "-")
        solution = solution.replace("'","")
        solution = solution.replace("[", "")
        solution = solution.replace("]", "")

        # export the final ans:
        f = open("output.txt", "w")
        f.write(solution+ " "+ str(counter)+ " "+ str(cost)+"\n")
        f.close()
    else: # export the final ans of "no path":
        f = open("output.txt", "w")
        f.write("no path")
        f.close()





