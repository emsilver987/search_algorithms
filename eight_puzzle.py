import random
from breadth_first_search import breadth_first_search
from a_star_search import a_star_search

goalState = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

random.seed(10)

def main():
    i = 12
    for test_num in range(3):
        random.seed(i)
        initalState = generateRandomState()
        outputState(initalState)
        
        # Test BFS
        path_bfs, count_bfs = breadth_first_search(initalState, goalState)
        print(f"Number of moves using BFS: {count_bfs}")
        
        # Test A*
        path_astar, count_astar = a_star_search(initalState, goalState)
        print(f"Number of moves using A*: {count_astar}")
        
        print(f"Test {test_num + 1} completed\n")
        i += 5


def generateRandomState():
    """Generate a random solvable 8-puzzle state"""
    # Start with the goal state
    goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    
    # Make random moves from the goal state to ensure solvability
    current = [row[:] for row in goal]  # Deep copy
    moves = random.randint(10, 50)  # Random number of moves
    
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
    
    return current

def outputState(state):
    print("\nInitial State")
    for row in state:
        print(row)

if __name__ == "__main__":
    main()