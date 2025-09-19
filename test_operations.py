import unittest

class TestSwapIndicies(unittest.TestCase):
    
    def test_swap_basic(self):
        """Test basic swap functionality"""
        state = [['A', 'B', 'C'], ['D', 0, 'E'], ['F', 'G', 'H']]
        emptyIndex = [1, 1]  # empty space position
        choiceIndex = [0, 1]  # element 'B' position
        
        swapIndicies(state, emptyIndex, choiceIndex)
        
        # After swap: empty space moves to [0,1], 'B' moves to [1,1]
        expected = [['A', 0, 'C'], ['D', 'B', 'E'], ['F', 'G', 'H']]
        self.assertEqual(state, expected)
    
    def test_swap_corner(self):
        """Test swapping from corner position"""
        state = [[0, 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']]
        emptyIndex = [0, 0]  # empty at top-left
        choiceIndex = [1, 0]  # element 'D' below empty
        
        swapIndicies(state, emptyIndex, choiceIndex)
        
        # 'D' moves up to [0,0], empty moves down to [1,0]
        expected = [['D', 'B', 'C'], [0, 'E', 'F'], ['G', 'H', 'I']]
        self.assertEqual(state, expected)
    
    def test_swap_middle(self):
        """Test swapping in middle of grid"""
        state = [['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 0, 'I']]
        emptyIndex = [2, 1]  # empty at [2,1]
        choiceIndex = [1, 1]  # element 'E' at [1,1]
        
        swapIndicies(state, emptyIndex, choiceIndex)
        
        # 'E' moves down to [2,1], empty moves up to [1,1]
        expected = [['A', 'B', 'C'], ['D', 0, 'F'], ['G', 'E', 'I']]
        self.assertEqual(state, expected)
    
    def test_swap_same_position(self):
        """Test that no change occurs when indices are the same"""
        state = [['A', 'B', 'C'], ['D', 0, 'E'], ['F', 'G', 'H']]
        emptyIndex = [1, 1]
        choiceIndex = [1, 1]  # same position
        
        original_state = [row[:] for row in state]
        swapIndicies(state, emptyIndex, choiceIndex)
        
        # Should remain unchanged
        self.assertEqual(state, original_state)
        
if __name__ == '__main__':
    unittest.main()
