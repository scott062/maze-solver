from point import Point
from line import Line

class Cell:
    def __init__(self, win, top_left, bottom_right, has_top=True, has_right=True, has_bottom=True, has_left=True):
        self.top_left = top_left # Point()
        self.bottom_right = bottom_right # Point()
        self.has_top = has_top
        self.has_right = has_right
        self.has_bottom = has_bottom
        self.has_left = has_left
        self.win = win
        self.visited = False


    def draw(self):
        if not self.win:
            return
        top_left, bottom_right = self.top_left, self.bottom_right
        top_right = Point(bottom_right.x, top_left.y)
        bottom_left = Point(top_left.x, bottom_right.y)
        win = self.win
        default = "white"
        color = "purple"

        win.draw_line(Line(top_left, top_right), default if self.has_top else color)
        win.draw_line(Line(top_right, bottom_right), default if self.has_right else color)
        win.draw_line(Line(bottom_left, bottom_right), default if self.has_bottom else color)
        win.draw_line(Line(top_left, bottom_left), default if self.has_left else color)


    def get_center(self):
        x = self.top_left.x + ((self.bottom_right.x - self.top_left.x) / 2)
        y = self.bottom_right.y + ((self.top_left.y - self.bottom_right.y) / 2)
        return Point(x,y)


    def draw_move(self, to_cell, undo=False):
        color = "gray" if undo else "red"
        self.win.draw_line(Line(self.get_center(), to_cell.get_center()), color)

