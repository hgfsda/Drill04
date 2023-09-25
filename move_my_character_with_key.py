from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 800, 600
open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
character = load_image('character.png')

def handle_events():
    global running

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False

running = True
x = 800 // 2
y = 600 // 2
frame = 0
dir_x, dir_y, dir_check = 0, 0, 0

while running:
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    if(dir_check == 0): character.clip_draw(frame*60, 0, 60, 60, x, y, 80, 80)
    elif(dir_check == 1): character.clip_draw(frame*60, 60, 60, 60, x, y, 80, 80)
    elif(dir_check == 2): character.clip_draw(frame*60, 120, 60, 60, x, y, 80, 80)
    elif(dir_check == 3): character.clip_draw(frame*60, 180, 60, 60, x, y, 80, 80)
    update_canvas()
    handle_events()
    frame = (frame + 1) % 8
    delay(0.08)

close_canvas()