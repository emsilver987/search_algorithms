

def swapIndicies(state, emptyIndex, choiceIndex):
    temp = state[emptyIndex[0]][emptyIndex[1]]
    state[emptyIndex[0]][emptyIndex[1]] = state[choiceIndex[0]][choiceIndex[1]]
    state[choiceIndex[0]][choiceIndex[1]] = temp
    return state
