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


