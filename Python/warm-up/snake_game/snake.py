import pygame
from pygame.locals import *  #import global variables
import time

# palette colors https://coolors.co/353535-3c6e71-ffffff-d9d9d9-284b63
SIZE = 14

class Apple:
    def __init__(self, parent_screen):
         self.image = pygame.image.load("G:\portafolio\\12a_DataStructuresAndAlgorithms\Python\warm-up\snake_game\images\\apple.png").convert()
         self.parent_screen = parent_screen
         self.x = SIZE*3
         self.y = SIZE*3

    def draw(self):
        self.parent_screen.blit(self.image, (self.x, self.y))
        pygame.display.flip()

class Snake:
    def __init__(self,parent_screen,length):
            self.length = length
            self.parent_screen = parent_screen
            self.block = pygame.image.load("G:\portafolio\\12a_DataStructuresAndAlgorithms\Python\warm-up\snake_game\images\\block2.png").convert()
            self.x = [SIZE]*length
            self.y = [SIZE]*length
            self.direction = "down"

    def draw(self):
        self.parent_screen.fill((40,75,99))
        for element in range(self.length):
            self.parent_screen.blit(self.block, (self.x[element],self.y[element]))
        pygame.display.flip()
    
    def move_left(self):
        self.direction = "left"
        
  
    def move_right(self):
        self.direction = "right"
        
  
    def move_up(self):
        self.direction  = "up"
        
  
    def move_down(self):
        self.direction = "down"
        

    def walk(self):

        for i in range(self.length-1,0,-1):
            self.x[i] =self.x[i-1]
            self.y[i] =self.y[i-1]


        if self.direction == 'up':
            self.y[0] -= SIZE
        if self.direction == 'down':
            self.y[0] += SIZE
        if self.direction == 'left':
            self.x[0] -= SIZE
        if self.direction == 'right':
            self.x[0] += SIZE
        self.draw()


        
class Game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((700,500))
        self.surface.fill((40,75,99))
        self.snake = Snake(self.surface,5)
        self.snake.draw()
        self.apple = Apple(self.surface)
        self.apple.draw()

    def play(self):
         self.snake.walk()
         self.apple.draw()

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
                self.play()
                time.sleep(0.25)


if __name__ == '__main__':
    game = Game()
    game.run()
    
    





   

 

 



