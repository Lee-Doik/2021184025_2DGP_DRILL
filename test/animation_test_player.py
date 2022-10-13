from pico2d import *

def handle_events():
    global running
    global dir
    global height
    global behavior
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir += 1
                behavior = 64
            elif event.key == SDLK_LEFT:
                dir -= 1
                behavior = 0
            elif event.key == SDLK_UP:
                height += 1
            elif event.key == SDLK_DOWN:
                height -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir -= 1
                behavior = 0
            elif event.key == SDLK_LEFT:
                dir += 1
                behavior = 64
            elif event.key == SDLK_UP:
                height -= 1
            elif event.key == SDLK_DOWN:
                height += 1
    pass

open_canvas()
grass = load_image('grass.png')
character = load_image('player_run_10x2.png')

running = True
x, y = 50,90
frame = 0
dir = 0
height = 0
behavior = 64

while running:
    clear_canvas()
    grass.draw(400,30)
    character.clip_draw(frame * 88, behavior * 1, 88, 64, x ,  y)
    update_canvas()

    handle_events()
    frame = (frame + 1) % 8
    x += dir * 20
    y += height * 20
    delay(0.05)


close_canvas()
