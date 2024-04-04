from tkinter import Tk, Canvas
import random


class Fruit:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.color = None
        self.colors = ['red', 'green', 'blue', 'yellow', 'orange', 'purple', 'pink']
        self.points = [2, 4, 1, 1, 3, 5, 6]

    def set_random_color(self):
        r = random.randint(0, len(self.colors)-1)
        self.color = self.colors[r]

    def set_coords(self, width, height):
        x = random.randint(5, width - 15)
        self.x = x - (x % 10)
        y = random.randint(5, height - 15)
        self.y = y - (y % 10)


class Snake:
    def __init__(self):
        self.x = 190
        self.y = 190
        self.size = 10
        self.direction = None
        self.body_parts = [[190, 200],
                           [190, 210],
                           [190, 220]]

    def go_up(self):
        if self.direction != 'Down':
            self.direction = 'Up'
            self.move_body_parts()
            self.y -= self.size

    def go_down(self):
        if self.direction != 'Up':
            self.direction = 'Down'
            self.move_body_parts()
            self.y += self.size

    def go_left(self):
        if self.direction != 'Right':
            self.direction = 'Left'
            self.move_body_parts()
            self.x -= self.size

    def go_right(self):
        if self.direction != 'Left':
            self.direction = 'Right'
            self.move_body_parts()
            self.x += self.size

    def move_body_parts(self):
        for i in range(len(self.body_parts)-1, 0, -1):
            self.body_parts[i][0] = self.body_parts[i - 1][0]
            self.body_parts[i][1] = self.body_parts[i - 1][1]
        self.body_parts[0][0] = self.x
        self.body_parts[0][1] = self.y

    def on_fruit(self, fruit):
        if self.x == fruit.x and self.y == fruit.y:
            self.body_parts.append([self.body_parts[-1][0], self.body_parts[-1][1]])
            return True
        else:
            return False

    def hit_side(self, width, height):
        # return true or false
        pass



class Window:
    def __init__(self):
        self.window = Tk()
        self.canvas = Canvas(self.window, width=400, height=400)
        self.canvas.grid(row=0, column=0)
        self.window.bind('<Key>', self.key_event)
        self.snake = Snake()
        self.fruit = Fruit()
        self.fruit.set_coords(400, 400)
        self.fruit.set_random_color()
        self.draw()

    def key_event(self, event):
        key = event.keysym
        if key == 'Up':
            self.snake.go_up()
        elif key == 'Down':
            self.snake.go_down()
        elif key == 'Left':
            self.snake.go_left()
        elif key == 'Right':
            self.snake.go_right()
        if self.snake.on_fruit(self.fruit):
            self.fruit.set_coords(400, 400)
            self.fruit.set_random_color()
        self.draw()

    def start_game(self):
        self.window.mainloop()

    def draw(self):
        self.canvas.delete("all")
        s = self.snake
        self.canvas.create_rectangle(s.x, s.y, s.x + s.size, s.y + s.size, fill="black")
        for part in self.snake.body_parts:
            self.canvas.create_rectangle(part[0], part[1], part[0] + s.size, part[1] + s.size, fill="green")
        f = self.fruit
        self.canvas.create_rectangle(f.x, f.y, f.x + s.size, f.y + s.size, fill=f.color)


if __name__ == "__main__":
    game = Window()
    game.start_game()