"""Flappy Bird Game"""
import random
import sys
import pygame
from pygame.locals import *

#Global Variables for the game
FPS = 32
SCREENWIDTH = 600
SCREENHEIGHT = 620
SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT)) ##depth
GROUNDY = SCREENWIDTH * 0.8
GAME_SPRITES = {}
GAME_SOUNDS = {}
PLAYER = './Images/bird1.png'
BACKGROUND = './Images/background2.jpg'
PIPE = './Images/pipe.png' 

def welcomeScreen():
   """
   Shows Welcome images on the Screen
   """
   playerx = int(SCREENWIDTH/5)        #blitting of image is done with respect to top left corner
   #playerx = int((SCREENWIDTH - GAME_SPRITES['base'].get_width())/2)
   playery = int((SCREENHEIGHT - GAME_SPRITES['player'].get_height())/2) 
   messagex = int((SCREENWIDTH - GAME_SPRITES['startMessage'].get_width())/2) 
   messagey = 0
   basex = 0
   basey = int(SCREENHEIGHT - GAME_SPRITES['base'].get_height())
   #baseY =  GROUNDY

   while True:
      for event in pygame.event.get():
         # If user clicks on cross button or presses ESP key, close the game and terminate the program.
         if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()

         # If user presses Space key or Up arrow key, start the game.
         elif event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
            return
         
         # Blit the Start Game screen images on the screen.
         else:
            SCREEN.blit(GAME_SPRITES['background'], (0, 0))
            SCREEN.blit(GAME_SPRITES['player'], (playerx, playery))
            SCREEN.blit(GAME_SPRITES['startMessage'], (messagex, messagey))
            #SCREEN.blit(GAME_SPRITES['base'], (basex, basey))

            pygame.display.update() ##flip
            fpsclock.tick(FPS)   ##less indent

#def mainGame():
   

if __name__ == "__main__": #Control of program will start from here
   pygame.init() #Initializing all Pygame modules
   fpsclock = pygame.time.Clock() 
   pygame.display.set_caption("Flappy Bird by Keshav")
   GAME_SPRITES['numbers'] = (
      pygame.image.load('./Images/0.png').convert_alpha(), #optimising  image for quick blitting
      pygame.image.load('./Images/1.png').convert_alpha(),
      pygame.image.load('./Images/2.png').convert_alpha(),
      pygame.image.load('./Images/3.png').convert_alpha(),
      pygame.image.load('./Images/4.png').convert_alpha(),
      pygame.image.load('./Images/5.png').convert_alpha(),
      pygame.image.load('./Images/6.png').convert_alpha(),
      pygame.image.load('./Images/7.png').convert_alpha(),
      pygame.image.load('./Images/8.png').convert_alpha(),
      pygame.image.load('./Images/9.png').convert_alpha()  
   )
  
   GAME_SPRITES['startMessage'] = pygame.image.load('./Images/start1.png').convert_alpha()
   GAME_SPRITES['base'] = pygame.image.load('./Images/base.png').convert_alpha()
   GAME_SPRITES['pipe'] = (
      pygame.transform.rotate(pygame.image.load(PIPE).convert_alpha(), 180),
      pygame.image.load(PIPE).convert_alpha()
   )
   GAME_SPRITES['background'] = pygame.image.load(BACKGROUND).convert()
   GAME_SPRITES['player'] = pygame.image.load(PLAYER).convert_alpha()
 
   GAME_SOUNDS['die'] = pygame.mixer.Sound('./Audios/die.mp3')
   GAME_SOUNDS['hit'] = pygame.mixer.Sound('./Audios/hit.mp3')
   GAME_SOUNDS['point'] = pygame.mixer.Sound('./Audios/point.mp3')
   GAME_SOUNDS['swoosh'] = pygame.mixer.Sound('./Audios/swoosh.mp3')
   GAME_SOUNDS['wing'] = pygame.mixer.Sound('./Audios/wing.mp3')
   
   while True:
       welcomeScreen()  #shows welcomescreen to user until any key is pressed.
       #mainGame()





