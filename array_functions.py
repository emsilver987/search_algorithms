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