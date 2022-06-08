import heapq

# this class organize the order of the nodes in the "expand" function, of the class "node".
# for UCS algorithm we need to keep the order as usual, in the other algorithms we need to reverse the order as stack.
# this class has only 1 function, so the description of the class is same to the function's description.
def ordered_set(coll, algo):
 if (algo == 'UCS'):
   return dict.fromkeys(coll).keys()
 order = dict.fromkeys(coll).keys()
 return reversed(sorted(order))
