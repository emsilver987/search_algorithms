import heapq
from array_functions import flatten, get_neighbors

def a_star_search(initial_state, goal_state):
    """
    A* Search Algorithm for 8-puzzle using misplaced tiles heuristic.
    
    :param initial_state: 2D array representing initial puzzle state
    :param goal_state: 2D array representing goal puzzle state
    :return: (path, count) tuple where path is list of states and count is number of moves
    """
    # Convert 2D arrays to 1D for easier handling
    start = flatten(initial_state)
    goal = flatten(goal_state)
    
    if start == goal:
        return [], 0  # Already at goal
    
    # Create neighbors function that returns (neighbor, cost) pairs
    def neighbors_fn(state):
        neighbors = get_neighbors(state)
        return [(neighbor, 1) for neighbor in neighbors]  # Each move costs 1
    
    # Create heuristic function
    def heuristic_fn(state):
        return misplaced_tiles_heuristic(state, goal)
    
    # Call the generic A* algorithm
    path = a_star_generic(start, goal, neighbors_fn, heuristic_fn)
    
    if path is None:
        return None, -1  # No solution found
    
    return path, len(path) - 1  # Return path and count

def a_star_generic(start, goal, neighbors_fn, heuristic_fn):
    """
    Generic A* Search Algorithm.

    :param start: Starting node
    :param goal: Goal node
    :param neighbors_fn: Function that takes a node and returns (neighbor, cost) pairs
    :param heuristic_fn: Function that takes a node and returns heuristic estimate to goal
    :return: Path from start to goal as a list of nodes, or None if no path
    """
    # Priority queue for frontier (min-heap of (f_score, node))
    frontier = [(0, start)]
    
    # Cost from start to each node
    g_score = {tuple(start): 0}
    
    # Parent dictionary for reconstructing path
    came_from = {}
    states_explored = 0
    
    while frontier:
        _, current = heapq.heappop(frontier)
        current_tuple = tuple(current)
        states_explored += 1
        
        if current == goal:
            # Reconstruct path
            path = []
            while current_tuple in came_from:
                path.append(current)
                current = came_from[current_tuple]
                current_tuple = tuple(current)
            path.append(start)
            return path[::-1]
        
        for neighbor, cost in neighbors_fn(current):
            neighbor_tuple = tuple(neighbor)
            tentative_g = g_score[current_tuple] + cost
            if neighbor_tuple not in g_score or tentative_g < g_score[neighbor_tuple]:
                g_score[neighbor_tuple] = tentative_g
                f_score = tentative_g + heuristic_fn(neighbor)
                heapq.heappush(frontier, (f_score, neighbor))
                came_from[neighbor_tuple] = current
    
    return None  # No path found

def misplaced_tiles_heuristic(state, goal):
    """
    Heuristic function: number of misplaced tiles.
    
    :param state: Current state as 1D list
    :param goal: Goal state as 1D list
    :return: Number of tiles in wrong positions
    """
    return sum(1 for i in range(len(state)) if state[i] != goal[i] and state[i] != 0)
