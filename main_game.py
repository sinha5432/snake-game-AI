from tkinter import *


def snake(event):
    x = 0  # Default
    y = 0
    if event.char == "w":
        y = -10

    if event.char == "a":
        x = -10

    if event.char == "s":
        y = 10

    if event.char == "d":
        x = 10

    field.move(rect, x, y)


if __name__ == "__main__":
    root = Tk()
    root.title("Snake")
    root["width"] = 400
    root["height"] = 400

    field = Canvas(root)
    rect = field.create_rectangle(10, 20, 30, 40)
    field.grid(row=0, column=0)

    root.bind("<Key>", snake)
    root.mainloop()

