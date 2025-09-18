import unittest
from operations import moveLeft

class TestMoveLeft(unittest.TestCase):
    
    def test_moveLeft_basic(self):
        """Test basic left move functionality"""
        state = [[1, 2, 3], [4, 0, 6], [7, 8, 9]]
        emptyIndex = [1, 1] 
        choiceIndex = [1, 0]  
        
        original_state = [row[:] for row in state]
        
        moveLeft(state, emptyIndex, choiceIndex)
        
        # After move: empty space should be at [1,0] and 4 should be at [1,1]
        expected = [[1, 2, 3], [0, 4, 6], [7, 8, 9]]
        self.assertEqual(state, expected)
    
    def test_moveLeft_corner_case(self):
        """Test moving from top-left corner"""
        state = [[0, 2, 3], [4, 5, 6], [7, 8, 9]]
        emptyIndex = [0, 0]  # empty at top-left
        choiceIndex = [0, 1]  # element to move at [0,1]
        
        moveLeft(state, emptyIndex, choiceIndex)
        
        expected = [[2, 0, 3], [4, 5, 6], [7, 8, 9]]
        self.assertEqual(state, expected)
    
    def test_moveLeft_bottom_row(self):
        """Test moving in bottom row"""
        state = [[1, 2, 3], [4, 5, 6], [7, 0, 9]]
        emptyIndex = [2, 1]  # empty at [2,1]
        choiceIndex = [2, 0]  # element to move at [2,0]
        
        moveLeft(state, emptyIndex, choiceIndex)
        
        expected = [[1, 2, 3], [4, 5, 6], [0, 7, 9]]
        self.assertEqual(state, expected)
    
    def test_moveLeft_same_position(self):
        """Test moving when empty and choice are the same position"""
        state = [[1, 2, 3], [4, 0, 6], [7, 8, 9]]
        emptyIndex = [1, 1]
        choiceIndex = [1, 1]  # same position
        
        original_state = [row[:] for row in state]
        moveLeft(state, emptyIndex, choiceIndex)
        
        # Should remain unchanged
        self.assertEqual(state, original_state)

if __name__ == '__main__':
    unittest.main()
