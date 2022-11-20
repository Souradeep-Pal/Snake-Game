from frame_main import *
from frame_home import *
from frame_options import *
from frame_game import *

SCREEN.set('HOME')


def update_frame(var=0, index=0, mode=0):    
    global win_home, win_options, win_game
    
    if SCREEN.get() == 'HOME':
        for item in win_game.winfo_children():
            item.destroy()
        win_home.place(x=0, y=0)
        display_home(win_home)
    else:
        win_home.place_forget()

    if SCREEN.get() == 'OPTIONS':
        win_options.place(x=0, y=0)
        display_options(win_options)
    else:   
        win_options.place_forget()

    if SCREEN.get() == 'NEW GAME':
        win_game.place(x=0,y=0)
        GAME_LIVE_SCORE=0
        run_game(win_game)
    else:
        win_game.place_forget()


update_frame()

SCREEN.trace("w", update_frame)

win.mainloop()


