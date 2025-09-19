import random
from breadth_first_search import breadth_first_search
from a_star_search import a_star_search

# Goal state is a nested array. Each element of goal state is a row and each element within is an element within that row
goalState = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

# Setting random seed so that the result can be mimicked over and over again but still "random"
random.seed(12)

def main():
    # i = 12 is random and not important
    i = 122
    for iteration in range(10):
        # Changes the seed so we will get 3 different arrays generated
        random.seed(i) 
        initalState = generateRandomState()
        outputState(initalState)
        
        # BFS and output
        path_bfs, count_bfs = breadth_first_search(initalState, goalState)
        print(f"Number of moves using BFS: {count_bfs}")
        
        # A* and ouput
        path_astar, count_astar = a_star_search(initalState, goalState)
        print(f"Number of moves using A*: {count_astar}")
        
        # Show that each iteration is different in console output
        print(f"Iteration {iteration + 1} completed\n")

        # the integer 5 means nothing, just responsible for altering the seed
        i += 12


def generateRandomState():
    """Generate a random solvable 8-puzzle state"""
    # Start with the goal state
    goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    
    # Make random moves from the goal state to ensure solvability, deep copy
    current = [row[:] for row in goal]
    # Random number of moves
    moves = random.randint(10, 50)  
    
    # 
    for _ in range(moves):
        # Find empty space
        empty_row, empty_col = 0, 0
        for i in range(3):
            for j in range(3):
                if current[i][j] == 0:
                    empty_row, empty_col = i, j
                    break
        
        # Get possible moves
        possible_moves = []
        if empty_row > 0:  # Can move up
            possible_moves.append((empty_row - 1, empty_col))
        if empty_row < 2:  # Can move down
            possible_moves.append((empty_row + 1, empty_col))
        if empty_col > 0:  # Can move left
            possible_moves.append((empty_row, empty_col - 1))
        if empty_col < 2:  # Can move right
            possible_moves.append((empty_row, empty_col + 1))
        
        # Pick a random move
        if possible_moves:
            new_row, new_col = random.choice(possible_moves)
            # Swap
            current[empty_row][empty_col], current[new_row][new_col] = current[new_row][new_col], current[empty_row][empty_col]
    # current is our array that we will use as inital ranodm state
    return current

def outputState(state):
    # Simple print statement
    print("\nInitial State")
    for row in state:
        print(row)

# Entry Point
if __name__ == "__main__":
    main()