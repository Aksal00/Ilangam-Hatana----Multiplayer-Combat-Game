import pygame
import random
from pygame import mixer



class music():
   def __init__(self,background_music):
      self.background_music = background_music
   def play_background_music(self):
      mixer.init()
      
      #background music of the menu
      if self.background_music == "menu_background_music":
            pygame.mixer.music.load("assets/audio/BG_Music_Menu.mp3")
            pygame.mixer.music.set_volume(0.3)
            pygame.mixer.music.play(-1,0.0,5000)  
      #backgroun music of a fight
      elif self.background_music == "fight_background_music":
         choice = random.randint(1, 2)
         if choice == 1:
            pygame.mixer.music.load("assets/audio/BG_Music_Fight_1.mp3")
            pygame.mixer.music.set_volume(0.2)
            pygame.mixer.music.play(-1,15.0,5000)
         if choice == 2:
            pygame.mixer.music.load("assets/audio/BG_Music_Fight_2.mp3")
            pygame.mixer.music.set_volume(0.2)
            pygame.mixer.music.play(-1,15.0,5000)
      #background music of the logo intro
      elif self.background_music == "intro_music":
         pygame.mixer.music.load("assets/audio/intro_audio.mp3")
         pygame.mixer.music.set_volume(1)
         pygame.mixer.music.play(-1,15.0,5000)
      #background music of a transition
      elif self.background_music == "transition":  
         transition_sound_fx = pygame.mixer.Sound("assets/audio/Transition.mp3")
         transition_sound_fx.set_volume(0.7)
         transition_sound_fx.play(loops = 0)
      
               
      else:
            pygame.mixer.music.pause()
            print("no music")
      
            

      
         
      

         