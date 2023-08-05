import pygame
from pygame import mixer
import button_list
import time
mixer.init()

debounce_time = 0.5  # Adjust this value to fit your game's needs
last_click_time = 0

pygame.init()
class Button:
    def __init__(self, txt, pos,size,font,screen):
        self.text = txt
        self.pos = pos
        self.width,self.height = size
        self.button = pygame.rect.Rect((self.pos[0], self.pos[1]), (self.width, self.height))
        self.font_color = 'black'
        self.font = font
        self.screen = screen
        

    def draw(self):
        text_width,text_height = self.font.size(self.text)
        pygame.draw.rect(self.screen, 'light gray',[self.pos[0], self.pos[1], self.width, self.height], 0, 100)
        pygame.draw.rect(self.screen, 'dark gray', [self.pos[0], self.pos[1], self.width, self.height], 5, 100)
        text2 = self.font.render(self.text, True, self.font_color)
        self.screen.blit(text2, (self.pos[0] + (((self.width)/2)-(text_width/2)), self.pos[1] + 10))
        

    def check_clicked(self):

        global last_click_time
        current_time = time.time()
        if self.button.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            if current_time - last_click_time > debounce_time:
                click_sound_fx = pygame.mixer.Sound("assets/audio/click_sound.wav")
                click_sound_fx.set_volume(1)
                click_sound_fx.play()
                last_click_time = current_time
                return True
        elif self.button.collidepoint(pygame.mouse.get_pos()):
           menu_font_enlarged = pygame.font.Font("assets/fonts/ApeMount-WyPM9.ttf",27)
           self.font_color = 'red'
           text3 = menu_font_enlarged.render(self.text, True, self.font_color)
           text_width,text_height = menu_font_enlarged.size(self.text)
           pygame.draw.rect(self.screen, 'light gray',[self.pos[0]-5, self.pos[1]-5, self.width+10, self.height+10], 0, 100)
           pygame.draw.rect(self.screen, 'dark gray', [self.pos[0]-5, self.pos[1]-5, self.width+10, self.height+10], 5, 100)
           self.screen.blit(text3, (self.pos[0]-5 + (((self.width+10)/2)-(text_width/2)), self.pos[1]+7.5))
           
        else:
           text_width,text_height = self.font.size(self.text)
           self.font_color = 'black'
           text3 = self.font.render(self.text, True, self.font_color)
           self.screen.blit(text3, (self.pos[0] + (((self.width)/2)-(text_width/2)), self.pos[1] + 10))
               
           return False
        
    def selected_button(self,selected_button):
        if button_list.selected_button.check_clicked():
            pygame.draw.rect(self.screen, 'red', [self.pos[0], self.pos[1], self.width+5, self.height+5], 5, 100)
                  
        
