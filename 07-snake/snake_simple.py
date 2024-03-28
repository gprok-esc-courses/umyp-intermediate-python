from tkinter import Tk, Canvas


class Snake:
    def __init__(self):
        self.x = 195
        self.y = 195
        self.size = 10
        self.direction = None
        self.body_parts = [[195, 205],
                           [195, 215],
                           [195, 225]]

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


class Window:
    def __init__(self):
        self.window = Tk()
        self.canvas = Canvas(self.window, width=400, height=400)
        self.canvas.grid(row=0, column=0)
        self.window.bind('<Key>', self.key_event)
        self.snake = Snake()
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
        self.draw()
    def start_game(self):
        self.window.mainloop()

    def draw(self):
        self.canvas.delete("all")
        s = self.snake
        self.canvas.create_rectangle(s.x, s.y, s.x + s.size, s.y + s.size, fill="black")
        for part in self.snake.body_parts:
            self.canvas.create_rectangle(part[0], part[1], part[0] + s.size, part[1] + s.size, fill="green")


if __name__ == "__main__":
    game = Window()
    game.start_game()