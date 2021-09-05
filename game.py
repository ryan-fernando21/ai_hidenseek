import pygame
import numpy as np 
from collections import namedtuple

pygame.init()
font = pygame.font.SysFont('arial', 30)



Point = namedtuple('Point', 'x, y')
press = False

game_over = False

class Game:

    def __init__(self, w=640, h=480):


        self.w = w
        self.h = h


        self.display = pygame.display.set_mode((self.w, self.h))
        pygame.display.set_caption("2D_City")
        self.clock = pygame.time.Clock()
        self.display.fill((0,0,0))
        

    def play(self):
        global press
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN or press==True:
                press = True
                self.mouse_x, self.mouse_y = pygame.mouse.get_pos()
                pygame.draw.rect(self.display, (128,128,128), (self.mouse_x, self.mouse_y, 10,10))
                print(self.mouse_x)
            if event.type ==pygame.MOUSEBUTTONUP:
                press=False
            #if pygame.mouse.get_pressed()==(1,0,0):

        #update game
        self._update_game()
        self.clock.tick(60)

        return 1
    
    def _update_game(self):
        pygame.display.flip()



        
        
if __name__ == '__main__':
    game = Game()

    while True:
        game.play()
        if game_over ==True:
            break

    pygame.quit()

