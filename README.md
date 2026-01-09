# Python-Github-and-Testing-Practice
 5 improvements

 -> Remove the error that pieces are allowed to move backwards (Implemented)
 
 -> Change the indexing (0-7, 1-8) to be consistent
 
 -> Change king symbol to use lowercase and uppercase instead of different letters (Implemented)

 -> Allow players to choose who starts
 
 -> Allow players to enter coordinates in one input by using double digit numbers or letters
 

 3 functionality additions
 
 -> Adding the king piece that checkers pieces can turn into when they reach the other end. King pieces can move foreward and backwards (Implemented!)
 
 -> Add the ability to continue one's turn after capturing a piece
 
 -> New mode where both sides have one random piece missing.

 Doctesting Brainstorm (Unit Testing Implemented)
 
To implement doctesting, I would first identify the most deterministic functions where expected behavior can be clearly defined, such as switch_player, initialize_board, is_valid_move, and promote_to_king. For each of these functions, I would aim to design board states that isolate a single rule and verify return values, piece counts, or specific board positions after a move similiar to how it is done with unit testing. To make doctesting practical, I need avoid testing interactive functions like main() and instead refactor logic-heavy functions to return values rather than only mutating state.
 
 Doctest Vs. Unit Test:

Doctests are better for verifying small, deterministic behaviors, since they embed example inputs and outputs directly in docstrings. This makes them better for simple helper functions, edge cases with clear expected results. However, doctests is hard to test with complex setup or many possible paths. Unit tests, by contrast, are better suited for testing complex logic and larger systems. They scale more cleanly as a project grows and make it easier to isolate failures.
