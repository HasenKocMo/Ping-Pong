from pygame import *
win_width = 600
win_height = 500
back = (200, 255, 255)
window = display.set_mode((win_width, win_height))

display.set_caption('Ping-Pong')
window.fill(back)

clock = time.Clock()
FPS = 60
game = True

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    display.update()
    clock.tick(FPS)