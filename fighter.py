import pygame
from pygame import mixer
from audio import music
from fighter_sounds import fighter_sounds
import random

class Fighter():
    
    def __init__(self,player,x,y,flip,data,sprite_sheet,animation_steps):
        self.player = player
        self.size = data[0]
        self.image_scale = data[1]
        self.offset = data[2]
        self.flip = flip
        self.animation_list = self.load_images(sprite_sheet,animation_steps)
        self.action = 0 #0-idel
        self.frame_index=0 
        self.image = self.animation_list[self.action][self.frame_index]        
        self.update_time= pygame.time.get_ticks()
        self.rect = pygame.Rect((x,y, 90, 270))
        self.vel_y = 0
        self.jump = False
        self.moving = False
        self.attacking= False
        self.attack_type = 0
        self.attack_cooldown = 0
        self.health = 100
        self.hit = False
        self.using_shield = False
        self.shield_sword_clash = False
        self.alive = True
        

    
    def load_images(self,sprite_sheet,animation_steps):
        #extract images from sprite sheets
        animation_list=[]
        for y,animation in enumerate(animation_steps): #enumerate:- start from y=0 and increase everytime by 1
            temp_img_list=[]
            for x in range(animation):
                temp_img = sprite_sheet.subsurface(x*self.size,y*self.size,self.size,self.size)    
                temp_img_list.append(pygame.transform.scale(temp_img,(self.size* self.image_scale,self.size* self.image_scale)))
            animation_list.append(temp_img_list)
        return animation_list
        

    def move(self,screen_width,screen_height,surface,target):
        SPEED = 10
        GRAVITY = 2
        dx = 0
        dy = 0
        self.using_shield = False
        self.moving = False
        self.attack_type = 0
        
        #get keypresses
        key = pygame.key.get_pressed()
        
        #can only perform other actions if not currently attacking
        if self.attacking == False and self.alive == True:
            #check player1_controls
            if self.player == 1:
                #movement
                #move left
                if key[pygame.K_a]:
                    dx = -SPEED
                    self.moving = True
                #move right 
                if key[pygame.K_d]:
                    dx = SPEED
                    self.moving = True
                    
                #jump
                if key[pygame.K_w] and self.jump == False:
                    self.vel_y = -37
                    self.jump = True

                #attack
                if key[pygame.K_r] or key[pygame.K_t] or key[pygame.K_g]:
                    self.attack(surface, target)
                    #determine which attack type was used
                    if key[pygame.K_r]:
                        self.attack_type = 1
                    if key[pygame.K_t]:
                        self.attack_type = 2
                    if key[pygame.K_g]:
                        self.attack_type = 3

                #shield
                if key[pygame.K_s] and self.jump == False and self.using_shield == False:
                    self.using_shield = True

            if self.player == 2:
                #movement
                if key[pygame.K_LEFT]:
                    dx = -SPEED
                    self.moving = True
                    
                if key[pygame.K_RIGHT]:
                    dx = SPEED
                    self.moving = True
                    
                #jump
                if key[pygame.K_UP] and self.jump == False:
                    self.vel_y = -37
                    self.jump = True

                #attack
                if key[pygame.K_o] or key[pygame.K_p] or key[pygame.K_k]:
                    self.attack(surface, target)
                    #determine which attack type was used
                    if key[pygame.K_p]:
                        self.attack_type = 1
                    if key[pygame.K_o]:
                        self.attack_type = 2
                    if key[pygame.K_k]:
                        self.attack_type = 3

                #shield
                if key[pygame.K_DOWN] and self.jump == False and self.using_shield == False:
                    self.using_shield = True   

                          

        #apply gravity
        self.vel_y += GRAVITY
        dy += self.vel_y

        #ensure player stays inside the screen
        if self.rect.left + dx <0:
            dx = -self.rect.left
        if self.rect.right + dx > screen_width:
            dx = screen_width - self.rect.right
        if self.rect.bottom + dy > screen_height - 60:
            self.vel_y=0
            dy = screen_height - 60 - self.rect.bottom
            self.jump = False

        #ensure players face each other
        if target.rect.centerx> self.rect.centerx:
            self.flip = False
        else:
            self.flip = True

        #apply attack cool down
        if self.attack_cooldown > 0:
           self.attack_cooldown -= 1
           


        #update player position
        self.rect.x += dx
        self.rect.y += dy

    #handle animation updates
    
    def update(self,target):
      
      #check what action the player is performing
      if self.health <= 0:
        self.health = 0
        self.alive = False
        self.update_action(9)     
          
      elif self.attacking == True:
        if self.attack_type == 1:
          self.update_action(1)
          #load attack type 1 sound
          attack_type_1_sound = fighter_sounds(0,0,0,1,0,0,0,0)
          attack_type_1_sound.play_sound_effect()
        elif self.attack_type == 2:
          self.update_action(5)
          attack_type_2_sound = fighter_sounds(0,0,0,0,1,0,0,0)
          attack_type_2_sound.play_sound_effect()
        elif self.attack_type == 3:
          self.update_action(6)
          attack_type_3_sound = fighter_sounds(0,0,0,0,0,1,0,0)
          attack_type_3_sound.play_sound_effect()
      elif self.hit == True:
        print("hit2")
        self.update_action(4)
        damage_sound = fighter_sounds(0,1,0,0,0,0,0,0)
        damage_sound.play_sound_effect()      
      elif self.using_shield == True:
        self.update_action(2)         
      elif self.moving == True and self.jump == False:
        
        self.update_action(3)
        moving_sound = fighter_sounds(1,0,0,0,0,0,0,0)
        moving_sound.play_sound_effect()
      elif self.jump == True:
        self.update_action(8)
        jump_sound = fighter_sounds(0,0,1,0,0,0,0,0)
        jump_sound.play_sound_effect()
      else:
        self.update_action(0)
      
        

      #define animation speed acording to animation number 
      if self.action == 3:
        animation_cooldown = 150
      elif self.action == 1:
        animation_cooldown = 20
      elif self.action == 5:
        animation_cooldown = 20
      elif self.action == 6:
        animation_cooldown = 34
      elif self.action == 8:
        animation_cooldown = 45
      else:
        animation_cooldown = 40

        #update image
      self.image = self.animation_list[self.action][self.frame_index]
        #check if enough time has passed since last update
      if pygame.time.get_ticks() - self.update_time > animation_cooldown:
          self.frame_index +=1
          self.update_time = pygame.time.get_ticks()
        #check if the animation has finished
      if self.frame_index >= len(self.animation_list[self.action]):
        #if the player is dead then end the animation
        if self.alive == False:
           self.frame_index = len(self.animation_list[self.action])-1
        else:
           self.frame_index = 0
           if self.action == 1 or self.action == 5 or self.action == 6:
              self.attacking = False
              self.attack_cooldown = 20
          #if damage was take
           if self.action == 4:
              self.hit = False
          #if the player was in the middle of the attack
              self.attacking = False
              self.attack_cooldown = 20
    
    def attack(self, surface,target):
        if self.attack_cooldown == 0:
            self.attacking = True
            attacking_rect = pygame.Rect(self.rect.centerx-(2*self.rect.width*self.flip), self.rect.y, 2* self.rect.width, self.rect.height)
            if attacking_rect.colliderect(target.rect) and target.using_shield == False:
                target.health -= 10
                target.hit = True
                if target.health <= 0:
                   self.moving = False
                   dead_sound = fighter_sounds(0,0,0,0,0,0,0,1)
                   dead_sound.play_sound_effect()
                   
            #When oponent is using a shield   
            if attacking_rect.colliderect(target.rect) and target.using_shield == True:
                self.shield_sword_clash = True
                target.health -= 1
                if target.health <= 0:
                   self.moving = False
                   dead_sound = fighter_sounds(0,0,0,0,0,0,0,1)
                   dead_sound.play_sound_effect()
                shield_sound = fighter_sounds(0,0,0,0,0,0,1,0)
                shield_sound.play_sound_effect()
                
    
    def update_action(self,new_action):
        #check if the new action is different to the previous one
        if new_action != self.action:
            self.action = new_action
            #update the animation settings
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()

    def draw(self, surface):
        img = pygame.transform.flip(self.image,self.flip,False)
        #pygame.draw.rect(surface,(255,0,0),self.rect)
        surface.blit(img,(self.rect.x-(self.offset[0]*self.image_scale),self.rect.y-(self.offset[1]*self.image_scale)))

    
