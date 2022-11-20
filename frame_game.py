from frame_main import *
from PIL import Image,ImageTk
import random
import sys

win_game = Frame(win,background=COLOR1,width=WIDTH,height=HEIGHT)
#win_game=Frame(win)

GAME_INIT_DEFAULT_WIDTH = 700    
GAME_INIT_DEFAULT_HEIGHT = 500
GAME_SPEED = 250 
SPACE_SIZE = 50
BODY_PARTS_AT_INIT = 3
SNAKE_COLOR = "#00FF00"
FOOD_COLOR = "red"
BG_COLOR = "black"
DEBUG_INFO = False
GAME_STATE = 'running'
GAME_HIGH_SCORE = 0
GAME_LIVE_SCORE = 0
GAME_HIGH_SCORE_FILE_NAME = "high.score"
DIRECTION = 'right'

img= (Image.open("fruit.png"))
resized_image= img.resize((50,50), Image.ANTIALIAS)
new_image= ImageTk.PhotoImage(resized_image)


def print_verbose(toprint):
    if DEBUG_INFO:
        print(toprint)

class Snek:
    def __init__(self,x,y,canvas_game):
        self.body_size = BODY_PARTS_AT_INIT
        self.coordinates = []
        self.squares = []

        for i in range(0, BODY_PARTS_AT_INIT):
            self.coordinates.append([0, 0])

        for x, y in self.coordinates:
            square = canvas_game.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tag="snake")
            self.squares.append(square)

class Food:
    def __init__(self,canvas_game):
        x = random.randint(0, (GAME_INIT_DEFAULT_WIDTH / SPACE_SIZE)-1) * SPACE_SIZE
        y = random.randint(0, (GAME_INIT_DEFAULT_HEIGHT / SPACE_SIZE) - 1) * SPACE_SIZE
        self.coordinates = [x, y]
        canvas_game.create_image(x+25, y+25,image=new_image, tag='food')

def inc_speed(amount_to_inc):
    global GAME_SPEED
    GAME_SPEED+=amount_to_inc
    print_verbose(GAME_SPEED)

def next_turn(snek, food, canvas_game, label):
    x, y = snek.coordinates[0]

    if GAME_STATE == 'running':
        if DIRECTION == "up":
            y -= SPACE_SIZE
        elif DIRECTION == "down":
            y += SPACE_SIZE
        elif DIRECTION == "left":
            x -= SPACE_SIZE
        elif DIRECTION == "right":
            x += SPACE_SIZE

        snek.coordinates.insert(0, (x, y))
        print_verbose(snek.coordinates[0])
        print_verbose("SPEED = {}".format(GAME_SPEED))
        square = canvas_game.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)
        snek.squares.insert(0, square)
        print_verbose("Inserted square")
        if x == food.coordinates[0] and y == food.coordinates[1]:
            global GAME_LIVE_SCORE
            global GAME_HIGH_SCORE
            GAME_LIVE_SCORE += 1
            if GAME_LIVE_SCORE > GAME_HIGH_SCORE:
                high_score_file_write(str(GAME_LIVE_SCORE))
            label.config(text="Score:{} High Score: {}".format(GAME_LIVE_SCORE,GAME_HIGH_SCORE))
            # inc_speed(-10)
            canvas_game.delete("food")
            food = Food(canvas_game)

        else:
            del snek.coordinates[-1]
            canvas_game.delete(snek.squares[-1])
            del snek.squares[-1]

        if collision_check(snek):
            game_over(canvas_game)

        else:
            win.after(GAME_SPEED, next_turn, snek, food, canvas_game, label)
    else:
        win.after(GAME_SPEED, next_turn, snek, food, canvas_game, label)

def switch_direction(DIRECTION_param):

    global DIRECTION

    if DIRECTION_param == 'left':
        if DIRECTION != 'right':
            DIRECTION = DIRECTION_param
    elif DIRECTION_param == 'right':
        if DIRECTION != 'left':
            DIRECTION = DIRECTION_param
    elif DIRECTION_param == 'up':
        if DIRECTION != 'down':
            DIRECTION = DIRECTION_param
    elif DIRECTION_param == 'down':
        if DIRECTION != 'up':
            DIRECTION = DIRECTION_param

def collision_check(snek):

    x, y = snek.coordinates[0]

    if x < 0 or x >= GAME_INIT_DEFAULT_WIDTH:
        print_verbose("X = {} , SNAKE COORDS = {}".format(x,snek.coordinates[0]))
        return True
    elif y < 0 or y >= GAME_INIT_DEFAULT_HEIGHT:
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

def game_over(canvas_game):
    canvas_game.delete(ALL)
    canvas_game.create_text(canvas_game.winfo_width()/2, canvas_game.winfo_height()/2, font=('consolas',70), text="GAME OVER", fill="red", tag="gameover")
    GAME_LIVE_SCORE =0
    #win.bind('<'+PAUSE.get()+'>',lambda event: win.mainloop())

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

def speed_hack(snake):
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

def return_home():
    SCREEN.set('HOME')

def on_enter(e):
    e.widget['background'] = COLOR3

def on_leave(e):
    e.widget['background'] = COLOR2

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



def run_game(win_game):

    check_first_launch()
    high_score_file_read()

    button_home=Button(win_game, text='BACK', font=(FONT1, 8), width=10, height=2, command=return_home, bg=COLOR2)
    button_home.place(x=5, y=5) 

    label = Label(win_game, text="Score:{} High Score:{}".format(GAME_LIVE_SCORE,GAME_HIGH_SCORE), font=("Comic Sans MS", 30),bg=COLOR1)
    label.place(x=150, y=25)

    
    canvas_game = Canvas(win_game, bg='black', height=HEIGHT-100, width=WIDTH, highlightthickness=0)
    canvas_game.place(x=0,y=100)

    win.update()

    window_width = win.winfo_width()
    window_height = win.winfo_height()
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()

    x = int((screen_width/2) - (window_width/2))
    y = int((screen_height/2) - (window_height/2))

    snake = Snek(x,y,canvas_game)
    food = Food(canvas_game)

    win.bind('<'+LEFT.get()+'>', lambda event: switch_direction('left'))
    win.bind('<'+RIGHT.get()+'>', lambda event: switch_direction('right'))
    win.bind('<'+UP.get()+'>', lambda event: switch_direction('up'))
    win.bind('<'+DOWN.get()+'>', lambda event: switch_direction('down'))
    win.bind('<'+PAUSE.get()+'>', lambda event: key())
    win.bind('<j>',lambda event: speed_hack(snake))
    
    button_home.bind('<Enter>', on_enter)
    button_home.bind('<Leave>', on_leave)

    next_turn(snake, food, canvas_game, label)
