from collections import deque

def breadth_first_search(initial_state, goal_state):
    """Find path from initial state to goal state using BFS"""
    # Convert 2D arrays to 1D for easier handling
    initial = flatten(initial_state)
    goal = flatten(goal_state)
    
    if initial == goal:
        return [], 0  # Empty path, 0 moves
    
    queue = deque([(initial, [])])  # (state, path)
    visited = {tuple(initial)}
    
    while queue:
        current, path = queue.popleft()
        
        if current == goal:
            return path, len(path)  # Return path and count
        
        for neighbor in get_neighbors(current):
            neighbor_tuple = tuple(neighbor)
            if neighbor_tuple not in visited:
                visited.add(neighbor_tuple)
                queue.append((neighbor, path + [neighbor]))
    
    return None, -1  # No solution found

def get_neighbors(state):
    """Get all possible next states by moving the empty space"""
    neighbors = []
    zero_pos = state.index(0)
    row, col = zero_pos // 3, zero_pos % 3
    
    # Try all 4 directions
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_state = state[:]
            new_zero_pos = new_row * 3 + new_col
            new_state[zero_pos], new_state[new_zero_pos] = new_state[new_zero_pos], new_state[zero_pos]
            neighbors.append(new_state)
    
    return neighbors

def flatten(array_2d):
    """Convert 2D array to 1D list"""
    if len(array_2d) == 9:  # Already 1D
        return array_2d
    return [element for row in array_2d for element in row]

def eval_state(state, goal):
    """Count how many positions match the goal state"""
    return sum(1 for i in range(len(state)) if state[i] == goal[i])