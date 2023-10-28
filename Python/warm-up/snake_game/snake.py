import pygame
from pygame.locals import *  #import global variables

def draw_block():
    surface.fill((40,75,99))
    surface.blit(block, (block_x,block_y))
    pygame.display.flip()

if __name__ == '__main__':
    pygame.init()

    surface = pygame.display.set_mode((700,500))
    surface.fill((40,75,99))

    block = pygame.image.load("./images/block.png").convert()
    block_x, block_y = 100,100
    surface.blit(block, (block_x,block_y))

    pygame.display.flip()

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                if event.key == K_UP:
                    block_y -= 8
                    draw_block()
                if event.key == K_DOWN:
                    block_y += 8
                    draw_block()
                if event.key == K_LEFT:
                    block_x -= 8
                    draw_block()
                if event.key == K_RIGHT:
                    block_x += 8
                    draw_block()




