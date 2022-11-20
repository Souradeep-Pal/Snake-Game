from frame_main import *
from PIL import Image,ImageTk


win_home=Frame(win,background=COLOR1,width=WIDTH,height=HEIGHT)

img= (Image.open("home.png"))
resized_image= img.resize((WIDTH,HEIGHT), Image.ANTIALIAS)
new_image= ImageTk.PhotoImage(resized_image)


def new_game():
    SCREEN.set('NEW GAME')
    # canvas_game.delete('all')

def load_options():
    SCREEN.set('OPTIONS')

def on_enter(e):
    e.widget['background'] = COLOR3

def on_leave(e):
    e.widget['background'] = COLOR2


def display_home(win_home):
    Label(win_home, image=new_image, bd=0).place(x=0,y=0)
    Label(win_home, text="Snake Game", font=("Comic Sans MS", 40, "bold"),bg='#98b503').place(x=45,y=120)

    X=30
    button_newgame=Button(win_home, text='NEW GAME', width=50, height=3, command=new_game, bg=COLOR2, relief="raised",font=("Comic Sans MS", 8))
    button_options=Button(win_home, text='OPTIONS', width=50, height=3, command=load_options, bg=COLOR2, relief="raised",font=("Comic Sans MS", 8))
    button_exit=Button(win_home, text='EXIT', width=50, height=3, command=win.destroy, bg=COLOR2, relief="raised",font=("Comic Sans MS", 8))

    button_newgame.place(x=X, y=280)
    button_options.place(x=X, y=360)
    button_exit.place(x=X, y=440)

    button_newgame.bind('<Enter>', on_enter)
    button_newgame.bind('<Leave>', on_leave)
    button_options.bind('<Enter>', on_enter)
    button_options.bind('<Leave>', on_leave)
    button_exit.bind('<Enter>', on_enter)
    button_exit.bind('<Leave>', on_leave)

