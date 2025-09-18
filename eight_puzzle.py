import random

goalState = [[1, 2, 3], [4, 5, 6], [7, 8, None]]

random.seed(42)

def main():
    state = generateRandomState()
    outputState(state)

def generateRandomState():
    state = []
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    i = 0
    random.shuffle(numbers)
    for _ in range(3):
        state.append([numbers[i],numbers[i+1],numbers[i+2]])
        i += 3
    return state

def outputState(state):
    for row in state:
        print(row)

if __name__ == "__main__":
    main()