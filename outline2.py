# ************************************
# Python Snake
# ************************************
from tkinter import *
import random
import sys

# IMPORTANT: Make sure that both GAME_WIDTH and GAME_HEIGHT are
# divisible by SPACE_SIZE (50 in this case)
GAME_INIT_DEFAULT_WIDTH = 700    #fallback in case argument doesnt match requirment OR no arg is passed
GAME_INIT_DEFAULT_WIDTH = 500
GAME_SPEED = 150 #reduce for higher speed
SPACE_SIZE = 50
BODY_PARTS_AT_INIT = 3
SNAKE_COLOR = "#00FF00"
FOOD_COLOR = "#FF0000"
BG_COLOR = "#000000"
DEBUG_INFO = False
GAME_STATE = 'running'
GAME_HIGH_SCORE = 0
GAME_LIVE_SCORE =0
GAME_HIGH_SCORE_FILE_NAME = "high.score"


def print_verbose(toprint):
    if DEBUG_INFO:
        print(toprint)

class Snek:
    def __init__(self,x,y):
        self.body_size = BODY_PARTS_AT_INIT
        self.coordinates = []
        self.squares = []

        for i in range(0, BODY_PARTS_AT_INIT):
            self.coordinates.append([0, 0])

        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tag="snake")
            self.squares.append(square)

class Food:

    def __init__(self):

        x = random.randint(0, (GAME_INIT_DEFAULT_WIDTH / SPACE_SIZE)-1) * SPACE_SIZE
        y = random.randint(0, (GAME_INIT_DEFAULT_WIDTH / SPACE_SIZE) - 1) * SPACE_SIZE
        self.coordinates = [x, y]

        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag="food")

def inc_speed(amount_to_inc):
    global GAME_SPEED
    GAME_SPEED+=amount_to_inc
    print_verbose(GAME_SPEED)

def next_turn(snek, food):

    x, y = snek.coordinates[0]
    
    if GAME_STATE == 'running':
        if direction == "up":
            y -= SPACE_SIZE
        elif direction == "down":
            y += SPACE_SIZE
        elif direction == "left":
            x -= SPACE_SIZE
        elif direction == "right":
            x += SPACE_SIZE

        snek.coordinates.insert(0, (x, y))
        print_verbose(snek.coordinates[0])
        print_verbose("SPEED = {}".format(GAME_SPEED))
        square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)
        snek.squares.insert(0, square)
        print_verbose("Inserted square")
        if x == food.coordinates[0] and y == food.coordinates[1]:
            global GAME_LIVE_SCORE
            global GAME_HIGH_SCORE
            GAME_LIVE_SCORE += 1
            if GAME_LIVE_SCORE > GAME_HIGH_SCORE:
                high_score_file_write(str(GAME_LIVE_SCORE))
            label.config(text="Score:{} High Score: {}".format(GAME_LIVE_SCORE,GAME_HIGH_SCORE))
            inc_speed(-10)
            canvas.delete("food")
            food = Food()

        else:

            del snek.coordinates[-1]

            canvas.delete(snek.squares[-1])

            del snek.squares[-1]

        if collision_check(snek):
            game_over()

        else:
            root.after(GAME_SPEED, next_turn, snek, food)
    else:
        root.after(GAME_SPEED,next_turn,snek,food)

def switch_direction(direction_param):

    global direction

    if direction_param == 'left':
        if direction != 'right':
            direction = direction_param
    elif direction_param == 'right':
        if direction != 'left':
            direction = direction_param
    elif direction_param == 'up':
        if direction != 'down':
            direction = direction_param
    elif direction_param == 'down':
        if direction != 'up':
            direction = direction_param

def collision_check(snek):

    x, y = snek.coordinates[0]

    if x < 0 or x >= GAME_INIT_DEFAULT_WIDTH:
        print_verbose("X = {} , SNAKE COORDS = {}".format(x,snek.coordinates[0]))
        return True
    elif y < 0 or y >= GAME_INIT_DEFAULT_WIDTH:
        return True

    for body_part in snek.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            return True

    return False

def key():
    global GAME_STATE
    if GAME_STATE == 'running':
        GAME_STATE='pause'
    else:
        GAME_STATE = 'running'
        print_verbose("Called unpause")

def game_over():
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2,
                       font=('consolas',70), text="GAME OVER", fill="red", tag="gameover")

    root.bind("<Return>",lambda event: root.mainloop())

def high_score_file_write(amount):
    with open(GAME_HIGH_SCORE_FILE_NAME,"r+") as file:
        file.seek(0)
        file.write(str(amount))
        file.truncate()

def high_score_file_read():
    global GAME_HIGH_SCORE
    file = open(GAME_HIGH_SCORE_FILE_NAME,"r")
    hs = file.readlines()
    GAME_HIGH_SCORE = int(hs[0])

def speed_hack():
    global GAME_SPEED
    GAME_SPEED = 150
    snake.body_size -= 1

def check_first_launch():
    import os.path
    if os.path.isfile(GAME_HIGH_SCORE_FILE_NAME) == False:
        print_verbose("First game launch detected. Creating a high score file")
        file = open(GAME_HIGH_SCORE_FILE_NAME,'w')
        file.write('0')
        file.close()

for iteration,arg in enumerate(sys.argv):
    if arg == "-v":
        DEBUG_INFO = True
    if arg == "-r":
        ARG_HEIGHT = int(sys.argv[iteration+1])
        ARG_WIDTH = int(sys.argv[iteration+2])

        H_REM = float(ARG_HEIGHT %50)
        W_REM = float(ARG_WIDTH % 50)
        print_verbose("H_REM: {} % 50 = {} and W_REM: {} % 50 = {}".format(ARG_HEIGHT,H_REM,ARG_WIDTH,W_REM))
        if H_REM != 0 or W_REM != 0:
            print("Provided height unusable by game. Using defaults")
        else:
            GAME_INIT_DEFAULT_WIDTH = int(sys.argv[iteration + 1])
            GAME_INIT_DEFAULT_HEIGHT = int(sys.argv[iteration + 2])
    if arg == "-h":
        GAME_STATE = 'pause'
        print("------------------------------------------------")
        print("[+] Welcome to snake game")
        print("[+] Game has been paused to show instructions.")
        print("[+] Press <Enter> to pause/unpause the game")
        print("[+] Use the arrow keys to navigate")
        print("[+] If the game is going to fast use the cheat button (a) to slow the game down :)")
        print("------------------------------------------------")

check_first_launch()
high_score_file_read()


root = Tk()
root.title("Snake game")
root.resizable(False, False)

pause_var = StringVar()
direction = 'right'
label = Label(root, text="Score:{} High Score:{}".format(GAME_LIVE_SCORE,GAME_HIGH_SCORE), font=('consolas', 40))
label.pack()

canvas = Canvas(root, bg=BG_COLOR, height=GAME_INIT_DEFAULT_WIDTH, width=GAME_INIT_DEFAULT_WIDTH)
canvas.pack()

root.update()

window_width = root.winfo_width()
window_height = root.winfo_height()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))

root.geometry(f"{window_width}x{window_height}+{x}+{y}")

root.bind('<Left>', lambda event: switch_direction('left'))
root.bind('<Right>', lambda event: switch_direction('right'))
root.bind('<Up>', lambda event: switch_direction('up'))
root.bind('<Down>', lambda event: switch_direction('down'))
root.bind('<Escape>', lambda event: key())
root.bind('a',lambda event: speed_hack())
snake = Snek(x,y)
food = Food()

next_turn(snake, food)
root.mainloop()