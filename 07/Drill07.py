from pico2d import *

open_canvas()

grass = load_image('grass.png')
sprite = load_image('sprite_sheet_ex.png')
sprite2 = load_image('sprite_sheet_ex2.png')

global frame
frame = 0

def walking_man(x):
    global frame
    clear_canvas()
    grass.draw(400,30)
    sprite.clip_draw(9 + frame * 22, 157, 17, 32, x, 100, 60, 110)
    update_canvas()
    frame = (frame + 1) % 4
    delay(0.1)
    get_events()

def jumping_man(x, y):
    global frame
    clear_canvas()
    grass.draw(400,30)
    sprite.clip_draw(9 + frame * 23, 111, 22, 32, x, y, 60, 110)
    update_canvas()
    frame = (frame + 1) % 3
    delay(0.1)
    get_events()

def death_man(x):
    global frame
    clear_canvas()
    grass.draw(400, 30)
    sprite.clip_draw(9 + frame * 24, 14, 28, 28, x, 100, 60, 110)
    update_canvas()
    frame = (frame + 1) % 4
    delay(0.2)
    get_events()

def run_dragon(x):
    global frame
    clear_canvas()
    grass.draw(400, 30)
    sprite2.clip_draw(33 + frame * 47, 660, 42, 48, x, 100, 90, 110)
    update_canvas()
    frame = (frame + 1) % 10
    delay(0.06)
    get_events()

def flip_dragon(x):
    global frame
    clear_canvas()
    grass.draw(400, 30)
    sprite2.clip_draw(50 + frame * 50, 615, 43, 44, x, 100, 90, 110)
    update_canvas()
    frame = (frame + 1) % 6
    delay(0.08)
    get_events()

x, y = 0, 0

while True:
    while x < 800:
        walking_man(x)
        x += 10
    x = 0

    while x < 800:
        jumping_man(x, 100 + y * 30)
        x += 20
        y = (y + 1) % 3
    x = 400

    while x > 300:
        death_man(x)
        x -= 25
    x = 0

    while x < 800:
        run_dragon(x)
        x += 15
    x = 0

    while x < 800:
        flip_dragon(x)
        x += 15
    x = 0

close_canvas()