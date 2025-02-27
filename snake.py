from tkinter import *

class snake:

    def __init__(self, size, speed):

        self.speed = speed

        self.size = size
        self.movement = [
            [-1, 0],  # up
            [1, 0],  # down
            [0, 1],  # right
            [0, -1],  # left
        ]

        # 0: up
        # 1: right
        # 2: down
        # 3: left

        self.direction = 0

    def main_loop():
        pass

