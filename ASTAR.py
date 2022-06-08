from node import node
from PriorityQueue import PriorityQueue
import sys
import problem
from UCS import *
# this class is for all the ASTAR algos - regular ASTAR and Iterative Deepening ASTAR.
# it gets an heuristic function h from the main, and using it for estimating the rest of the distance to the goal.

# this function return the solution for ASTAR algorithm, that uses BFS (best_first_graph_search() is in class UCS) + heuristics.
def astar_search(problem, h):
  def g(node):
    return node.path_cost
  return best_first_graph_search(problem, f = lambda n: g(n)+h(n)) #best_first_graph_search() is in class UCS

# this function is like depth_limited_search in IDS class, just with f as parameter.
# f is the h heuristic function.
def depth_limited_search_by_cost(problem, limit, f):
  new_node = node(problem.s_start)
  frontier = [new_node]
  counter = 0
  while frontier:
    new_node = frontier.pop()
    counter = counter +1
    if problem.is_goal(new_node.state):
      return new_node.solution(), counter, new_node.path_cost
    if f(new_node) < limit:
      frontier.extend(new_node.expand(problem))
  return None, counter, new_node.path_cost

# this function defines the depth of search in any iteration (limit) of depth_limited_search_by_cost algorithm.
# then, it gets the result (if there is) and bring it back to the main. h is the heuristic function from the main.
def iterative_deepening_astar_search(problem, h):
  def g(node):
    return node.path_cost
  counter1 = -1
  for i in range(1,20):
    result , counter2, cost = depth_limited_search_by_cost(problem, i, f= lambda n: g(n) + h(n))
    counter1 = counter2 + counter1
    if result:
      return result, counter1, cost
  return None