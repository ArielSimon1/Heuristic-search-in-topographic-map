from node import node
from PriorityQueue import PriorityQueue

# this class is for defining UCS algorithm.
# g here is the node path_cost, and the best_first_graph_search get this g and the problem object.
def best_first_graph_search(problem, f):
  the_node = node(problem.s_start)
  frontier = PriorityQueue(f)
  frontier.append(the_node)
  closed_list = set() # data structer set
  counter = -1 #initilize counter
  while frontier: # forntier isn't empty = we still have nodes to develop and check with action()
    counter = (counter + 1) # for counting how many nodes are developed
    the_node = frontier.pop() #pop out the next node in the queue of frontier, to be checked
    if problem.is_goal(the_node.state):
      return the_node.solution(),counter, the_node.path_cost
    closed_list.add(tuple(the_node.state))

    for child in the_node.expand(problem):
      if (child not in frontier) and (tuple(child.state) not in closed_list):
        frontier.append(child)
      elif child in frontier and f(child) < frontier[child]:
        del frontier[child]
        frontier.append(child)
  return None, counter

# here f = g, so uniform_cost_search algorithm sets g as best_first_graph_search (f)
def uniform_cost_search(problem):
  def g(the_node):
    return the_node.path_cost
  return best_first_graph_search(problem, g)