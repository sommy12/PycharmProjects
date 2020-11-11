#game colors used
orange=[240,100,23]
black=[0,0,0]
white=[255,255,255]

#positions of the drawn object
display_width = 600
display_height = 600

import pygame as py
import time
#initializing the game module
py.init()

#game display and game caption(game name)
py.display.set_caption('MINESPEAR')
gameDisplay = py.display.set_mode([display_width,display_height])
clock=py.time.Clock()

font=py.font.SysFont(None, 30)
def print_msg(msg,color):
    text = font.render(msg, True, color)
    gameDisplay.blit(text, [display_width/2, display_height/2])

#loop for events handling like movements, actions, frame-rate, display-update, etc
def game_loop():
    display_width = 600
    display_height = 600
    posx = display_width / 2
    posy = display_height / 2
    posx_change = 0
    posy_change = 0
    gameExit = False
    while not gameExit:
        for event in py.event.get():
            if event.type == py.QUIT:
                gameExit=True
            #code to move object to different positions
            if event.type == py.KEYDOWN:
                if event.key == py.K_LEFT:
                    posx_change = -5
                    posy_change = 0
                elif event.key == py.K_RIGHT:
                    posx_change = 5
                    posy_change = 0
                elif event.key == py.K_UP:
                    posy_change = -5
                    posx_change = 0
                elif event.key == py.K_DOWN:
                    posy_change = 5
                    posx_change = 0
            if event.type == py.KEYUP:
                if event.key == py.K_LEFT or event.key == py.K_RIGHT or event.key == py.K_UP or event.key == py.K_DOWN:
                    posx_change = 0
                    posy_change=0
        if posx >= (display_width-28) or posy >= (display_height-28) or posx <=0 or posy <= 0:
            gameExit = True

        posx+=posx_change
        posy+=posy_change
        gameDisplay.fill(orange)
        # code to draw objects and identify the location, position on location and width and height
        py.draw.ellipse(gameDisplay, black, [posx, posy, 10, 10])
        py.draw.rect(gameDisplay, white, [0, 0, 10, 600])
        py.draw.rect(gameDisplay, white, [0, 0, 600, 10])
        py.draw.rect(gameDisplay, white, [590, 5, 10, 600])
        py.draw.rect(gameDisplay, white, [5, 590, 600, 10])

        clock.tick(20)
        py.display.update()

    print_msg('GAME OVER!', black)
    py.display.update()
    #quiting the initialized game module
game_loop()

time.sleep(2)
py.quit()
quit()
