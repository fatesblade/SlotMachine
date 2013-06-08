'''
Created on 2013-06-07

@author: Kyle
'''

import pygame, pygbutton
pygame.font.init()
img = pygame.image.load('blank.jpg')
ff1 = pygame.image.load('ff1.jpg')
ff2 = pygame.image.load('ff2.jpg')
ff3 = pygame.image.load('ff3.jpg')
ff4 = pygame.image.load('ff4.jpg')
ff5 = pygame.image.load('ff5.jpg')
ff6 = pygame.image.load('ff6.jpg')
ff7 = pygame.image.load('ff7.jpg')
ff8 = pygame.image.load('ff8.jpg')
title = pygame.image.load('title.jpg')

def main():
    """ The Main function that runs the game loop """
    pygame.init()
    Player_Money = 1000
    Jack_Pot = 500
    Turn = 1
    Bet = 0
    Prev_Bet=0
    win_number = 0
    loss_number = 0
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("The House Always Wins!")    
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((5, 5, 5))    
    clock = pygame.time.Clock()
    keepGoing = True
    box = pygame.Surface((560, 390))
    box = box.convert()
    box.fill((235, 230, 230))
    box_x = 40
    box_y = 40
    box1 = pygame.Surface((250, 100))
    box1 = box1.convert()
    box1.fill((55, 55, 55))
    box1_x = 100
    box1_y = 310
    buttonSpin = pygbutton.PygButton((400, 350, 150, 30), 'Spin')
    buttonReset = pygbutton.PygButton((400, 380, 150, 30), 'Reset')
    while keepGoing:    
        clock.tick(60)    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
        screen.blit(background, (0, 0))
        screen.blit(box, (box_x, box_y))
        screen.blit(box1, (box1_x, box1_y))
        screen.blit(title,( 150, 50))
        screen.blit(img,( 95, 125))
        screen.blit(img,( 255, 125))
        screen.blit(img,( 415, 125))
        
        buttonSpin.draw(screen)
        buttonReset.draw(screen)
        pygame.display.flip()
if __name__ == "__main__": main()