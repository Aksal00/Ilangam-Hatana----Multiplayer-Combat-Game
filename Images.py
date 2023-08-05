import pygame

screen_width = 1280
screen_height = int(screen_width*(9/16))

screen = pygame.display.set_mode((screen_width,screen_height))

#Loading Images
main_menu_bg_image = pygame.image.load("assets/Images/main_menu_img.png").convert_alpha()
main_menu_bg_image = pygame.transform.scale(main_menu_bg_image, (screen_width, screen_height))
aksal_games_logo_image = pygame.image.load("assets/Images/aksal_games_logo.png").convert_alpha()
aksal_games_logo_image = pygame.transform.scale(aksal_games_logo_image, (150, 150))
Ilangam_Hatana_logo_image = pygame.image.load("assets/Images/Ilangam Hatana logo.png").convert_alpha()
Ilangam_Hatana_logo_image = pygame.transform.scale(Ilangam_Hatana_logo_image, (900, 260))
key_binding_image = pygame.image.load("assets/Images/key_binding_image.png").convert_alpha()
key_binding_image = pygame.transform.scale(key_binding_image, (1100, 620))
sound_on_image = pygame.image.load("assets/Images/sound_on.png").convert_alpha()
sound_on_image = pygame.transform.scale(sound_on_image, (50, 50))
sound_off_image = pygame.image.load("assets/Images/sound_off.png").convert_alpha()
sound_off_image = pygame.transform.scale(sound_off_image, (50, 50))
paper_background_image = pygame.image.load("assets/Images/paper_background.png").convert_alpha()
paper_background_image = pygame.transform.scale(paper_background_image, (1400, 1300))
developer_image = pygame.image.load("assets\Images\developer.jpg").convert_alpha()
developer_image = pygame.transform.scale(developer_image, (299, 300))
healthbar_bg = pygame.image.load("assets\Images\healthbar_bg.png").convert_alpha()
idle = pygame.image.load("assets/Images/Fighter/Idle1.png").convert_alpha()
idle = pygame.transform.scale(idle, (100, 100))
idle_black = pygame.image.load("assets/Images/Fighter/Idle1_black.png").convert_alpha()
idle_black = pygame.transform.scale(idle_black, (100, 100))
sound_on_img = "assets\Images\sound_on.png"
sound_off_img = "assets\Images\sound_off.png"
cursor = pygame.image.load("assets/Images/cursor.png").convert_alpha()
cursor = pygame.transform.scale(cursor, (50, 50))
healthbar_guidelines = pygame.image.load("assets/Images/healthbar_guidelines.png").convert_alpha()
healthbar_guidelines = pygame.transform.scale(healthbar_guidelines, (400, 30))


def draw_black_square(position,size):
    #pygame.draw.rect(screen, 'black', [100, 100, 300, 300])
    x_pos,y_pos,square_width,square_height = position[0],position[1],size[0],size[1]
    black_square = pygame.Surface((square_width,square_height))  # the size of rect
    black_square.set_alpha(200)                # alpha level
    black_square.fill('black')           # this fills the entire surface
    screen.blit(black_square, (x_pos,y_pos))