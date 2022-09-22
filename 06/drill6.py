from pico2d import *
from math import *

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

cnt = 0

if (cnt % 2 == 0):	
	x = 400
	y = 90
	while (x < 770):
		clear_canvas_now()
		grass.draw_now(400,30)
		character.draw_now(x,90)

		x = x + 2

		delay(0.001)

	while(y < 570):
		clear_canvas_now()
		grass.draw_now(400,30)
		character.draw_now(770,y)

		y = y + 2

		delay(0.001)

	while (x > 30):
		clear_canvas_now()
		grass.draw_now(400,30)
		character.draw_now(x,y)

		x = x - 2

		delay(0.001)

	while (y > 90):
		clear_canvas_now()
		grass.draw_now(400,30)
		character.draw_now(30,y)

		y = y - 2

		delay(0.001)

	while (x < 400):
		clear_canvas_now()
		grass.draw_now(400,30)
		character.draw_now(x,90)

		x = x + 2

		delay(0.001)

	cnt += 1

	
else:
	circle = 0
	theta = 0
	while(circle < 180):
		clear_canvas_now()
		grass.draw_now(400,30)
		character.draw_now((400 + 250 * math.cos(math.radians(theta))),(300 + 250 * math.sin(math.radians(theta))))
		theta = theta + 2
		delay(0.01)

	cnt += 1
