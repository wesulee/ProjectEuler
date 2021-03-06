'''
In the 5 by 5 matrix below, the minimal path sum from the top left to the
bottom right, by only moving to the right and down, is indicated in bold red
and is equal to 2427.

    131  673  234  103   18
    201   96  342  965  150
    630  803  746  422  111
    537  699  497  121  956
    805  732  524   37  331

Find the minimal path sum, in matrix.txt (right click and
'Save Link/Target As...'), a 31K text file containing a 80 by 80 matrix, 
from the top left to the bottom right by only moving right and down.
'''

class Matrix(object):
    def __init__(self, matrix):
        self.matrix = matrix[:]
        self.length_x = len(matrix[0]) - 1
        self.length_y = len(matrix) - 1
        self.solvedDict = self.genSolvedDict(self.length_x + 1, self.length_y + 1)

    def genSolvedDict(self, length_x, length_y):
        L = [(n, [False] * length_y) for n in xrange(length_x)]
        return dict(L)

    def getWeight(self, coord):
        return self.matrix[coord[1]][coord[0]]

    def getWeights(self, coords):
        return [self.getWeight(coord) for coord in coords]
    
    def markSolved(self, coord, weight):
        self.solvedDict[coord[0]][coord[1]] = weight
        
    def isSolved(self, coord):
        return self.solvedDict[coord[0]][coord[1]] != False

    def getBranches(self, coord):
        '''return list of unsolved nodes'''
        nodes = []
        # check right
        if not coord[0] >= self.length_x:
            nodes.append((coord[0] + 1, coord[1]))
        # check down
        if not coord[1] >= self.length_y:
            nodes.append((coord[0], coord[1] + 1))
        # filter out solved nodes
        unsolved_nodes = []
        for coord in nodes:
            if not self.isSolved(coord):
                unsolved_nodes.append(coord)
        return unsolved_nodes


def getMatrix(path='matrix.txt'):
    '''put matrix into list'''
    with open(path, 'r') as f:
        matrix = map(lambda x: x.split(','), f.readlines())
        return [map(int, n) for n in matrix]


def best_node(branches):
    return min(branches, key=lambda x: x[1])


def min_index(weights):
    minimum = weights[0]
    min_index = 0
    for i in xrange(1, len(weights)):
        if weights[i] < minimum:
            minimum = weights[i]
            min_index = i
    return min_index


def findPath(matrix):
    end = (matrix.length_x, matrix.length_y)
    solved = [((0, 0), matrix.getWeight((0, 0)))]  # solved nodes ((x,y), weight)
    while solved[-1][0] != end:
        branches = []
        remove_nodes = []
        for coord, weight in solved:
            node_branch = matrix.getBranches(coord)
            if not node_branch:
                remove_nodes.append((coord, weight))
                continue
            minimum = node_branch[min_index(matrix.getWeights(node_branch))]
            branches.append((minimum, weight + matrix.getWeight(minimum)))
        solved.append(best_node(branches))
        matrix.markSolved(solved[-1][0], solved[-1][1])
        while remove_nodes:
            solved.remove(remove_nodes.pop(0))
    return solved[-1][1]


print findPath(Matrix(getMatrix('matrix.txt')))
