import random

class GameBoard:
    def __init__(self, rows, cols, board=None):
        self.rows = rows
        self.cols = cols
        if board:
            self.board = board
        else:
            self.board = [[' ' for _ in range(cols)] for _ in range(rows)]
        self.start = None
        self.stop = None
        self.obstacles = []

    def generate_board(self):
        self.generate_start_stop()
        self.generate_obstacles()

    def generate_start_stop(self):
        if self.start is None:
            self.start = (random.randint(0, self.rows - 1), 0)
            self.board[self.start[0]][self.start[1]] = 'A'
        if self.stop is None:
            self.stop = (random.randint(0, self.rows - 1), self.cols - 1)
            self.board[self.stop[0]][self.stop[1]] = 'B'

    def generate_obstacles(self):
        num_obstacles = random.randint(3, (self.rows * self.cols) // 4)
        for _ in range(num_obstacles):
            obstacle = (random.randint(0, self.rows - 1), random.randint(1, self.cols - 2))
            self.obstacles.append(obstacle)
            self.board[obstacle[0]][obstacle[1]] = 'X'

    def print_board(self):
        for row in self.board:
            print(' '.join(row))

    def is_valid_move(self, row, col):
        if row < 0 or row >= self.rows or col < 0 or col >= self.cols:
            return False
        if self.board[row][col] == 'X':
            return False
        return True

    def move_up(self):
        current_pos = self.get_current_position()
        new_pos = (current_pos[0] - 1, current_pos[1])
        self.move_to_new_position(new_pos)

    def move_down(self):
        current_pos = self.get_current_position()
        new_pos = (current_pos[0] + 1, current_pos[1])
        self.move_to_new_position(new_pos)

    def move_left(self):
        current_pos = self.get_current_position()
        new_pos = (current_pos[0], current_pos[1] - 1)
        self.move_to_new_position(new_pos)

    def move_right(self):
        current_pos = self.get_current_position()
        new_pos = (current_pos[0], current_pos[1] + 1)
        self.move_to_new_position(new_pos)

    def get_current_position(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.board[i][j] == 'A':
                    return (i, j)
        return None

    def move_to_new_position(self, new_pos):
        if self.is_valid_move(new_pos[0], new_pos[1]):
            current_pos = self.get_current_position()
            self.board[current_pos[0]][current_pos[1]] = ' '
            self.board[new_pos[0]][new_pos[1]] = 'A'

    def is_at_end(self):
        current_pos = self.get_current_position()
        return current_pos == self.stop

    def play_game(self):
        current_pos = self.start
        while not self.is_at_end():
            self.print_board()
            direction = input("Enter direction (up, down, left, right): ")
            if direction == 'up':
                new_pos = (current_pos[0] - 1, current_pos[1])
            elif direction == 'down':
                new_pos = (current_pos[0] + 1, current_pos[1])
            elif direction == 'left':
                new_pos = (current_pos[0], current_pos[1] - 1)
            elif direction == 'right':
                new_pos = (current_pos[0], current_pos[1] + 1)
            else:
                print("Invalid direction!")
                continue

            if self.is_valid_move(new_pos[0], new_pos[1]):
                self.board[current_pos[0]][current_pos[1]] = ' '
                self.board[new_pos[0]][new_pos[1]] = 'A'
                current_pos = new_pos
            else:
                print("Invalid move!")

        self.print_board()
        print("Congratulations, you reached the destination!")
        
if __name__ == '__main__':
    game = GameBoard(5, 5)
    game.generate_board()

    print("Welcome to the game!")
    print("Instructions:")
    print("Enter 'up' to move up")
    print("Enter 'down' to move down")
    print("Enter 'left' to move left")
    print("Enter 'right' to move right")
    print("Try to reach the destination 'B' from the starting point 'A' without hitting the obstacles 'X'")
    print()

    game.play_game()
