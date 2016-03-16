from Node import Node
import math
import sys
class AI:
    root = None
    priorityMap = {} # Assigns weight to each node based on depth and children per node
    moveMap = {} # possible moves for each node
    def __init__(self,r):
        self.root = r
        print(self.moveMap)
    # @RN March 15 2016
    # Sets priority for each node based on depth / children of node
    # Nodes without children that are lower in the tree are prioritized higher than higher nodes with children
    def generatePriorityMap(self, root,depth=0):
        if root:
            self.priorityMap[root.ID] = (depth / (len(root.children) + 1))
            for ids, child in root.children.items():
                self.generatePriorityMap(child,depth+1)

    # @RN March 15 2016
    # Generates possible moves for each node based segmented by an angle
    def generateMoveMap(self, root, radius, degree=10, segments=0,radian=False):
        if not radian:
            degree = math.radians(degree)
        if segments == 0:
            segments = int(round(2*math.pi / degree,0))
        if root:
            self.moveMap[root.ID] = []
            for i in range(segments):
                self.moveMap[root.ID].append((round(root.x + radius*math.cos(i*degree),0),round(root.y +
                    radius*math.sin(i*degree),0)))
            for ids, child in root.children.items():
                self.generateMoveMap(child,radius,degree,segments,radian)

    #returns the value of a move
    #these nodes are NOT game nodes, they are gamestates. 
    def minimax(board, depth, pnum):
        if depth == 0 or len(node.children) == 0:
            return heuristic(board)

        if pnum == 0: #max
            bestvalue = sys.float_info.max
            for move in moveMap: #probably wrong
                value = minimax(move, depth - 1, 1)
                bestvalue = max(value, bestvalue)
        else: #min
            bestvalue = sys.float_info.min
            for move in moveMap: #ditto
                value = minimax(move, depth - 1, 0)
                bestvalue = min(bestvalue, value)
        return value

    #bs is a board state (a list of roots)
    def heuristic(bs):
        return 0

    #thebs is the current boar state
    def getMove(thebs, depth, pnum):
        bestMove = None
        bestMoveValue = sys.float_info.min
        for move in moveMap: #might be wrong
            value = minimax(thebs, depth, pnum)
            if value >= bestMoveValue:
                bestMoveValue = value
                bestMove = move
        return bestMove