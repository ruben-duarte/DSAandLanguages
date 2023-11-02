import pygame
from pygame.locals import *  #import global variables

# palette colors https://coolors.co/353535-3c6e71-ffffff-d9d9d9-284b63
class Snake:
    def __init__(self,parent_screen):
            self.parent_screen = parent_screen
            self.block = pygame.image.load("G:\portafolio\\12a_DataStructuresAndAlgorithms\Python\warm-up\snake_game\images\\block2.png").convert()
            self.x = 100
            self.y = 100
    
    def draw(self):
        self.parent_screen.fill((40,75,99))
        self.parent_screen.blit(self.block, (self.x,self.y))
        pygame.display.flip()
    
    def move_left(self):
        self.x -=8
        self.draw()
  
    def move_right(self):
        self.x +=8
        self.draw()
  
    def move_up(self):
        self.y -=8
        self.draw()
  
    def move_down(self):
        self.y +=8
        self.draw()

        
class Game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((700,500))
        self.surface.fill((40,75,99))
        self.snake = Snake(self.surface)
        self.snake.draw()

    def run(self):
            running = True

            while running:
                for event in pygame.event.get():
                    if event.type == QUIT:
                        running = False
                    elif event.type == KEYDOWN:
                        if event.key == K_ESCAPE:
                            running = False
                        if event.key == K_UP:
                           self.snake.move_up()
                        if event.key == K_DOWN:
                            self.snake.move_down()
                        if event.key == K_LEFT:
                            self.snake.move_left()
                        if event.key == K_RIGHT:
                            self.snake.move_right()



if __name__ == '__main__':
    game = Game()
    game.run()
    
    





   

 

 



