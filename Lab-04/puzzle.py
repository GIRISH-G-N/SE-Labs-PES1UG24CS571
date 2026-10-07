import random


class Puzzle:
    def __init__(self, size=4):
        self.size = size
        self.board = self.make_board()

    def solved_board(self):
        tiles = list(range(1, self.size * self.size)) + [0]
        return [tiles[r * self.size:(r + 1) * self.size] for r in range(self.size)]

    def make_board(self):
        # Start from the solved board and apply only legal blank moves,
        # so every generated board is guaranteed to be solvable.
        self.board = self.solved_board()
        opposite = {"w": "s", "s": "w", "a": "d", "d": "a"}
        while True:
            last = None
            steps = 0
            while steps < self.size * self.size * 20:
                direction = random.choice("wasd")
                if last and direction == opposite[last]:
                    continue  # don't immediately undo the previous move
                if self.move(direction):
                    last = direction
                    steps += 1
            if not self.solved():
                return self.board

    def blank_pos(self):
        for r in range(self.size):
            for c in range(self.size):
                if self.board[r][c] == 0:
                    return r, c

    def move(self, direction):
        r, c = self.blank_pos()
        dr, dc = {"w": (-1, 0), "s": (1, 0), "a": (0, -1), "d": (0, 1)}[direction]
        nr, nc = r + dr, c + dc
        if not (0 <= nr < self.size and 0 <= nc < self.size):
            return False
        self.board[r][c], self.board[nr][nc] = self.board[nr][nc], self.board[r][c]
        return self.board[r][c]

    def solved(self):
        return sum(self.board, []) == list(range(1, self.size * self.size)) + [0]