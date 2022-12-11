from pico2d import *
from random import *
import game_world
import server


class Ball:
    image = None

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def __init__(self):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x = randint(100, 1600)
        self.y = randint(100, 1100)

    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

    def update(self):
        pass

    def handle_collision(self, other, group):
        if group == 'boy:ball':
            game_world.remove_object(self)
