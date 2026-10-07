import time
from puzzle import Puzzle

SIZES = ("3", "4", "5")


class SlidingPuzzle:
    def __init__(self, size=4):
        self.size = size
        self.puzzle = Puzzle(self.size)
        self.moves = 0
        self.started = time.monotonic()
        self.finished = False
        self.final_time = 0

    def new_board(self, size):
        # Only the board is recreated; moves and the timer are kept.
        self.size = size
        self.puzzle = Puzzle(size)

    def choose_size(self):
        while True:
            choice = input("Choose board size (3, 4 or 5): ").strip()
            if choice in SIZES:
                self.new_board(int(choice))
                return
            print("Please enter 3, 4 or 5.")

    def elapsed(self):
        if self.finished:
            return self.final_time
        return int(time.monotonic() - self.started)

    def finish(self):
        self.finished = True
        self.final_time = int(time.monotonic() - self.started)

    def display(self):
        print()
        for row in self.puzzle.board:
            print(" ".join(f"{x or ' ':>2}" for x in row))
        print("Moves:", self.moves, " Time:", self.elapsed(), "s")

    def run(self):
        print("Sliding Puzzle - W/A/S/D moves the tile into the blank.")
        print("Type 3, 4 or 5 to change board size. Q quits.")
        self.choose_size()
        self.started = time.monotonic()
        while True:
            self.display()
            if self.finished:
                print(f"Solved in {self.moves} moves and {self.final_time} s. Game over!")
                return
            key = input("> ").strip().lower()
            if key == "q":
                return
            if key in SIZES:
                self.new_board(int(key))
                print(f"Switched to {key}x{key}. Moves and time carried over.")
                continue
            if key not in ("w", "a", "s", "d"):
                print("Use W/A/S/D, 3/4/5 or Q.")
                continue
            tile = self.puzzle.move(key)
            if tile:
                self.moves += 1
                print(f"Slid tile {tile} into the blank.")
                if self.puzzle.solved():
                    self.finish()
            else:
                print("That move is not possible. Move count unchanged.")