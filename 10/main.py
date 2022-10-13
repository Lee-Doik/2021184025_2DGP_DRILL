import pico2d
import logo_state
import play_state

states = [logo_state, play_state] # 모듈의 변수화.
pico2d.open_canvas()
for state in states:
    state.enter()
    # game main loop code
    while state.running:
        state.handle_events()
        state.update()
        state.draw()
        pico2d.delay(0.05)
# finalization code
state.exit()
pico2d.close_canvas()
