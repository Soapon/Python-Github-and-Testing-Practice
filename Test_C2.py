#Unit Tests for Checkers_2 module
# >_<
#1/7/2026

from Checkers_2 import (
    initialize_board,
    move_piece,
    switch_player,
    promote_to_king
)

# Based on the video provided
class TestInitializeBoard:
    def test_board_creation(self):
        """Test that board is initialized correctly"""
        board = initialize_board()
        
        # Check white pieces are in rows 0-2
        assert board[(0, 1)] == 'W'
        assert board[(1, 0)] == 'W'
        assert board[(2, 1)] == 'W'
        
        # Check black pieces are in rows 5-7
        assert board[(5, 0)] == 'B'
        assert board[(6, 1)] == 'B'
        assert board[(7, 0)] == 'B'
        
        # Check middle rows are empty
        assert (3, 0) not in board
        assert (4, 1) not in board
    
    def test_board_size(self):
        #Test that board has correct number of pieces
        board = initialize_board()
        assert len(board) == 24  # 12 pieces per player to start with


class TestMovePiece:
    def test_simple_move(self):
        #Test a simple move without capturing
        board = {(2, 1): 'W', (3, 2): 'B'}
        move_piece(board, (2, 1), (3, 0))
        
        assert (2, 1) not in board
        assert board[(3, 0)] == 'W'
    
    def test_capture_move(self):
        #Test capturing an opponent's piece
        board = {(2, 1): 'W', (3, 2): 'B'}
        move_piece(board, (2, 1), (4, 3))
        
        assert (2, 1) not in board
        assert (3, 2) not in board  # Captured piece removed
        assert board[(4, 3)] == 'W'
#Trynna see if the players flip!
class TestSwitchPlayer:
    def test_switch_from_white(self):
        assert switch_player('W') == 'B'
    
    def test_switch_from_black(self):
         assert switch_player('B') == 'W'


class TestPromoteToKing:
    def test_white_promotion(self):
        #test white piece promotion to king
        board = {(7, 1): 'W'}
        promote_to_king(board, (8, 2))
        assert board[(7, 1)] == 'M'
        #now for black
    def test_black_promotion(self):
        board = {(0, 1): 'B'}
        promote_to_king(board, (1, 2))
        assert board[(0, 1)] == 'P'
