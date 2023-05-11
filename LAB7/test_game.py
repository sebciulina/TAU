import pytest
from game import GameBoard

@pytest.fixture(scope="class")
def game_board(request):
    return GameBoard(5, 5)

@pytest.mark.usefixtures("game_board")
class TestGameBoardClass:
    @classmethod
    def setup_class(cls):
        print("Setting up TestGameBoardClass...")

    @classmethod
    def teardown_class(cls):
        print("Tearing down TestGameBoardClass...")

    def setup_method(self, method):
        print(f"Setting up {method.__name__}...")
        self.game_board = GameBoard(5, 5)
        self.game_board.generate_board()

    def teardown_method(self, method):
        print(f"Tearing down {method.__name__}...")

    @pytest.mark.parametrize("row, col", [(0, 0), (4, 4)])
    def test_is_valid_move(self, row, col):
        assert self.game_board.is_valid_move(row, col)

    @pytest.mark.parametrize("row, col", [(-1, 0), (5, 0), (0, -1), (0, 5)])
    def test_out_of_bounds(self, row, col):
        assert not self.game_board.is_valid_move(row, col)        

    def test_move_right(self):
        initial_pos = self.game_board.get_current_position()
        obstacle_pos = (initial_pos[0], initial_pos[1] + 1)
        if self.game_board.board[obstacle_pos[0]][obstacle_pos[1]] == 'X':
            pytest.skip("Obstacle encountered on the right")
        
        self.game_board.move_right()
        new_pos = self.game_board.get_current_position()
        assert new_pos == (initial_pos[0], initial_pos[1] + 1)

    @pytest.mark.xfail(reason="Expected failure - Invalid move")
    def test_move_left_invalid(self):
        initial_pos = self.game_board.get_current_position()
        self.game_board.move_left()
        new_pos = self.game_board.get_current_position()
        assert new_pos != initial_pos

    def test_level_completed(self):
        current_pos = self.game_board.get_current_position()
        self.game_board.stop = current_pos
        assert self.game_board.is_at_end()

    @pytest.mark.skip
    def test_duplicate_position(self):
        self.game_board.start = (0, 0)
        initial_pos = self.game_board.get_current_position()
        self.game_board.move_down()
        current_pos = self.game_board.get_current_position()

        assert current_pos != initial_pos

if __name__ == '__main__':
    pytest.main()
