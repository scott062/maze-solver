from tkinter import Tk, Canvas


class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.__root = Tk()
        self.__root.title = "Scott's Maze"
        self.__canvas = Canvas(self.__root, bg="purple", height=self.height, width=self.width)
        self.__canvas.pack(fill="both", expand=1)
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()
    
    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()

    def close(self):
        self.__running = False

    def draw_line(self, line, fill_color="white"):
        line.draw(self.__canvas, fill_color)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def draw(self, canvas, fill_color):
        a,b = self.a, self.b
        canvas.create_line(a.x, a.y, b.x, b.y, fill=fill_color, width=2)


class Cell:
    def __init__(self, win, top_left, bottom_right, has_top=True, has_right=True, has_bottom=True, has_left=True):
        self.top_left = top_left # Point()
        self.bottom_right = bottom_right # Point()
        self.has_top = has_top
        self.has_right = has_right
        self.has_bottom = has_bottom
        self.has_left = has_left
        self.win = win

    def draw(self):
        top_left, bottom_right = self.top_left, self.bottom_right
        top_right = Point(bottom_right.x, top_left.y)
        bottom_left = Point(top_left.x, bottom_right.y)
        win = self.win
        if self.has_top: 
            win.draw_line(Line(top_left, top_right))
        if self.has_right:
            win.draw_line(Line(top_right, bottom_right))
        if self.has_bottom:
            win.draw_line(Line(bottom_left, bottom_right))
        if self.has_left:
            win.draw_line(Line(top_left, bottom_left))

    def get_center(self):
        x = self.top_left.x + ((self.bottom_right.x - self.top_left.x) / 2)
        y = self.bottom_right.y + ((self.top_left.y - self.bottom_right.y) / 2)
        return Point(x,y)


    def draw_move(self, to_cell, undo=False):
        color = "gray" if undo else "red"
        self.win.draw_line(Line(self.get_center(), to_cell.get_center()), color)        


def main():
    win = Window(800, 600)
    a = Cell(win, Point(50,50), Point(100,100))
    b = Cell(win, Point(150,150), Point(200,200))
    a.draw()
    b.draw()
    a.draw_move(b, True)
    win.wait_for_close()

main()
