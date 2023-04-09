#Создай собственный Шутер!

from pygame import *
from random import randint
win_width = 700
win_height = 500
global_miss = 0
global_score = 0
class Gamesprite(sprite.Sprite):
    def __init__(self,player_image, player_x,player_y,player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65,65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x=player_x
        self.rect.y=player_y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
class Bullet(Gamesprite):
    def update(self):
        if self.rect.y < win_height:
            self.rect.y -=2
        else:
            self.rect.y = 0
            self.rect.x - randint(1,win_width=65)
class Player(Gamesprite):
    def update(self):
        keys_pressed=key.get_pressed()
        if keys_pressed[K_LEFT] and self.rect.x>5:
            self.rect.x-=self.speed
        if keys_pressed[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x+=self.speed
    def fire(self):
        bullet = Bullet('bullet.png', self.rect.centerx, self.rect.top, 15)
        keys_pressed = key.get_pressed()
        if keys_pressed[K_SPACE] and self.rect.x >5:
            bullets.add(Bullet)
        else:
            self.rect.y = 0
            bullet.kill()
class Enemy(Gamesprite):
    def update(self):
        if self.rect.y < win_height:
            self.rect.y += 2
        else:
            self.rect.y = 0
            self.rect.x = randint(1,win_height-65)
            global global_miss
            global_miss += 1
window = display.set_mode((win_width, win_height))
display.set_caption('ИГра')
background = transform.scale(image.load('galaxy.jpg'),(win_width, win_height))
mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()
player = Player('rocket.png',5,win_height-80,4)
bullets = sprite.Group()
ufoes = sprite.Group()
ufo1 = Enemy('ufo.png',randint(1, win_width-65), 1, randint(1,5))
ufo2 = Enemy('ufo.png',randint(1, win_width-65), 1, randint(1,5))
ufo3 = Enemy('ufo.png',randint(1, win_width-65), 1, randint(1,5))
ufo4 = Enemy('ufo.png',randint(1, win_width-65), 1, randint(1,5))
ufo5 = Enemy('ufo.png',randint(1, win_width-65), 1, randint(1,5))
ufoes.add(ufo1, ufo2 , ufo3, ufo4, ufo5)
clock = time.Clock()
FPS = 60
finish = False
run = True
font.init()
font1 = font.Font(None,36)
while run:
    if finish != True:
        score = font1.render('ОЧки',  True,(255,255,255))
        bullets.draw(window)
        bullets.update()
        display.update()
        clock.tick(FPS)
        window.blit(background, (0,0))
        player.reset()
        player.update()
    for e in event.get():
        if e.type == QUIT:
            run = False