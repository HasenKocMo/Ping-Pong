from pygame import *
win_width = 600
win_height = 500
back = (200, 255, 255)
window = display.set_mode((win_width, win_height))

display.set_caption('Ping-Pong')
window.fill(back)

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y < 500:
            self.rect.y += self.speed
        if keys[K_DOWN] and self.rect.y > win_width - 80:
            self.rect.y -= self.speed

player1 = Player('racket.png', 5, win_height - 100, 80, 100, 10)
player2 = Player('racket.png', 10, win_height - 80, 80, 100, 10)

clock = time.Clock()
FPS = 60
game = True

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    player1.update()
    player2.update()

    player1.reset()
    player2.reset()

    display.update()
    clock.tick(FPS)
