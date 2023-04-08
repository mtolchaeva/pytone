from pygame import *
from random import *
#создай окно игры
window = display.set_mode((700, 500))
display.set_caption('Небо')
direction = ''
class GameSprite(sprite.Sprite):
    def __init__(self, w, h, player_image, player_x, player_y, player_speed,):
        super().__init__()
        self.w = w
        self.h = h
        self.image = transform.scale(image.load(player_image), (w, h))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def showhero(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    def upravlenie(self):
        keysq = key.get_pressed()
        if keysq[K_LEFT]:
            self.rect.x -= self.speed
        if keysq[K_RIGHT]:
            self.rect.x += self.speed 
    def update(self):
        global lose
        self.rect.y += self.speed
        if self.rect.y >= 550:
            self.rect.x = randint(0,650)
            self.rect.y = -50
            lose += 1
    def fire(self):
        bullet = Bullet(20, 20, 'pula.png', self.rect.centerx, self.rect.y, 5)
        bullets.add(bullet)
        
class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y < 5:
            self.kill()

clock = time.Clock()
FPS = 60
lose = 0
lose1 = 0
life = 3
fon = transform.scale(image.load('fon.png'), (700, 500))
live = GameSprite(115, 45, 'live.png', 0, 60, 0)
font.init()
font1 = font.Font(None, 36)

text_popadanie = font1.render('Попадание:' + str(lose1), 1, (255,255,255))
player = GameSprite(100, 100, 'vrag.png', 350, 350, 10)

bullets = sprite.Group()
monsters = sprite.Group()
for i in range(10):
    monster = GameSprite(50, 50, 'mone.png', randint(0, 650), -50, randint(1,3))
    monsters.add(monster)
game = True
game1 = False
while game:
    window.blit(fon, (0,0))
    text_lose = font1.render('Пропущено:' + str(lose), 1, (255,255,255))
    text_popadanie = font1.render('Попадание:' + str(lose1), 1, (255,255,255))
    window.blit(text_lose, (0,0))
    window.blit(text_popadanie, (0,30))
    player.showhero()
    live.showhero()
    player.upravlenie()
    monsters.draw(window)
    bullets.draw(window)
    monsters.update()
    bullets.update()
    kp = key.get_pressed()
    for e in event.get():
        if e.type == QUIT:
            game = False
        if kp[K_SPACE]:
            player.fire()
    if sprite.spritecollide(player, monsters, True):
        life -= 1
        if life == 2:
            live = GameSprite(115, 45, 'live1.png', 0, 60, 0)
            live.showhero()
        elif life == 1:
            live = GameSprite(115, 45, 'live2.png', 0, 60, 0)
            live.showhero()
    if life == 0:
        game = False
    if sprite.groupcollide(monsters, bullets, True, True):
        lose1 += 1
        monster = GameSprite(70, 60, 'mone.png', randint(0, 650), -50, randint(1,3))
        monsters.add(monster)
    if lose1 >= 15: 
        game = False
        game1 = True
    clock.tick(FPS)
    display.update()

life1 = 3
lose = 0
lose1 = 0
fon1 = transform.scale(image.load('noch.jpg'), (700, 500))
live1 = GameSprite(115, 45, 'live.png', 0, 60, 0)
monsters1 = sprite.Group()
for i in range(15):
    monster = GameSprite(50, 50, 'mone.png', randint(0, 650), -50, randint(1,3))
    monsters1.add(monster)

while game1:
    window.blit(fon1, (0,0))
    text_lose = font1.render('Пропущено:' + str(lose), 1, (255,255,255))
    text_popadanie = font1.render('Попадание:' + str(lose1), 1, (255,255,255))
    window.blit(text_lose, (0,0))
    window.blit(text_popadanie, (0,30))
    player.showhero()
    live1.showhero()
    player.upravlenie()
    monsters1.draw(window)
    bullets.draw(window)
    monsters1.update()
    bullets.update()
    kp = key.get_pressed()
    for e in event.get():
        if e.type == QUIT:
            game1 = False
        if kp[K_SPACE]:
            player.fire()
    if sprite.spritecollide(player, monsters, True):
        life1 -= 1
        if life1 == 2:
            live1 = GameSprite(115, 45, 'live1.png', 0, 60, 0)
            live1.showhero()
        elif life == 1:
            live1 = GameSprite(115, 45, 'live2.png', 0, 60, 0)
            live1.showhero()
    if life1 == 0:
        game1 = False
    if sprite.groupcollide(monsters1, bullets, True, True):
        lose1 += 1
        monster = GameSprite(70, 60, 'mone.png', randint(0, 650), -50, randint(1,3))
        monsters1.add(monster)
    if lose1 >= 30:
        game1 = False
    clock.tick(FPS)
    display.update()