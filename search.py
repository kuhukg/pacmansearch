# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    """
    start = [problem.getStartState(), list(), None]
    successors = list()
    path = dict()
    counter = 0
    fringe = util.Stack()
    fringe.push(start)
    while (not fringe.isEmpty()):
        state = fringe.pop()
        if (problem.isGoalState(state[0])):
            return state[1]
        if (path.get(state[0]) != 1):
            path[state[0]] = 1
            result = list(state[1])
            for child in problem.getSuccessors(state[0]):
                baby = list()
                baby.append(child[0])
                result.append(child[1])
                print str(result)
                baby.append(result)
                baby.append(child[2])
                fringe.push(baby)
    return result
    """
    counter = 0
    # get start state
    start = problem.getStartState()
    print "start : ", start

    # first node
    node = [start,[]]

    #create the stack
    stack = util.Stack()
    print "Stack created"

    # keep track of visited nodes
    visited = []

    # path between start and goal node
    path = []

    # add start to stack
    stack.push(node)

    # if the start state itself is the goal state
    if problem.isGoalState(start):
        return node[1]

    # while there is something in stack
    while stack:
        counter+=1
        print "Iteration", counter
        # pop out a node
        node = stack.pop()
        print "Popped Parent " , node

        # check its already visited, if yes skip it
        if node[0] in visited:
            print "node is already visited, skip it"
            continue

        # parent node is the goal state
        print "Check goal state",node[0]
        if problem.isGoalState(node[0]):
            print "Goal found returning " , node[1]
            return node[1]

        print "Mark node Visted" , node
        # append the visited node
        visited.append(node[0])

        print "Get childs for node" , node
        # get the successors
        children = problem.getSuccessors(node[0])
        print "Found children", len(children)
        # loop through the children and add them to stack
        for child in children:
            print "found child : ", child
            print node[1], child[1]
            # create the child node and add to stack
            cnode = [child[0],node[1] + [child[1]]]
            print "Add child to stack: ", cnode
            stack.push(cnode)


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    counter = 0
    # get start state
    start = problem.getStartState()
    print "start : ", start

    # first node
    node = [start,[]]

    #create the queue
    queue = util.Queue()
    print "Queue created"

    # keep track of visited nodes
    visited = []

    # path between start and goal node
    path = []

    # add start to queue
    queue.push(node)

    # if the start state it self is the goal state
    if problem.isGoalState(start):
        return node[1]

    # while there is something in queue
    while queue:
        counter+=1
        print "Iteration", counter
        # pop out a node
        node = queue.pop()
        print "Popped Parent " , node

        # check its already visited, if yes skip it
        if node[0] in visited:
            print "node is already visited, skip it"
            continue

        # parent node is the goal state
        print "Check goal state",node[0]
        if problem.isGoalState(node[0]):
            print "Goal found returning " , node[1]
            return node[1]

        print "Mark node Visted" , node
        # append the visited node
        visited.append(node[0])

        print "Get childs for node" , node
        # get the successors
        children = problem.getSuccessors(node[0])
        print "Found children", len(children)
        # loop through the children and add them to stack
        for child in children:
            print "found child : ", child
            print node[1], child[1]
            # create the child node and add to stack
            cnode = [child[0],node[1] + [child[1]]]
            print "Add child to stack: ", cnode
            queue.push(cnode)

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    counter = 0
    # get start state
    start = problem.getStartState()
    print "start : ", start

    # first node
    node = [start,[]]

    #create the stack
    pQueue = util.PriorityQueue()
    print "Stack created"

    # keep track of visited nodes
    visited = []

    # path between start and goal node
    path = []

    # add start to stack
    pQueue.update(node, 0)

    # if the start state itself is the goal state
    if problem.isGoalState(start):
        return node[1]

    # while there is something in priority Queue
    while pQueue:
        counter+=1
        print "Iteration", counter
        # pop out an node
        node = pQueue.pop()
        print "Popped Parent " , node

        # check its already visited, if yes skip it
        if node[0] in visited:
            print "node is already visited, skip it"
            continue

        # parent node is the goal state
        print "Check goal state",node[0]
        if problem.isGoalState(node[0]):
            print "Goal found returning " , node[1]
            return node[1]

        print "Mark node Visted" , node
        # append the visited node
        visited.append(node[0])

        print "Get childs for node" , node
        # get the successors
        children = problem.getSuccessors(node[0])
        print "Found children", len(children)
        # loop through the children and add them to stack
        for child in children:
            print "found child : ", child
            print node[1], child[1]
            # create the child node and add to stack
            cnode = [child[0],node[1] + [child[1]]]
            print "Add child to stack: ", cnode
            pQueue.update(cnode, child[2])

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    counter = 0
    # get start state
    start = problem.getStartState()
    print "start : ", start

    # first node
    node = [start,[]]

    #create the stack
    pQueue = util.PriorityQueue()
    print "Stack created"

    # keep track of visited nodes
    visited = []

    # path between start and goal node
    path = []

    # add start to stack
    pQueue.update(node, 0)

    # if the start state itself is the goal state
    if problem.isGoalState(start):
        return node[1]

    # while there is something in priority Queue
    while pQueue:
        counter+=1
        print "Iteration", counter
        # pop out an node
        node = pQueue.pop()
        print "Popped Parent " , node

        # check its already visited, if yes skip it
        if node[0] in visited:
            print "node is already visited, skip it"
            continue

        # parent node is the goal state
        print "Check goal state",node[0]
        if problem.isGoalState(node[0]):
            print "Goal found returning " , node[1]
            return node[1]

        print "Mark node Visted" , node
        # append the visited node
        visited.append(node[0])

        print "Get childs for node" , node
        # get the successors
        children = problem.getSuccessors(node[0])
        print "Found children", len(children)
        # loop through the children and add them to stack
        for child in children:
            print "found child : ", child
            print node[1], child[1]
            # create the child node and add to stack
            cnode = [child[0],node[1] + [child[1]]]
            print "Add child to stack: ", cnode
            pQueue.update(cnode, problem.getCostOfActions(cnode[1]) + heuristic(cnode[0], problem))


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
