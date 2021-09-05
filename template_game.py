import pygame
import numpy as np 
from collections import namedtuple
from enum import Enum

pygame.init()
font = pygame.font.SysFont('arial', 30)



Point = namedtuple('Point', 'x, y')
press = False

class Direction(Enum):
    LEFT = 1
    RIGHT = 2

game_over = False

ROAD_SIZE = 50

class Game:

    def __init__(self, w=1080, h=1000):

        self.w = w
        self.h = h

        self.x = ROAD_SIZE
        self.y = ROAD_SIZE

        self.last = 0

        self.direction = 0
        self.image = pygame.image.load("assets/city-car-png.png")
        self.image = pygame.transform.scale(self.image,(60,39))

        self.display = pygame.display.set_mode((self.w, self.h))
        pygame.display.set_caption("2D_City")
        self.clock = pygame.time.Clock()

        pygame.draw.rect(self.display, (0,0,0), pygame.Rect(ROAD_SIZE, ROAD_SIZE, self.w-2*ROAD_SIZE, ROAD_SIZE))

        coordinates = (Point(ROAD_SIZE, ROAD_SIZE), Point(self.w-ROAD_SIZE, ROAD_SIZE), Point(self.w-ROAD_SIZE, 2*ROAD_SIZE), Point(ROAD_SIZE, 2*ROAD_SIZE))

        self._draw_lines(coordinates)
        pygame.draw.line(self.display, (255,255,255), (ROAD_SIZE+2, ROAD_SIZE), (self.w-ROAD_SIZE-2, ROAD_SIZE), width=5)
        pygame.draw.line(self.display, (255,255,255), (ROAD_SIZE+2, ROAD_SIZE*2), (self.w-ROAD_SIZE-2, ROAD_SIZE*2), width=5)

        self.draw_horizontal(Point(0, self.h-ROAD_SIZE), Point(self.w//2, self.h-ROAD_SIZE))
        
        #self.display.blit(self.image, (coordinates[0].x,coordinates[0].y))

    def draw_horizontal(self, Point_a, Point_b):
        coordinates = [Point_a, Point_b, Point(Point_b.x, Point_b.y+ROAD_SIZE), Point(Point_a.x, Point_a.y+ROAD_SIZE)]
        x0,y0 = coordinates[0]
        x1, y1= coordinates[1]
        x2, y2 = coordinates[2]
        x3, y3 = coordinates[3]

        pygame.draw.rect(self.display, (0,0,0), pygame.Rect(x0, y0, x1-x0, ROAD_SIZE))
        self._draw_lines(coordinates)
        pygame.draw.line(self.display, (255,255,255), (x0+2, y0), (x1-2, y1), width=5)
        pygame.draw.line(self.display, (255,255,255), (x3+2, y3), (x2-2, y2), width=5)




    #class horizontal_road:
       # def __init(self, Point_a, Point_b):
            #self.coordinates = [Point_a, Point_b, Point(Point_b.x, Point_b.y+ROAD_SIZE), Point(Point_a.x, Point_a.y+ROAD_SIZE)]
           # self.x0, self.y0 = self.coordinates[0]
            #self.x1, self.y1= self.coordinates[1]
            #self.x2, self.y2 = self.coordinates[2]
            #self.x3, self.y3 = self.coordinates[3]
        #def draw(self):
        #    pygame.draw.rect(self.display, (0,0,0), pygame.Rect(self.x0, self.y0, self.x1-self.x0, ROAD_SIZE))
         #   self._draw_lines(self.coordinates)
          #  pygame.draw.line(self.display, (255,255,255), (self.x0, self.y0), (self.x1, self.y1), width=5)
           # pygame.draw.line(self.display, (255,255,255), (self.x3, self.y3), (self.x2, self.y2), width=5)
        #def _draw_lines(self):
         #   line_width = 3
          #  length = self.coordinates[1].x 
           # width = ROAD_SIZE
            #i = 0
        #    while i < length:
         #       x = x0
          #      y = ROAD_SIZE + width//2 - line_width/2
           #     pygame.draw.line(self.display, (255,255,0), (x0,y), (x0+10, y), width=3)
            #    x0 = x0 + 10 + 6
             #   i = x0 

              #  if i > length  - 10: 
                #    last_length = length -i 
               #     pygame.draw.line(self.display, (255,255,0), (x0, y), (length, y), width=3) 
                 #   i+=10


    def play(self):
        global press
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.direction = 1
                elif event.key == pygame.K_RIGHT:
                    self.direction = 2
                elif event.key ==pygame.K_DOWN:
                    self.direction = 3
                elif event.key==pygame.K_UP:
                    self.direction = 4            
            if event.type ==pygame.KEYUP:
                self.direction = 0


        #update game

        print(self.direction)
        self._update_game()
        self.clock.tick(60)

        return 1
    
    def _update_game(self):
        self.display.fill((5,123,0))

        pygame.draw.rect(self.display, (0,0,0), pygame.Rect(ROAD_SIZE, ROAD_SIZE, self.w-2*ROAD_SIZE, ROAD_SIZE))

        coordinates = (Point(ROAD_SIZE, ROAD_SIZE), Point(self.w-ROAD_SIZE, ROAD_SIZE), Point(self.w-ROAD_SIZE, 2*ROAD_SIZE), Point(ROAD_SIZE, 2*ROAD_SIZE))
        self._draw_lines(coordinates)
        pygame.draw.line(self.display, (255,255,255), (ROAD_SIZE+2, ROAD_SIZE), (self.w-ROAD_SIZE-2, ROAD_SIZE), width=5)
        pygame.draw.line(self.display, (255,255,255), (ROAD_SIZE+2, ROAD_SIZE*2), (self.w-ROAD_SIZE-2, ROAD_SIZE*2), width=5)

        self.draw_horizontal(Point(0, self.h-ROAD_SIZE), Point(self.w//2, self.h-ROAD_SIZE))
        self.draw_horizontal(Point(ROAD_SIZE, self.h/2 - ROAD_SIZE), Point(self.w//2 + ROAD_SIZE,self.h/2 - ROAD_SIZE ))

        self._move()
        print(self.x)
        self.display.blit(self.image, (self.x,self.y+5))
        
        pygame.display.flip()
        pygame.display.update()
    def _draw_lines(self, coordinates):
        line_width = 3
        length = coordinates[1].x 
        width = ROAD_SIZE
        x0,y0 = coordinates[0]
        x1, y1= coordinates[1]
        x2, y2 = coordinates[2]
        x3, y3 = coordinates[3]
        i = 0
        while i < length:
            x = x0
            y = y0 + width//2 - line_width/2 
            pygame.draw.line(self.display, (255,255,0), (x0,y), (x0+10, y), width=3)
            x0 = x0 + 10 + 6
            i = x0 

            if i > length  - 10: 
                last_length = length -i 
                pygame.draw.line(self.display, (255,255,0), (x0, y), (length, y), width=3) 
                i+=10
    def _move(self):
        if self.direction==1:
            if self.last ==3 or self.last==4:
                self.image = pygame.image.load("assets/city-car-png.png")
                self.image = pygame.transform.scale(self.image,(60,39))
                self.x-=15

            print("HEYY BABBEEE")
            self.x = self.x - 10
            self.last=1

        elif self.direction==2:
            if self.last ==3 or self.last==4:
                self.image = pygame.image.load("assets/city-car-png.png")
                self.image = pygame.transform.scale(self.image,(60,39))
            print('HEY BABE FUCK ME ')
            self.x +=10
            self.last=2
        elif self.direction == 3:
            if self.last==1 or self.last ==2:
                self.image = pygame.image.load("assets/car-down.png")
                self.image = pygame.transform.scale(self.image,(39,60))
                self.x+=15
            self.y+=10
            self.last=3
        elif self.direction == 4:
            if self.last==1 or self.last ==2:
                self.image = pygame.image.load("assets/car-down.png")
                self.image = pygame.transform.scale(self.image,(39,60))
                self.x+=15
            self.y-=10
            self.last = 4


            




        
        
if __name__ == '__main__':
    game = Game()

    while True:
        game.play()
        if game_over ==True:
            break

    pygame.quit()

