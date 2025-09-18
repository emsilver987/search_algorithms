
import array


def breadth_first_search(initialState, goalState):
    goalState_flat = decompose_array(goalState)
    initialState_flat = decompose_array(initialState)
    return eval_bfs(initialState_flat, goalState_flat)

def eval_bfs(initial, goal):
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