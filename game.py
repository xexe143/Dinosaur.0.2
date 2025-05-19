from random import randint
from pygame import *
from time import sleep

window = display.set_mode((700, 500))
display.set_caption('')
background = transform.scale(image.load('pon.jpg'), (700, 500))

grass = transform.scale(image.load('grass2.png'), (790, 200))
grass2 = transform.scale(image.load('grass2.png'), (790, 200))

clock = time.Clock()
FPS = 60

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x=65, size_y=65, speed=7):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.dir  = 'left'
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_d] and self.rect.x < 625:
            self.rect.x +=self.speed
        if keys_pressed[K_a] and self.rect.x > 5:
            self.rect.x -=self.speed
        if keys_pressed[K_w] and self.rect.y > 25:
            self.rect.y -=self.speed
        if keys_pressed[K_s] and self.rect.y < 150:
            self.rect.y +=self.speed
    def update2(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_RIGHT] and self.rect.x < 625:
            self.rect.x +=self.speed
        if keys_pressed[K_LEFT] and self.rect.x > 5:
            self.rect.x -=self.speed
        if keys_pressed[K_UP] and self.rect.y > 215:
            self.rect.y -=self.speed

        if keys_pressed[K_DOWN] and self.rect.y < 375:
            self.rect.y +=self.speed


hero = Player('monkey.png', 15, 150, 70, 70)
hero2 = Player('monkey.png', 15, 375, 70, 70)
       
class Enemy(GameSprite):
    def update(self):
        self.rect.x -=self.speed
        if self.rect.x < 5:
            self.rect.x = 690

q = 700
w = 700
enemies = sprite.Group()
for i in range(3):
    enemy = Enemy('bushes.png', w, 175, 50, 50, 3)
    enemies.add(enemy)
    enemy = Enemy('bushes.png', q, 400, 50, 50, 4)
    enemies.add(enemy)
    q = 700
w = 700

class Banana(GameSprite):
    def update(self):
        self.rect.x -=self.speed
        if self.rect.x < 5:
            self.rect.x = randint(400, 690)
            self.rect.y = randint(85, 135)

bananas = sprite.Group()
for i in range(2):
    banana = Banana('banana.png', randint(170, 600), randint(85, 135), 25, 25)
    bananas.add(banana)

class Bananas(GameSprite):
    def update(self):
        self.rect.x -=self.speed
        if self.rect.x < 5:
            self.rect.x = randint(400, 690)
            self.rect.y = randint(290, 425)

banan = sprite.Group()
for i in range(2):
    banana = Bananas('banana.png', randint(170, 600), randint(290, 425), 25, 25)
    banan.add(banana)

font.init()
font1 = font.SysFont('Arial', 36)    
score = 0

textscore =  font1.render('Счет:' +str(score) , 1 ,(255,255,255))

finish = True
game = True
while game == True:
    if finish == True:
        window.blit(background, (0,0))
        window.blit(grass, (0, 370))
        window.blit(grass2, (0, 145))
        enemies.update()
        enemies.draw(window)
        bananas.update()
        bananas.draw(window)
        banan.update()
        banan.draw(window)
        hero.update()
        hero2.update2()
        hero.reset()
        hero2.reset() 
        if sprite.spritecollide(hero, bananas, True):
            finish = True 
            score +=1
            textscore =  font1.render('Счет:'+ str(score) , 1 ,(255,255,255))
            banana = Banana('banana.png', randint(170, 600), randint(85, 135), 25, 25)
            bananas.add(banana)
        window.blit(textscore, ( 10, 20))
        if sprite.spritecollide(hero2, banan, True):
            finish = True 
            score +=1
            textscore =  font1.render('Счет:'+ str(score) , 1 ,(255,255,255))
            banana = Bananas('banana.png', randint(170, 600), randint(85, 135), 25, 25)
            banan.add(banana)
        window.blit(textscore, ( 10, 20))
        if sprite.spritecollide(hero2, enemies, True):
            finish = False
            window.blit(background, (0,0))
            text_final = font1.render('Вы проиграли((', 1 ,(255,255,255))
            window.blit(text_final, ( 240, 250))
        if sprite.spritecollide(hero, enemies, True):
            finish = False
            window.blit(background, (0,0))
            text_final = font1.render('Вы проиграли((', 1 ,(255,255,255))
            window.blit(text_final, ( 240, 250))
        if score == 100:
            finish = False
            window.blit(background, (0,0))
            text_final = font1.render('ПОБЕДА!!', 1 ,(255,255,255))
            window.blit(text_final, ( 240, 250))
    for e in event.get():
        if e.type == QUIT:
            game = False
    display.update()
    clock.tick(FPS)