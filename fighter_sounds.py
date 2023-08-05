import pygame
import random
from pygame import mixer

mixer.init()

class fighter_sounds():
    def __init__(self,moving_sound,damage_sound,jump_sound,attack_type_1,attack_type_2,attack_type_3,shield_sound,dead_sound):
      self.moving_sound = moving_sound
      self.damage_sound = damage_sound
      self.jump_sound = jump_sound
      self.attack_type_1 = attack_type_1
      self.attack_type_2 = attack_type_2
      self.attack_type_3 = attack_type_3
      self.shield_sound = shield_sound
      self.dead_sound = dead_sound


    def play_sound_effect(self):
      if self.moving_sound == 1:
         moving_fx = pygame.mixer.Sound("assets/audio/moving.wav")
         moving_fx.set_volume(0.1)
         moving_fx.play(loops = 0)

      if self.jump_sound == 1:
         j = random.randint(1,2)
         if j == 1:
            jump_sound_fx = pygame.mixer.Sound("assets/audio/jump_1.ogg")
            jump_sound_fx.set_volume(0.5)
            jump_sound_fx.play(loops = 0)
         else:
            jump_sound_fx = pygame.mixer.Sound("assets/audio/jump_2.ogg")
            jump_sound_fx.set_volume(0.5)
            jump_sound_fx.play(loops = 0)


      if self.attack_type_1 == 1:
         attack_type_1_swordfx = pygame.mixer.Sound("assets/audio/attack_type_1_sword.wav")
         attack_type_1_swordfx.set_volume(0.7)
         attack_type_1_swordfx.play(loops = 0)
         attack_type_1_fighterfx = pygame.mixer.Sound("assets/audio/attack_type_1_fighter.wav")
         attack_type_1_fighterfx.set_volume(0.5)
         attack_type_1_fighterfx.play(loops = 0)

      if self.attack_type_2 == 1:
         attack_type_1_swordfx = pygame.mixer.Sound("assets/audio/attack_type_2_sword.wav")
         attack_type_1_swordfx.set_volume(0.7)
         attack_type_1_swordfx.play(loops = 0)
         attack_type_2_fighterfx = pygame.mixer.Sound("assets/audio/attack_type_2_fighter.wav")
         attack_type_2_fighterfx.set_volume(0.5)
         attack_type_2_fighterfx.play(loops = 0)
      
      if self.attack_type_3 == 1:
         attack_type_3_swordfx = pygame.mixer.Sound("assets/audio/attack_type_3_sword.wav")
         attack_type_3_swordfx.set_volume(0.7)
         attack_type_3_swordfx.play(loops = 0)
         attack_type_3_fighterfx = pygame.mixer.Sound("assets/audio/attack_type_3_fighter.wav")
         attack_type_3_fighterfx.set_volume(0.5)
         attack_type_3_fighterfx.play(loops = 0)

      if self.shield_sound == 1:
         shield_sound_fx = pygame.mixer.Sound("assets/audio/shield_sound.wav")
         shield_sound_fx.set_volume(1)
         shield_sound_fx.play(loops = 0)
      
      if self.dead_sound == 1:
         dead_sound_fx = pygame.mixer.Sound("assets/audio/dead.wav")
         dead_sound_fx.set_volume(0.6)
         dead_sound_fx.play(loops = 0)
         
      if self.damage_sound == 1:   
         damage_sound_fx = pygame.mixer.Sound("assets/audio/damage_2.wav")
         damage_sound_fx.set_volume(0.5)
         damage_sound_fx.play(loops = 0)
      

