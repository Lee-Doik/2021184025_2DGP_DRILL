from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1280, 1024

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
                behavior = 100
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
                behavior = 300
            elif event.key == SDLK_LEFT:
                dir += 1
                behavior = 200
            elif event.key == SDLK_UP:
                height -= 1
            elif event.key == SDLK_DOWN:
                height += 1
    pass

open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')

running = True
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
frame = 0
dir = 0
height = 0
behavior = 300

while running and 0 < x < 1280 and 0 < y 1024:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    character.clip_draw(frame * 100, behavior * 1, 100, 100, x ,  y)
    update_canvas()

    handle_events()
    frame = (frame + 1) % 8
    x += dir * 5
    y += height * 5
    delay(0.01)


close_canvas()

