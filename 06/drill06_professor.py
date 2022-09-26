from pico2d import *
from math import *

# 최대한 함수형으로 프로그래밍 하라.
# 조금씩 개발하고 실행해보자.
# 자주 쓰이는 블록이 있다면 함수화 하자. 
# 코드 리팩토링 과정을 거쳐서 개발하자.

# pass 키워드 : 현재 들여쓰기 탈출.
# 함수 이름과 주석으로 기능 설명을 자세히 하자.

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

def render_all(x,y):
	clear_canvas_now()
	grass.draw_now(400,30)
	character.draw_now(x,y)
	delay(0.01)

def run_circle(): #Move Circle
	print('CIRCLE')
	
	cx, cy, r = 400, 300, 200
	for degree in range(-90, 270, 5):
		x = cx + r * cos(radians(degree))
		y = cy + r * sin(radians(degree))
		render_all(x,y)

def run_rectangle(): #Move rectangle
	print('RECTANGLE')

	#Bottom Line1
	for x in range(400, 750 + 1, 10):
		render_all(x, 90)

	#Right Line
	for y in range(90, 550 + 1, 10):
		render_all(750, y)

	#Top Line
	for x in range(750, 50 - 1, -10):
		render_all(x, 550)

	#Left Line
	for y in range(550, 90 - 1, -10):
		render_all(50, y)

	#Bottom Line2
	for x in range(50, 400 + 1, 10):
		render_all(x, 90)	

while(True):
	run_circle()
	run_rectangle()
	#break

close_canvas()
