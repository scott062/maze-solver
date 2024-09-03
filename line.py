class Line:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def draw(self, canvas, fill_color):
        a,b = self.a, self.b
        canvas.create_line(a.x, a.y, b.x, b.y, fill=fill_color, width=2)
