from point import Point
from cell import Cell
import time

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self.cells = []

        self.create_cells()

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
        self.draw_cell()


    def draw_cell(self):
        for col in self.cells:
            for cell in col:
                cell.draw()
                self.animate()


    def animate(self):
        if not self.win:
            return
        self.win.redraw()
        time.sleep(.05)

