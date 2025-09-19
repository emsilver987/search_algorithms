import unittest
from array_functions import get_neighbors, flatten
from breadth_first_search import breadth_first_search, eval_state
from a_star_search import a_star_search, misplaced_tiles_heuristic

class TestArrayFunctions(unittest.TestCase):
    
    def test_flatten_2d_to_1d(self):
        """Test flattening 2D array to 1D"""
        array_2d = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 0]
        result = flatten(array_2d)
        self.assertEqual(result, expected)
    
    def test_flatten_already_1d(self):
        """Test flattening when already 1D"""
        array_1d = [1, 2, 3, 4, 5, 6, 7, 8, 0]
        result = flatten(array_1d)
        self.assertEqual(result, array_1d)
    
    def test_get_neighbors_basic(self):
        """Test getting neighbors from middle position"""
        state = [1, 2, 3, 4, 0, 6, 7, 8, 5]  # Empty at position 4
        neighbors = get_neighbors(state)
        
        # Should have 4 neighbors (up, down, left, right)
        self.assertEqual(len(neighbors), 4)
        
        # Check that all neighbors are valid states
        for neighbor in neighbors:
            self.assertEqual(len(neighbor), 9)
            self.assertEqual(neighbor.count(0), 1)  # Exactly one empty space
    
    def test_get_neighbors_corner(self):
        """Test getting neighbors from corner position"""
        state = [0, 2, 3, 4, 5, 6, 7, 8, 1]  # Empty at position 0 (top-left)
        neighbors = get_neighbors(state)
        
        # Should have 2 neighbors (right, down)
        self.assertEqual(len(neighbors), 2)

class TestSearchAlgorithms(unittest.TestCase):
    
    def test_bfs_simple_case(self):
        """Test BFS with a simple 1-move case"""
        initial = [[1, 2, 3], [4, 0, 6], [7, 8, 5]]
        goal = [[1, 2, 3], [4, 6, 0], [7, 8, 5]]
        
        path, count = breadth_first_search(initial, goal)
        
        self.assertIsNotNone(path)
        self.assertEqual(count, 1)
    
    def test_astar_simple_case(self):
        """Test A* with a simple 1-move case"""
        initial = [[1, 2, 3], [4, 0, 6], [7, 8, 5]]
        goal = [[1, 2, 3], [4, 6, 0], [7, 8, 5]]
        
        path, count = a_star_search(initial, goal)
        
        self.assertIsNotNone(path)
        self.assertEqual(count, 1)
    
    def test_bfs_vs_astar_same_result(self):
        """Test that BFS and A* give same results"""
        initial = [[1, 2, 3], [4, 0, 6], [7, 8, 5]]
        goal = [[1, 2, 3], [4, 6, 0], [7, 8, 5]]
        
        path_bfs, count_bfs = breadth_first_search(initial, goal)
        path_astar, count_astar = a_star_search(initial, goal)
        
        self.assertEqual(count_bfs, count_astar)
        self.assertEqual(len(path_bfs), len(path_astar))

class TestHeuristics(unittest.TestCase):
    
    def test_eval_state_perfect_match(self):
        """Test eval_state with perfect match"""
        state = [1, 2, 3, 4, 5, 6, 7, 8, 0]
        goal = [1, 2, 3, 4, 5, 6, 7, 8, 0]
        
        result = eval_state(state, goal)
        self.assertEqual(result, 9)  # All 9 positions match
    
    def test_eval_state_no_match(self):
        """Test eval_state with no matches"""
        state = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        goal = [1, 2, 3, 4, 5, 6, 7, 8, 0]
        
        result = eval_state(state, goal)
        self.assertEqual(result, 0)  # No positions match
    
    def test_misplaced_tiles_heuristic(self):
        """Test misplaced tiles heuristic"""
        state = [1, 2, 3, 4, 0, 6, 7, 8, 5]
        goal = [1, 2, 3, 4, 5, 6, 7, 8, 0]
        
        result = misplaced_tiles_heuristic(state, goal)
        self.assertEqual(result, 2)  # Tiles 5 and 8 are misplaced (excluding empty space)
    
    def test_misplaced_tiles_perfect_match(self):
        """Test misplaced tiles heuristic with perfect match"""
        state = [1, 2, 3, 4, 5, 6, 7, 8, 0]
        goal = [1, 2, 3, 4, 5, 6, 7, 8, 0]
        
        result = misplaced_tiles_heuristic(state, goal)
        self.assertEqual(result, 0)  # No misplaced tiles

if __name__ == '__main__':
    unittest.main()
