#######  #    #  #######  #######  #            #######  #######  #         #  #######  #######
#     #  #   #   #        #     #  #            #        #     #  # #     # #  #        #  
#######  ###     #######  #######  #            #   ###  #######  #  #   #  #  #####    ####### 
#     #  #   #         #  #     #  #            #     #  #     #  #   # #   #  #              #
#     #  #    #  #######  #     #  ########     #######  #     #  #    #    #  #######  #######
   
import pygame
import button_list
import fonts
from image_button import Image_Button
import webbrowser
from sound_button import Sound_Button
from pygame import mixer
from button import Button
from video import play_video_as_background,transition,intro
from audio import music
from Ilangam_Hatana import ilangam_hatana
from player_names import get_player_names
import Images
from cursor import cursor
from moviepy.editor import VideoFileClip


pygame.init()
mixer.init()

#defining screen size
screen_width = 1280
screen_height = int(screen_width*(9/16))
screen = pygame.display.set_mode((screen_width,screen_height),pygame.FULLSCREEN)

pygame.display.set_caption("Ilangam Hatana")
timer = pygame.time.Clock()
starting_screen = False
black_square = False
menu_state = "main"
music_state = "on"
location = "DEFAULT"
time = "DAY"
video_path = "assets/videos/menu_background.mp4"
video_clip = VideoFileClip(video_path)
# Variables for controlling the video playback
frame_index = 0
fps = video_clip.fps
clock = pygame.time.Clock()

# Resize the video to fit the screen
video_clip = video_clip.resize((screen_width, screen_height))

#function for drawing texts
def drawing_text(text,font,text_color,x,y):
   img = font.render(text,True,text_color)
   screen.blit(img,(x,y))

def open_web_address(url):
    webbrowser.open(url)

#Play Intro video
intro()
if menu_state == "main":
     transition()

#function for drawing background
def draw_menu_bg():
  # Get the current frame from the video and blit it on the screen
  music_state = "on"
  frame = video_clip.get_frame(frame_index / fps)
  frame_surface = pygame.image.fromstring(frame.tobytes(), (screen_width, screen_height), 'RGB')
  screen.blit(frame_surface, (0, 0))


if music_state == "on":
       menu_background_music = music("menu_background_music")
       menu_background_music.play_background_music()
           
run = True

while run:
  draw_menu_bg() 
  
  if starting_screen == True:
      if menu_state == "main":
         button_list.button1.draw()
         button_list.button2.draw()
         button_list.button3.draw()
         button_list.button4.draw()
         
         if music_state == "on":
                  button_list.sound_button_1.draw()       
         if music_state == "off":
                  button_list.sound_button_2.draw()
         if button_list.sound_button_1.check_clicked():
            if pygame.mixer.music.get_busy():
                  music_state = "off"
                  pygame.mixer.music.pause()
            else:
                  music_state = "on"
                  pygame.mixer.music.unpause()
                              
         if button_list.button1.check_clicked():
               menu_state = "play"
               if menu_state == "play":              
                  ilangam_hatana(time,location,music_state,1,1,0,0,True,player1_name="PLAYER 1",player2_name="PLAYER 2")
                  if music_state == "on":
                        menu_background_music = music("menu_background_music")
                        menu_background_music.play_background_music()
                  menu_state = "main" 
         if button_list.button2.check_clicked():
               menu_state = "developer"   
         if button_list.button3.check_clicked():   
               menu_state = "key_bindings"             
         if button_list.button4.check_clicked():
               menu_state = "quit"
                       
      if menu_state == "developer":
            screen.blit(Images.paper_background_image,(-70,-310))
            pygame.draw.rect(screen, 'white', [195, 165, 309, 310], 5, 5)
            screen.blit(Images.developer_image,(200,170))
            Images.draw_black_square((0,600),(1280,120))
            drawing_text("Developer" ,fonts.font1,'black',510,90)
            drawing_text("P.M. Akila Salinda Srikantha" ,fonts.font3,'black',560,220)
            drawing_text("Undergraduate(3rd year)," ,fonts.font3,'black',560,260)
            drawing_text("Department of Computer Science," ,fonts.font3,'black',560,300)
            drawing_text("University of Sri Jayewardenepura" ,fonts.font3,'black',560,340)
            button_list.button32.draw()
            button_list.button33.draw()
            button_list.button9.draw()
            

            if button_list.button32.check_clicked():             
                  open_web_address("https://www.linkedin.com/in/akila-srikantha-2693b41b9/?trk=public-profile-join-page")
            if button_list.button33.check_clicked():
                  open_web_address("https://github.com/Aksal00")   
            if button_list.button9.check_clicked():
                  menu_state = "main"

      if menu_state =="quit":
            Images.draw_black_square((0,600),(1280,120))
            drawing_text("WANNA LEAVE THE GAME?",fonts.font2,'white',470,600)
            button_list.button10.draw()
            button_list.button11.draw()

            if button_list.button10.check_clicked():
                  transition()
                  run = False
            if button_list.button11.check_clicked():
                  menu_state = "main"         

      if menu_state == "key_bindings":
            screen.blit(Images.paper_background_image,(-70,-310))
            Images.draw_black_square((0,600),(1280,120))
            button_list.button9.draw()
            screen.blit(Images.key_binding_image,(50,50))

            if button_list.button9.check_clicked():
                  menu_state = "main"
     
  else:  
    
    button_list.starting_button.draw()

    if button_list.starting_button.check_clicked():
       #main_menu = True
       black_square = True
       Images.draw_black_square((0,600),(1280,120))
       starting_screen = True
                
  #event handler
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False

  # Move to the next frame, and loop back to the beginning if the end is reached
  frame_index += 1
  if frame_index >= int(fps * video_clip.duration):
        frame_index = 0
  
  cursor(screen)
  #update display
  pygame.display.update()

pygame.quit()
