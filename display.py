from tkinter import *


class Display:

    def __init__(self, width, height):

        self.pixel_side = 100

        self.size_x = width * self.pixel_side
        self.size_y = height * self.pixel_side

        self.master = Tk()

    def draw(self):

        w = Canvas(self.master, width=self.size_x, height=self.size_y)
        w.create_rectangle(0, 0, self.pixel_side, self.pixel_side, fill="blue", outline="blue")
        w.create_rectangle(20, 20, self.pixel_side, self.pixel_side, fill="red", outline="blue")
        w.pack()
        self.master.mainloop()
