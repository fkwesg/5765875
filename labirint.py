# Разработай свою игру в этом файле!
from pygame import *
window = display.set_mode((700, 500))
white = ((255, 255, 255))
window.fill(white)
display.set_caption('неизвестная аномалия')
background = transform.scale(image.load('final.jpg'), (700, 500))
win_width = 200
win_width_1 = 380
lose = transform.scale(image.load('gameover.jpg'), (700, 500))

class cookie(sprite.Sprite):
    def __init__(self, picture, w, h, x, y):
        super().__init__()
        self.image = transform.scale(image.load(picture), (w, h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Card((sprite.Sprite)):
    def __init__(self, width, height, x, y, color):
        super().__init__()
        self.rect = Rect(x, y, width, height)
        self.fill_color = color
    def draw(self):
        draw.rect(window, self.fill_color, self.rect)

class Player(cookie):
    def __init__(self, picture, w, h, x, y, x_speed, y_speed):
        super().__init__(picture, w, h, x, y)
        self.x_speed = x_speed
        self.y_speed = y_speed
    def update(self):
        self.rect.x += self.x_speed
        platforms_touched = sprite.spritecollide(self, barriers, False)
        if self.x_speed > 0:
            for p in platforms_touched:
                self.rect.right = min(self.rect.right, p.rect.left)
        elif self.x_speed < 0:
            for p in platforms_touched:
                self.rect.left = max(self.rect.left, p.rect.right)
        self.rect.y += self.y_speed
        platforms_touched = sprite.spritecollide(self, barriers, False)
        if self.y_speed > 0:
            for p in platforms_touched:
                self.rect.bottom = min(self.rect.bottom, p.rect.top)
        elif self.y_speed < 0:
            for p in platforms_touched:
                self.rect.top = max(self.rect.top, p.rect.bottom)
    
class Enemy(cookie):
    def __init__(self, picture, w, h, x, y, speed):
        super().__init__(picture, w, h, x, y)
        self.speed = speed
    def update(self):
        if self.rect.y <= 100:
            self.direction = "bottom"
        if self.rect.y >= win_width - 40:
            self.direction = "top"
        if self.direction == "top":
            self.rect.y -= self.speed
        else:
            self.rect.y += self.speed

class enemies(cookie):
    def __init__(self, picture, w, h, x, y, speed):
        super().__init__(picture, w, h, x, y)
        self.speed = speed
    def update(self):
        if self.rect.y <= 100:
            self.direction = "bottom"
        if self.rect.y >= win_width_1:
            self.direction = "top"
        if self.direction == "top":
            self.rect.y -= self.speed
        else:
            self.rect.y += self.speed

player = Player('people.png', 60, 60, 620, 350, 0, 0)
tik = Card(40, 110, 50, 80, (153, 153, 153))
wall1 = cookie('countr.png', 20, 210, 580, 290)
wall2 = cookie('countr.png', 20, 200, 480, 170)
door = cookie('exit.jpg', 80, 30, 30, 20)
wall3 = cookie('countr1.png', 230, 20, 480, 171)
monster = Enemy('ball.png', 60, 50, 110, 10, 5)
mouse = enemies('monsters.png', 60, 50, 310, 380, 5)
wall4 = cookie('countr.png', 20, 100, 200, 0)
wall5 = cookie('countr1.png', 200, 20, 0, 180)
wall6 = cookie('countr1.png', 200, 20, 290, 71)
wall7 = cookie('countr.png', 20, 200, 280, 70)
wall8 = cookie('countr.png', 20, 200, 380, 0)
wall9 = cookie('countr.png', 20, 200, 380, 300)
wall10 = cookie('countr.png', 20, 100, 570, 0)
wall11 = cookie('countr1.png', 220, 20, 80, 270)
wall12 = cookie('countr.png', 20, 160, 80, 269)
wall13 = cookie('countr1.png', 150, 20, 160, 390)
wall14 = cookie('countr.png', 20, 200, 225, 350)

barriers = sprite.Group()
barriers.add(wall1)
barriers.add(wall2)
barriers.add(wall3)
barriers.add(wall4)
barriers.add(wall5)
barriers.add(wall6)
barriers.add(wall7)
barriers.add(wall8)
barriers.add(wall9)
barriers.add(wall10)
barriers.add(wall11)
barriers.add(wall12)
barriers.add(wall13)
barriers.add(wall14)

monsters = sprite.Group()
monsters.add(monster)
monsters.add(mouse)

finish = False
run = True
while run:
    time.delay(50)
    window.fill(white)
    
    for e in event.get():
        if e.type == QUIT:
            run = False
        elif e.type == KEYDOWN:
            if e.key == K_UP:
                player.y_speed -= 10
            if e.key == K_DOWN:
                player.y_speed += 10
            if e.key == K_LEFT:
                player.x_speed -= 10
            if e.key == K_RIGHT:
                player.x_speed += 10
        elif e.type == KEYUP:
            if e.key == K_UP:
                player.y_speed = 0
            if e.key == K_DOWN:
                player.y_speed = 0
            if e.key == K_LEFT:
                player.x_speed = 0
            if e.key == K_RIGHT:
                player.x_speed = 0
            if e.key == K_SPACE:
                player.fire()

    if finish != True:
        player.update()
        monsters.update()
        tik.draw()
        door.reset()
        player.reset()
        monsters.draw(window)
        barriers.draw(window)

        if sprite.collide_rect(player, tik):
            finish = True
            window.blit(background, (0, 0))

        if sprite.spritecollide(player, monsters, False):
            finish = True
            window.blit(lose, (0, 0))
        
        display.update()