import heapq
from array_functions import flatten, get_neighbors

def a_star_search(initial_state, goal_state):
    """A* Search Algorithm for 8-puzzle using misplaced tiles heuristic."""
    # Convert 2D arrays to 1D for easier handling and comparison
    # This allows us to work with flat lists instead of nested arrays
    start = flatten(initial_state)
    goal = flatten(goal_state)
    
    # Early termination: if we're already at the goal, no moves needed
    if start == goal:
        return [], 0  # Empty path, 0 moves
    
    # Create neighbors function that returns (neighbor, cost) pairs
    def neighbors_fn(state):
        # Get all possible states
        neighbors = get_neighbors(state)  
        return [(neighbor, 1) for neighbor in neighbors]  

    # Call the generic A* algorithm with our specific functions
    path = a_star_generic(start, goal, neighbors_fn, misplaced_tiles_heuristic)
    
    # Handle case where no solution exists
    if path is None:
        return None, -1  
    
    # Return the solution path and number of moves (path length - 1)
    return path, len(path) - 1  

def a_star_generic(start, goal, neighbors_fn, heuristic_fn):
    """Generic A* Search Algorithm."""
    # We use a min-heap so the node with lowest f-score is always popped first
    frontier = [(0, start)]
    
    # g_score: actual cost from start to each node
    g_score = {tuple(start): 0}
    
    # came_from: parent dictionary for reconstructing the solution path
    # it maps each node to its parent in the optimal path
    came_from = {}
    states_explored = 0  # Counter for performance analysis
    
    # Main A* search loop
    while frontier:
        # Pop the node with lowest f-score from priority queue
        _, current = heapq.heappop(frontier)
        current_tuple = tuple(current)  # Convert to tuple for hashing
        states_explored += 1
        
        # Check if we've reached the goal
        if current == goal:
            # Reconstruct the solution path by following parent pointers
            path = []
            while current_tuple in came_from:
                path.append(current)
                current = came_from[current_tuple]
                current_tuple = tuple(current)
            path.append(start)  # Add the starting node
            return path[::-1]  # Reverse to get path from start to goal
        
        # Explore all neighbors of the current node
        for neighbor, cost in neighbors_fn(current):
            neighbor_tuple = tuple(neighbor)  # Convert to tuple for hashing
            
            # Calculate tentative g-score (cost from start through current to neighbor)
            tentative_g = g_score[current_tuple] + cost
            
            # Update if we found a better path to this neighbor
            if neighbor_tuple not in g_score or tentative_g < g_score[neighbor_tuple]:
                g_score[neighbor_tuple] = tentative_g  # Update best known cost
                f_score = tentative_g + heuristic_fn(neighbor, goal)  # Calculate f-score
                heapq.heappush(frontier, (f_score, neighbor))  # Add to priority queue
                came_from[neighbor_tuple] = current  # Record parent for path reconstruction
    
    return None  # No path found (shouldn't happen with solvable 8-puzzle)

def misplaced_tiles_heuristic(state, goal):
    """Heuristic function: number of misplaced tiles."""
    return sum(1 for i in range(len(state)) if state[i] != goal[i] and state[i] != 0)
