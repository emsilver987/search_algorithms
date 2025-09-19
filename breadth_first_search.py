from collections import deque
from array_functions import flatten, get_neighbors

def breadth_first_search(initial_state, goal_state):
    """Find path from initial state to goal state using BFS"""
    # Convert 2D arrays to 1D for easier handling
    initial = flatten(initial_state)
    goal = flatten(goal_state)
    
    if initial == goal:
        return [], 0  # Empty path, 0 moves
    
    queue = deque([(initial, [])])  # (state, path)
    visited = {tuple(initial)}
    states_explored = 0
    
    while queue:
        current, path = queue.popleft()
        states_explored += 1
        
        if current == goal:
            return path, len(path)  # Return path and count
        
        for neighbor in get_neighbors(current):
            neighbor_tuple = tuple(neighbor)
            if neighbor_tuple not in visited:
                visited.add(neighbor_tuple)
                queue.append((neighbor, path + [neighbor]))
    
    return None, -1  # No solution found


def eval_state(state, goal):
    """Count how many positions match the goal state"""
    return sum(1 for i in range(len(state)) if state[i] == goal[i])