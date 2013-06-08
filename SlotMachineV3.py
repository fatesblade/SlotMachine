'''
Created on 2013-06-07

@author: Kyle
'''

import pygame, pygbutton, sys
import random
pygame.font.init()
blank = pygame.image.load('blank.jpg')
ff1 = pygame.image.load('ff1.jpg')
ff2 = pygame.image.load('ff2.jpg')
ff3 = pygame.image.load('ff3.jpg')
ff4 = pygame.image.load('ff4.jpg')
ff5 = pygame.image.load('ff5.jpg')
ff6 = pygame.image.load('ff6.jpg')
ff7 = pygame.image.load('ff7.jpg')
title = pygame.image.load('title.jpg')


def Reels():
    """ When this function is called it determines the Bet_Line results.
        e.g. Bar - Orange - Banana """
        
    # [0]Fruit, [1]Fruit, [2]Fruit
    Bet_Line = [" "," "," "]
    Outcome = [0,0,0]
    
    # Spin those reels
    for spin in range(3):
        Outcome[spin] = random.randrange(1,65,1)
        # Spin those Reels!
        if Outcome[spin] >= 1 and Outcome[spin] <=26:   # 40.10% Chance
            Bet_Line[spin] = "blank"
        if Outcome[spin] >= 27 and Outcome[spin] <=36:  # 16.15% Chance
            Bet_Line[spin] = "ff1"
        if Outcome[spin] >= 37 and Outcome[spin] <=45:  # 13.54% Chance
            Bet_Line[spin] = "ff2"
        if Outcome[spin] >= 46 and Outcome[spin] <=53:  # 11.98% Chance
            Bet_Line[spin] = "ff3"
        if Outcome[spin] >= 54 and Outcome[spin] <=58:  # 7.29%  Chance
            Bet_Line[spin] = "ff4"
        if Outcome[spin] >= 59 and Outcome[spin] <=61:  # 5.73%  Chance
            Bet_Line[spin] = "ff5"
        if Outcome[spin] >= 62 and Outcome[spin] <=63:  # 3.65%  Chance
            Bet_Line[spin] = "ff6"  
        if Outcome[spin] == 64:                         # 1.56%  Chance
            Bet_Line[spin] = "ff7"    
    
    return Bet_Line

def pullthehandle(Bet, Player_Money, Jack_Pot):
    """ This function takes the Player's Bet, Player's Money and Current JackPot as inputs.
        It then calls the Reels function which generates the random Bet Line results.
        It calculates if the player wins or loses the spin.
        It returns the Player's Money and the Current Jackpot to the main function """
    Player_Money -= Bet
    Jack_Pot += (int(Bet*.15)) # 15% of the player's bet goes to the jackpot
    win = False
    FFwheel_Reel = Reels()
    FFchar = FFwheel_Reel[0] + " - " + FFwheel_Reel[1] + " - " + FFwheel_Reel[2]
    Reel1 = pygame.image.load(FFwheel_Reel[0] + ".jpg")
    Reel2 = pygame.image.load(FFwheel_Reel[1] + ".jpg")
    Reel3 = pygame.image.load(FFwheel_Reel[2] + ".jpg")
    #re-draws the gui
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("The House Always Wins!")
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((5, 5, 5))    
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
    myFont = pygame.font.SysFont('Times New Roman', 15,)
    JackPotLabel = myFont.render('Jackpot Amount:', 1, (255, 255, 255))
    MoneyLabel = myFont.render('Money Remaining:', 1, (255, 255, 255))
    TurnLabel = myFont.render('Turn #', 1, (255, 255, 255))
    BetLabel = myFont.render('Current Bet:', 1, (255, 255, 255))
    WinLabel = myFont.render('# of Wins:', 1, (255, 255, 255))
    LossLabel = myFont.render('# of Loses:', 1, (255, 255, 255))
    buttonSpin = pygbutton.PygButton((400, 320, 150, 30), 'Spin')
    buttonReset = pygbutton.PygButton((400, 350, 150, 30), 'Reset')
    buttonQuit = pygbutton.PygButton((400, 380, 150, 30), 'Quit')
    buttonbetupsmall = pygbutton.PygButton((110, 410, 35, 30), '+10')
    buttonbetupmed = pygbutton.PygButton((145, 410, 40, 35), '+25')
    buttonbetuplarge = pygbutton.PygButton((185, 410, 45, 40), '+100')
    buttonbetdownsmall = pygbutton.PygButton((230, 410, 35, 30), '-10')
    buttonbetdownmed = pygbutton.PygButton((265, 410, 40, 35), '-25')
    buttonbetdownlarge = pygbutton.PygButton((305, 410, 45, 40), '-100')
    screen.blit(background, (0, 0))
    screen.blit(box, (box_x, box_y))
    screen.blit(box1, (box1_x, box1_y))
    screen.blit(title,( 150, 50))
    screen.blit(JackPotLabel,(110, 320))  
    screen.blit(MoneyLabel,(110, 335))
    screen.blit(TurnLabel,(110, 350)) 
    screen.blit(BetLabel,(230, 350)) 
    screen.blit(WinLabel,(110, 365)) 
    screen.blit(LossLabel,(230, 365))        
    buttonSpin.draw(screen)
    buttonReset.draw(screen)
    buttonQuit.draw(screen)
    buttonbetupsmall.draw(screen)
    buttonbetupmed.draw(screen)
    buttonbetuplarge.draw(screen)
    buttonbetdownsmall.draw(screen)
    buttonbetdownmed.draw(screen)
    buttonbetdownlarge.draw(screen)
    screen.blit(Reel1,( 95, 125))
    screen.blit(Reel2,( 415, 125))
    screen.blit(Reel3,( 255, 125))
    # Match 3
    if FFwheel_Reel.count("ff1") == 3:
        winnings,win = Bet*20,True
    elif FFwheel_Reel.count("ff2") == 3:
        winnings,win = Bet*30,True
    elif FFwheel_Reel.count("ff3") == 3:
        winnings,win = Bet*40,True
    elif FFwheel_Reel.count("ff4") == 3:
        winnings,win = Bet*100,True
    elif FFwheel_Reel.count("ff5") == 3:
        winnings,win = Bet*200,True
    elif FFwheel_Reel.count("ff6") == 3:
        winnings,win = Bet*300,True
    elif FFwheel_Reel.count("ff7") == 3:
        print("One Winged Angel Bonus!!!")
        winnings,win = Bet*1000,True
    # Match 2
    elif FFwheel_Reel.count("Blank") == 0:
        if FFwheel_Reel.count("ff1") == 2:
            winnings,win = Bet*2,True
        if FFwheel_Reel.count("ff2") == 2:
            winnings,win = Bet*2,True
        elif FFwheel_Reel.count("ff3") == 2:
            winnings,win = Bet*3,True
        elif FFwheel_Reel.count("ff4") == 2:
            winnings,win = Bet*4,True
        elif FFwheel_Reel.count("ff5") == 2:
            winnings,win = Bet*5,True
        elif FFwheel_Reel.count("ff6") == 2:
            winnings,win = Bet*10,True
        elif FFwheel_Reel.count("ff7") == 2:
            winnings,win = Bet*20,True
    
        # Match Lucky Seven
        elif FFwheel_Reel.count("ff7") == 1:
            winnings, win = Bet*10,True
            
        else:
            winnings, win = Bet*2,True
    if win:    
        print(FFchar + "\n" + "You Won $ " + str(int(winnings)) + " !!! \n")
        Player_Money += int(winnings)
    
        # Jackpot 1 in 450 chance of winning
        jackpot_try = random.randrange(1,51,1)
        jackpot_win = random.randrange(1,51,1)
        if  jackpot_try  == jackpot_win:
            print ("You Won The Jackpot !!!\nHere is your $ " + str(Jack_Pot) + "prize! \n")
            Jack_Pot = 500
        elif jackpot_try != jackpot_win:
            print ("You did not win the Jackpot this time. \nPlease try again ! \n")
    # No win
    else:
        print(FFchar + "\nPlease try again. \n")
    
    return Player_Money, Jack_Pot, win


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
    Win = 0    
    clock = pygame.time.Clock()
    keepGoing = True
    #the gui drawn for the first time
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("The House Always Wins!")
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((5, 5, 5))    
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
    myFont = pygame.font.SysFont('Times New Roman', 15,)
    JackPotLabel = myFont.render('Jackpot Amount:', 1, (255, 255, 255))
    MoneyLabel = myFont.render('Money Remaining:', 1, (255, 255, 255))
    TurnLabel = myFont.render('Turn #', 1, (255, 255, 255))
    BetLabel = myFont.render('Current Bet:', 1, (255, 255, 255))
    WinLabel = myFont.render('# of Wins:', 1, (255, 255, 255))
    LossLabel = myFont.render('# of Loses:', 1, (255, 255, 255))
    buttonSpin = pygbutton.PygButton((400, 320, 150, 30), 'Spin')
    buttonReset = pygbutton.PygButton((400, 350, 150, 30), 'Reset')
    buttonQuit = pygbutton.PygButton((400, 380, 150, 30), 'Quit')
    buttonbetupsmall = pygbutton.PygButton((110, 410, 35, 30), '+10')
    buttonbetupmed = pygbutton.PygButton((145, 410, 40, 35), '+25')
    buttonbetuplarge = pygbutton.PygButton((185, 410, 45, 40), '+100')
    buttonbetdownsmall = pygbutton.PygButton((230, 410, 35, 30), '-10')
    buttonbetdownmed = pygbutton.PygButton((265, 410, 40, 35), '-25')
    buttonbetdownlarge = pygbutton.PygButton((305, 410, 45, 40), '-100')
    screen.blit(background, (0, 0))
    screen.blit(box, (box_x, box_y))
    screen.blit(box1, (box1_x, box1_y))
    screen.blit(title,( 150, 50))
    screen.blit(JackPotLabel,(110, 320))  
    screen.blit(MoneyLabel,(110, 335))
    screen.blit(TurnLabel,(110, 350)) 
    screen.blit(BetLabel,(230, 350)) 
    screen.blit(WinLabel,(110, 365)) 
    screen.blit(LossLabel,(230, 365))        
    buttonSpin.draw(screen)
    buttonReset.draw(screen)
    buttonQuit.draw(screen)
    buttonbetupsmall.draw(screen)
    buttonbetupmed.draw(screen)
    buttonbetuplarge.draw(screen)
    buttonbetdownsmall.draw(screen)
    buttonbetdownmed.draw(screen)
    buttonbetdownlarge.draw(screen)
    screen.blit(blank,( 95, 125))
    screen.blit(blank,( 255, 125))
    screen.blit(blank,( 415, 125))
    while keepGoing:    
        clock.tick(60)    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
        if Player_Money <1:
            Player_Money = 500
        #requires double click
        if 'click' in buttonbetupsmall.handleEvent(event):
            Bet = Bet + 10
        elif 'click' in buttonbetupmed.handleEvent(event):
            Bet = Bet + 25
        elif 'click' in buttonbetuplarge.handleEvent(event):
            Bet = Bet + 100
        elif 'click' in buttonbetdownsmall.handleEvent(event):
            Bet = Bet - 10
        elif 'click' in buttonbetdownmed.handleEvent(event):
            Bet = Bet - 25
        elif 'click' in buttonbetdownlarge.handleEvent(event):
            Bet = Bet - 100
        if 'click' in buttonQuit.handleEvent(event):
            pygame.quit()
            sys.exit()
        if 'click' in buttonReset.handleEvent(event):
            screen.blit(blank,( 95, 125))
            screen.blit(blank,( 255, 125))
            screen.blit(blank,( 415, 125))
        if 'click' in buttonSpin.handleEvent(event):   
            if Bet > Player_Money:
                print("Sorry, you only have $" + str(Player_Money) + " \n")
            elif Bet <= Player_Money:
                Turn +=1
                Prev_Bet = Bet
                Player_Money, Jack_Pot, win = pullthehandle(Bet, Player_Money, Jack_Pot)
        pygame.display.flip()
if __name__ == "__main__": main()