import pygame
import time
pygame.init()

debounce_time = 0.5  # Adjust this value to fit your game's needs
last_click_time = 0

class Sound_Button:
    def __init__(self,image_path,pos,size,screen):

        self.img = pygame.image.load(image_path).convert_alpha()
        self.resized_image = pygame.transform.scale(self.img, (size[0], size[1]))
        self.pos = pos
        self.size = size
        self.button = pygame.rect.Rect((self.pos[0], self.pos[1]), (size[0], size[1]))
        self.screen = screen
        
    def draw(self):
        #pygame.draw.rect(self.screen, 'light gray',[self.pos[0], self.pos[1], self.size[0], self.size[1]], 5, 0)
        self.screen.blit(self.resized_image,(self.pos[0],self.pos[1]))

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
           
        else:
               
           return False