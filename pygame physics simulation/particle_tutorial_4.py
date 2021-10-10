
import pygame
import random
import math

background_colour = (255,255,255)
(width, height) = (900, 700)
PlayerMovementX = 10
PlayerMovementY = 10

PlayedWidthX = 50
PlayedWidthY = 50

Velocity = 1

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('testicles')
screen.fill(background_colour)

pygame.time.delay(1)

class Particle:
    def __init__(self, position, size):
        self.x, self.y = position
        self.size = size
        self.colour = (255, 0, 0)
        self.speed = 0
        self.angle = 0

    def display(self):
        pygame.draw.circle(screen, self.colour, (self.x, self.y), self.size)

    def move(self):
        self.x += math.sin(self.angle) * self.speed
        self.y -= math.cos(self.angle) * self.speed

size = random.randint(25, 40)
x = random.randint(size, width - size)
y = random.randint(size, height - size) 

joe_mama = Particle((x, y), size)

joe_mama.speed = random.random()
joe_mama.angle = random.uniform(0, math.pi*2)


running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(background_colour)

    Movement = pygame.key.get_pressed()

    if Movement[pygame.K_LEFT]:
        PlayerMovementX -= Velocity

    if Movement[pygame.K_RIGHT]:
        PlayerMovementX += Velocity

    if Movement[pygame.K_UP]:
        PlayerMovementY -= Velocity

    if Movement[pygame.K_DOWN]:
        PlayerMovementY += Velocity

    joe_mama.move()
    joe_mama.display()

    pygame.draw.rect(screen , (255,0,0),(PlayerMovementX, PlayerMovementY, PlayedWidthX, PlayedWidthY))
    pygame.display.flip()
    pygame.display.update()
