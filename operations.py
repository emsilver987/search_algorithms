
def moveLeft(state, emptyIndex, choiceIndex):
    temp = state[emptyIndex[0]][emptyIndex[1]]
    state[emptyIndex[0]][emptyIndex[1]] = state[choiceIndex[0]][choiceIndex[1]]
    state[choiceIndex[0]][choiceIndex[1]] = temp

def moveRight(state):
    return 0 

def moveUp(state):
    return 0 

def moveDown(state):
    return 0
