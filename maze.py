from point import Point
from cell import Cell
import time
import random

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self.cells = []

        if seed:
            random.seed(seed)

        self.create_cells()
        self.break_entrance_and_exit()
        self.break_walls_r(0, 0)
        self.reset_cells_visited()

    def create_cells(self):
        top_left_x = self.x1
        top_left_y = self.y1
        x_offset = self.cell_size_x
        y_offset = self.cell_size_y

        for c in range(self.num_cols):
            col = []
            for r in range(self.num_rows):
                top_l = Point(top_left_x, top_left_y)
                bot_r = Point(top_left_x + x_offset, top_left_y + y_offset)
                col.append(Cell(self.win, top_l, bot_r))
                top_left_y += y_offset # Increment the y axis while within same column
            self.cells.append(col)
            top_left_y = self.y1 # Reset y axis when starting new column
            top_left_x += x_offset # Increment y axis only when starting new column

        for col in self.cells:
            for cell in col:
                self.draw_cell(cell)

    def draw_cell(self, cell):
        cell.draw()
        self.animate()

    def animate(self):
        if not self.win:
            return
        self.win.redraw()
        time.sleep(.01)

    def break_entrance_and_exit(self):
        start = self.cells[0][0]
        end = self.cells[-1][-1]
        start.has_top = False
        end.has_bottom = False
        self.draw_cell(start)
        self.draw_cell(end)

    def break_walls_r(self, i, j):
        current = self.cells[i][j]
        current.visited = True

        neighbors = [
            ("above", [i, j-1]),
            ("next_right", [i+1, j]),
            ("below", [i, j+1]),
            ("next_left", [i-1, j]),
        ]

        while True:
            to_visit = []
            for n in neighbors:
                col = n[1][0]
                row = n[1][1]
                if self.num_cols > col > -1 and self.num_rows > row > -1:
                    if not self.cells[col][row].visited:
                        to_visit.append(n)

            if not to_visit: # Nowhere valid to move
                self.draw_cell(current)
                return

            chosen_direction = random.choice(to_visit)
            dir = chosen_direction[0]
            col = chosen_direction[1][0]
            row = chosen_direction[1][1]
            target = self.cells[col][row]

            if dir == "above":
                current.has_top = False
                target.has_bottom = False
            if dir == "next_right":
                current.has_right = False
                target.has_left = False
            if dir == "below":
                current.has_bottom = False
                target.has_top = False
            if dir == "next_left":
                current.has_left = False
                target.has_right = False

            self.break_walls_r(col, row)

    def reset_cells_visited(self):
        for col in self.cells:
            for row in col:
                row.visited = False




