from node import node
from PriorityQueue import PriorityQueue
import sys
import problem

# this function calculates depth_limited_search algorithm, with the limit ranges that were defined in the function iterative_deepening_search()
def depth_limited_search(problem, limit = 5):
  the_node = [(node(problem.s_start))]
  frontier = the_node
  counter3 = 0
  while frontier:
      new_node = frontier.pop()
      if problem.is_goal(new_node.state):
          return new_node.solution(), counter3, new_node.path_cost
      if new_node.depth < limit:
          frontier.extend((new_node.expand(problem)))
      counter3 = counter3 + 1
      if counter3 > 10000: #for solve the infinity loop. if counter3 is greater them 10,000, so probably there is no solution and it's an infinity loop.
          return None, counter3, new_node.path_cost
  return None, counter3, new_node.path_cost

# this function defines the depth of search in any iteration (limit) of depth_limited_search algorithm.
# then, it gets the result (if there is) and bring it back to the main.
def iterative_deepening_search(problem):
  counter2 = 1
  for depth in range(1, 20):
    result, counter1, cost = depth_limited_search(problem, depth)
    counter2 = counter1 + counter2 #calculates how many nodes were developed
    if result:
      return result, counter2, cost
  return None, iterative_deepening_search