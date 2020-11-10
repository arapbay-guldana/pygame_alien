import pygame
from random import randint

fps = 30
width = 750
height = 750
pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('GALAXIAN')
clock = pygame.time.Clock()


class Spaceship(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30, 20))
        self.image.fill((0, 0, 255))
        self.rect = self.image.get_rect()
        self.rect.centerx = int(width / 2)
        self.rect.bottom = height - 50
        self.initial_health = 10
        self.remaining_health = 10


    def update(self):
        speed = 20
        key = pygame.key.get_pressed()
        if key[pygame.K_RIGHT]:
            self.rect.x += speed
        elif key[pygame.K_LEFT]:
            self.rect.x -= speed
        if self.rect.right > width:
            self.rect.right = width
        elif self.rect.left < 0:
            self.rect.left = 0


    def shoot(self):
        lazer = Lazer(self.rect.centerx, self.rect.top)
        spaceship_group.add(lazer)
        lazer_group.add(lazer)


class Lazer(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 10))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speedy = -15

    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill()
        if pygame.sprite.spritecollide(self, aliens_group, True):
            self.kill()
        if pygame.sprite.spritecollide(self, shields_group, True):
            self.kill()

    pygame.draw.rect(screen, (0, 255, 0), (self.rect.x, (self.rect.bottom + 10), self.rect.width, 15))
    if self.remaining_health > 0:
        pygame.draw.rect(screen, (0, 255, 0), (
        self.rect.x, (self.rect.bottom + 10), int(self.rect.width * (self.remaining_health / self.initial_health)), 15))


class Aliens(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((40, 20))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()
        self.move_direction=1
        self.move_counter=0
    def update(self):
        self.rect.x += self.move_direction
        self.move_counter += 1
        if abs(self.move_counter) > 125:
            self.move_direction *= -1
            self.move_counter *= self.move_direction
            self.rect.y+=5
class Shields(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 10))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()
    def update(self):
        if pygame.sprite.spritecollide(self, aliens_group, True):
            self.kill()


spaceship_group = pygame.sprite.Group()
spaceship = Spaceship()
spaceship_group.add(spaceship)
lazer_group = pygame.sprite.Group()
aliens_group = pygame.sprite.Group()
shields_group = pygame.sprite.Group()
for row in range(1, 6):
    for column in range(1, 11):
        aliens = Aliens()
        aliens.rect.x = 80 + (50 * column)
        aliens.rect.y = 50 + (50 * row)
        aliens_group.add(aliens)

for shield in range(4):
    for row in range(5):
        for column in range(10):
            shields = Shields()
            shields.rect.x = (50 + (195 * shield)) + (10 * column)
            shields.rect.y = 500 + (10 * row)
            shields_group.add(shields)
play_game = True
while play_game:
    clock.tick(fps)
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play_game = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                spaceship.shoot()
    spaceship_group.draw(screen)
    lazer_group.draw(screen)
    aliens_group.draw(screen)
    shields_group.draw(screen)
    spaceship_group.update()
    lazer_group.update()
    aliens_group.update()
    shields_group.update()
    pygame.display.update()
pygame.quit()

