from pygame import *
import random

window = display.set_mode((700, 500))
display.set_caption('Шутер')
background = transform.scale(image.load('galaxy.jpg'), (700, 500))
z=10
l=6
x=0
s='0'
f='0'
y=0
s1=0
f1=0
x5 = 0
UFo = sprite.Group()
BUl = sprite.Group()
font.init()
mixer.init()
kill = mixer.Sound('fire.ogg')
font1 = font.SysFont("Arial", 80)
font2 = font.SysFont("Arial", 80)
score = font2.render('Score:', True, (255, 255, 255))
score1 = font2.render(s, True, (255, 255, 255))
skip = font2.render('Skip:', True, (255, 255, 255))
skip1 = font2.render(f, True, (255, 255, 255))
win = font1.render('YOU WIN!', True, (0, 180, 0))
lose = font1.render('YOU LOSE!', True, (180, 0, 0))
class GameSprite(sprite.Sprite):
    def __init__(self, image1, x, y, size_x, size_y, speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(image1), (size_x, size_y))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update(self):
        global x5
        global x
        global y
        global kill
        x5 = self.rect.x
        if keys[K_LCTRL]:
            self.speed = 10
        if keys[K_SPACE] and y != 1:
            if x == l:
                a=self.rect.x + 33
                b=self.rect.y
                bul = BULLET('bullet.png', a, b, 5, 15, 35)
                BUl.add(bul)   
                kill.play()
                x=0
            x += 1
        if keys[K_LEFT] and self.rect.x >= 2 and y != 1 or keys[K_a] and self.rect.x >= 2 and y != 1:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x <= 628 and y != 1 or keys[K_d] and self.rect.x <= 628 and y != 1:
            self.rect.x += self.speed
        self.speed = 3
        if y == 1 or f1 >= z:
            self.rect.y = 600

class UFO(GameSprite):
    def update(self):
        global y
        global f
        global f1
        global skip1
        if y == 1 or f1 >= z:
            self.rect.y = -100
            self.speed = 0
        if self.rect.y >= 550:
            a=random.randint(2, 628)
            b=random.randint(-100, -50)
            c=random.randint(2, 4)
            self.rect.x = a
            self.rect.y = b
            if y != 1:
                self.speed = c
            f1 += 1
            f=str(f1)
            skip1 = font2.render(f, True, (255, 255, 255))
        if sprite.spritecollide(gg, UFo, False):
            y=1
        self.rect.y += self.speed

class ASTEROID(GameSprite):
        def update(self):
            pass

class BULLET(GameSprite):
        def update(self):
            global s
            global s1
            global score1
            self.rect.y -= self.speed
            if sprite.groupcollide(UFo, BUl, True, True):
                s1 += 1
                s=str(s1)
                score1 = font2.render(s, True, (255, 255, 255))
            if self.rect.y <= -50:
                self.kill()


clock=time.Clock()
FPS=100
game = True
gg = Player('rocket.png', 325, 400, 70, 100, 3)
for i in range(0, z):
    a=random.randint(2, 628)
    b=random.randint(-100, -50)
    c=random.randint(2, 4)
    ufo = UFO('ufo.png', a, b, 70, 40, c)
    UFo.add(ufo)
mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()
while game:
    keys = key.get_pressed()
    for e in event.get():
        if e.type == QUIT:
            game = False
    window.blit(background, (0, 0))
    window.blit(score, (0, 0))
    window.blit(score1, (110, 0))
    window.blit(skip, (0, 30))
    window.blit(skip1, (92, 30))
    if s == str(z):
        window.blit(win, (200, 200))
    if y == 1 or f1 >= z:
        window.blit(lose, (200, 200))
    gg.reset()
    gg.update()
    UFo.update()
    UFo.draw(window)
    BUl.update()
    BUl.draw(window)
    clock.tick(FPS)
    display.update()
