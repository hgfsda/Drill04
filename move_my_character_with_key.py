from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 800, 600
open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
character = load_image('character.png')

def handle_events():
    global running, dir_x, dir_y, dir_check

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir_x += 1
                dir_check = 1
            elif event.key == SDLK_LEFT:
                dir_x -= 1
                dir_check = 2
            elif event.key == SDLK_UP:
                dir_y += 1
                dir_check = 0
            elif event.key == SDLK_DOWN:
                dir_y -= 1
                dir_check = 3
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir_x -= 1
            elif event.key == SDLK_LEFT:
                dir_x += 1
            elif event.key == SDLK_UP:
                dir_y -= 1
            elif event.key == SDLK_DOWN:
                dir_y += 1

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
    if x <= 760 and x >= 40: x += dir_x * 10
    elif x > 760: x = 760
    elif x < 40: x = 40

    if y <= 560 and y >= 40: y += dir_y * 10
    elif y > 560: y = 560
    elif y < 40: y = 40
    delay(0.08)

close_canvas()