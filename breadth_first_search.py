
import array

# Start from the initial scrambled board.
# Explore all states one move away.
# Then explore all states two moves away.
# Continue level by level until the goal state is found

def breadth_first_search(initialState, goalState):
    goalState_flat = decompose_array(goalState)
    initialState_flat = decompose_array(initialState)
    return eval_state(initialState_flat, goalState_flat)

def eval_state(initial, goal):
    # return number of squares that match goal state
    count = 0
    for i in range(len(initial)):
        if initial[i] == goal[i]:
            count += 1
    return count

def decompose_array(array_2d):
    result = []
    for row in array_2d:
        for element in row:
            result.append(element)
    return result

def get_neighbors(initalState):
    # 1 = Up, 2 = Down, 3 = Left, 4 = Right
    movesPossible = []
    for i in range(len(initalState)):
        if initalState[i] == 0:
            zeroIndex = i #need a more time efficent way of finding and/or storing zero index
    if zeroIndex < 6:
        movesPossible.append(1)
    if zeroIndex > 3:
        movesPossible.append(2)
    if zeroIndex != 0 or zeroIndex != 3 or zeroIndex != 6:
        movesPossible.append(3)
    if zeroIndex != 7 or zeroIndex != 5 or zeroIndex != 8:
        movesPossible.append(4)
    return movesPossible

def bfs_tree(root):
    if not root:
        return
    queue = [root]
    while queue:
        current = queue.pop(0)
        print(current.val)
        if hasattr(current, 'left') and current.left:
            queue.append(current.left)
        if hasattr(current, 'right') and current.right:
            queue.append(current.right)