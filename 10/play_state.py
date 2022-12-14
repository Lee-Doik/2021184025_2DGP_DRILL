from pico2d import *
import game_framework
import title_state
import item_state
import add_delete_state
from random import randint

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

class Boy:
    def __init__(self):
        self.x, self.y = randint(100, 700), 90
        self.frame = randint(0, 7)
        self.dir = 1 # 오른쪽
        self.image = load_image('animation_sheet.png')
        self.item = None
        self.ball_image = load_image('ball21x21.png')
        self.big_ball_image = load_image('ball41x41.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += self.dir * 2

        if self.x > 800:
            self.x = 800
            self.dir = -1

        elif self.x < 0:
            self.x = 0
            self.dir = 1

    def draw(self):
        if self.item == 'Ball':
            self.ball_image.draw(self.x + 10 , self.y + 40)
        elif self.item == 'Big_Ball':
            self.big_ball_image.draw(self.x + 10, self.y + 50)

        if self.dir == 1:
            self.image.clip_draw(self.frame*100, 100, 100, 100, self.x, self.y)
        else:
            self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)

def handle_events():
    #global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.change_state(title_state)
            elif event.key == SDLK_i:
                game_framework.push_state(item_state)
            elif event.key == SDLK_b:
                game_framework.push_state(add_delete_state)

team = [None]
boy_num = 1
grass = None
running = None

def enter():
    global team, grass, running, boy_num
    team = [Boy() for i in range(boy_num)]
    grass = Grass()
    running = True

def exit():
    global team, grass
    del team
    del grass

def update():
    global team
    for boy in team:
        boy.update()

def draw():
    clear_canvas()
    draw_world()
    update_canvas()

def draw_world():
    global team
    grass.draw()
    for boy in team:
        boy.draw()

def PLUS_boy():
    global boy_num
    boy_num += 1

def MINUS_boy():
    global boy_num
    if boy_num < 1:
        boy_num = 1
    else:
        boy_num -= 1

def pause():
    pass

def resume():
    pass
