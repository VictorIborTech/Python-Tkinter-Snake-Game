from tkinter import *
import random

GAME_WIDTH = 700
GAME_HEIGHT = 500
SPEED = 180
SPACE_SIZE = 20
BODY_PART = 3
SNAKE_COLOR =  "green"
FOOD_COLOR =  "red"
BACKGROUND_COLOR =  "black"


class Snake:
    def __init__(self):
        self.bodypart = BODY_PART

        self.coordinate = [ ]
        self.squares = [ ]

        for i in range(0, BODY_PART):
            self.coordinate.append([0, 0])

        for x, y in self.coordinate:
            square = canvas.create_rectangle(x, y,
                                             x + SPACE_SIZE,
                                             y + SPACE_SIZE,
                                             fill = SNAKE_COLOR,
                                             tag ="snake")
            self.squares.append(square)



class Food:
    def __init__(self):
        x = random.randint(0, (GAME_WIDTH/SPACE_SIZE) - 1) * SPACE_SIZE
        y = random.randint(0, (GAME_HEIGHT/SPACE_SIZE) - 1) * SPACE_SIZE

        self.coordinate = [x, y]

        canvas.create_oval(x, y,
                           x + SPACE_SIZE,
                           y + SPACE_SIZE,
                           fill= FOOD_COLOR,
                           tag="food")

def  next_turn(snake, food):
    x , y = snake.coordinate[0]

    if direction == "up":
        y  = y - SPACE_SIZE

    elif direction == "down":
        y  = y + SPACE_SIZE

    elif direction == "left":
        x  = x - SPACE_SIZE

    elif direction == "right":
        x  = x + SPACE_SIZE

    snake.coordinate.insert(0, (x, y))

    square = canvas.create_rectangle(x, y,
                                     x + SPACE_SIZE,
                                     y + SPACE_SIZE,
                                     fill = SNAKE_COLOR)
    snake.squares.insert(0, square)

    # Changing the score by formatting it previous score when snake eat
    if x == food.coordinate[0] and y == food.coordinate[1]:

        global  score

        score = score + 1

        label.config(text = "Score:{}".format(score))

        canvas.delete("food")

        food = Food()

    else:
        # deleting the last square or the snake botton when it moves and dont eat
        del snake.coordinate[-1]

        canvas.delete(snake.squares[-1])

        del snake.squares[-1]


    # Checking collision so snake cant go out of screen
    if check_collision(snake):
        game_over()
    else:
        window.after(SPEED,  next_turn,  snake,  food)


def check_collision(snake):
    x , y = snake.coordinate[0]

    if  x< 0 or x >= GAME_WIDTH:
        return True
    elif y < 0 or y >= GAME_WIDTH:
        return True

    for body_part in snake.coordinate[1: ]:
        if x == body_part[0] and y == body_part[1]:
            return True


def change_direction(new_direction):

    global  direction

    if new_direction == 'left':
        if direction != 'right':
            direction = new_direction

    elif new_direction == 'right':
        if direction != 'left':
            direction = new_direction

    elif new_direction == 'up':
        if direction != 'down':
            direction = new_direction

    elif new_direction == 'down':
        if direction != 'up':
            direction = new_direction


def game_over():

    canvas.delete(ALL)

    canvas.create_text(canvas.winfo_width() / 2,  canvas.winfo_height() / 2,
                       font = ('consolas', 70),
                       text = "Game Over",
                       fill = "red",
                       tag = "gameover")



window = Tk()

window.title("Snake Game Python")
window.resizable(False, False)

score = 0
direction = 'down'

label = Label(window,
              text = "Score:{}".format(score),
              font = ('consolas', 40)
              )
label.pack()

canvas = Canvas(window, bg= BACKGROUND_COLOR,
                width = GAME_WIDTH,
                height = GAME_HEIGHT)
canvas.pack()


window.update()

window_width = window.winfo_width()
window_heigth = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width/ 2) - (window_width /2))
y = int((screen_height/ 2) - (window_heigth /2))

window.geometry(f"{window_width}x{window_heigth}+{x}+{y}")

window.bind('<Left>', lambda event: change_direction('left'))
window.bind('<Right>', lambda event: change_direction('right'))
window.bind('<Up>', lambda event: change_direction('up'))
window.bind('<Down>', lambda event: change_direction('down'))

snake= Snake()
food= Food()


next_turn(snake, food)
window.mainloop()