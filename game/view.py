import pygame

from .rules import *
from .rect import Rect


class View(object):

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((310, 310))
        pygame.display.set_caption('Tic Tac Toe')
        blockSize = 100
        self.grid = [
            Rect(0*blockSize, 0*blockSize, blockSize, blockSize), 
            Rect(1*blockSize+5, 0*blockSize, blockSize, blockSize), 
            Rect(2*blockSize+10, 0*blockSize, blockSize, blockSize),

            Rect(0*blockSize, 1*blockSize+5, blockSize, blockSize), 
            Rect(1*blockSize+5, 1*blockSize+5, blockSize, blockSize), 
            Rect(2*blockSize+10, 1*blockSize+5, blockSize, blockSize),

            Rect(0*blockSize, 2*blockSize+10, blockSize, blockSize), 
            Rect(1*blockSize+5, 2*blockSize+10, blockSize, blockSize), 
            Rect(2*blockSize+10, 2*blockSize+10, blockSize, blockSize),
        ]
        
        self.run()
    
    def run(self):
        run = True
        self.playerTurn = True
        for rect in self.grid:
            pygame.draw.rect(self.screen, (255,255,255), rect)

        while run:
            for event in pygame.event.get():

                self.redrawScreen()

                if event.type == pygame.QUIT:
                    run = False

                if self.playerTurn:
                    if not(isWinner(self.grid, 'O')) :
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            for rect in self.grid:
                                if rect.collidepoint(
                                    pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]
                                ):
                                    self.drawX(rect)
                                    pygame.display.update()
                    else:
                        print('You lose')
                        run = False
                else:
                    if not(isWinner(self.grid, 'X')):
                        move = computerMove(self.grid)
                        self.drawO(self.grid[move])
                        pygame.display.update()
                    else:
                        print('You won')
                        run = False

                if isGridFull(self.grid):
                    run = False

        pygame.quit()

    def redrawScreen(self):
        pygame.display.update()

    def drawX(self, rect):
        if rect.draw != '':
            print('Space is fulfilled')
            return

        pygame.draw.lines(
            self.screen, 
            (255,0,0), 
            False, 
            [(rect.x+10, rect.y+10), (rect.x+90, rect.y+90)],
            10)
        pygame.draw.lines(
            self.screen, 
            (255,0,0), 
            False, 
            [(rect.x+10, rect.y+90), (rect.x+90, rect.y+10)],
            10)
        rect.draw = 'X'
        self.playerTurn = False

    def drawO(self, rect):
        pygame.draw.circle(
            self.screen, 
            (0,0,255), 
            [rect.x+50, rect.y+50], 
            40,
            5
        )
        rect.draw = 'O'
        self.playerTurn = True
