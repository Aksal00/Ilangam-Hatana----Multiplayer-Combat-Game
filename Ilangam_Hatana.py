import pygame
import sys
import button_list
import Images
import fonts
import colors
import random
from pygame import mixer
from fighter import Fighter
from fight_background_video import fight_background_video
from audio import music
from fighter_sounds import fighter_sounds
from button import Button
from player_names import get_player_names
from video import transition
from moviepy.editor import VideoFileClip
from sound_button import Sound_Button
from cursor import cursor

mixer.init()
pygame.init()

class ilangam_hatana():
   def __init__(self,time,location,music_state,No_of_rounds,current_round,player1_score,player2_score,new_game_rules,player1_name,player2_name):
      self.music_state = music_state
      self.background_image = location
      self.No_of_rounds = No_of_rounds
      self.current_round = current_round
      self.player1_score = player1_score
      self.player2_score = player2_score
      self.player1_name = player1_name
      self.player2_name = player2_name
      self.new_game_rules = new_game_rules
      #screen size
      screen_width = 1280
      screen_height = int(screen_width*(9/16))

      screen = pygame.display.set_mode((screen_width,screen_height))
      screen_res = (screen_width,screen_height)
      pygame.display.set_caption("Ilangam Hatana")
      
      #set framerate
      clock = pygame.time.Clock()
      FPS = 60

      #define count variables
      intro_count = 4
      last_count_update = pygame.time.get_ticks()
      

      #define fighter variables
      warrior1_size = 300
      warrior1_offset = [120,103]
      warrior1_scale = 1.7
      warrior1_data = [warrior1_size,warrior1_scale,warrior1_offset]
      warrior2_size = 300
      warrior2_offset = [125,103]
      warrior2_scale = 1.7
      warrior2_data = [warrior2_size,warrior2_scale,warrior2_offset]
      
      
    
      pause_button_clicked = False
      pause_menu = False
      key_bindings = False
      pause_menu_state = "off"
      new_game_state = False
      frame_index = 0
      

      #Load spritesheets
      warrior1_sheet = pygame.image.load("assets\Images\Fighter\sprite sheet- ilangam fighter_1.png").convert_alpha()
      warrior2_sheet = pygame.image.load("assets\Images\Fighter\sprite sheet- ilangam fighter_2.png").convert_alpha()
      #define number of steps in each animation
      warrior1_animation_steps = [10,9,6,2,4,10,10,10,10,9]
      warrior2_animation_steps = [10,9,6,2,4,10,10,10,10,9]

      
      #get keypresses
      key = pygame.key.get_pressed()

      #function for drawing texts
      def drawing_text(text,font,text_color,x,y):
        img = font.render(text,True,text_color)
        screen.blit(img,(x,y))
      

      #function for drawing fighter health bar
      def draw_health_bar(health,x,y):
        ratio = health /100
        pygame.draw.rect(screen,colors.WHITE,(x-3,y-3,406,36),0,15,15,15,15)
        pygame.draw.rect(screen,colors.RED,(x,y,400,30),0,10,10,10,10)
        pygame.draw.rect(screen,colors.GREEN, (x,y,400*ratio,30),0,10,10,10,10)
        screen.blit(Images.healthbar_guidelines,(x,y))
      
      
      if new_game_rules == True:
        music_state = "on"
        if music_state == "on":
          Fight_background_music = music("fight_background_music")
          Fight_background_music.play_background_music()
        time,location,No_of_rounds,current_round,player1_score,player2_score,player1_name, player2_name = get_player_names()
        if No_of_rounds==0 and current_round== 0 and player1_score == 0 and player2_score == 0 and player1_name == "" and  player2_name == "":
          return
      video_path,video_clip,fps = fight_background_video(time,location,screen_res)
        

      #function for drawing background
      def draw_bg_elements():
            screen.blit(Images.healthbar_bg,(0,0))
            #show player stats
            draw_health_bar(fighter_1.health,50,20)
            draw_health_bar(fighter_2.health,830,20)
            #show player names
            drawing_text(player1_name,fonts.menu_font,'white',50,60)
            drawing_text(player2_name,fonts.menu_font,'white',830,60)
            
            if player1_score > 0:
               drawing_text(str(player1_score),fonts.menu_font,'red',430,60)
            else:
               drawing_text(str(player1_score),fonts.menu_font,'white',430,60)
    
            if player2_score > 0:
               drawing_text(str(player2_score),fonts.menu_font,'red',1210,60)
            else:
               drawing_text(str(player2_score),fonts.menu_font,'white',1210,60)
               
            
      #load fight_background music
      Fight_background_music = music("fight_background_music")
      Fight_background_music.play_background_music()
      

      #create two instances of fighters
      fighter_1 = Fighter(1,280, 390,False,warrior1_data, warrior1_sheet,warrior1_animation_steps)
      fighter_2 = Fighter(2,900, 390,True,warrior2_data,warrior2_sheet,warrior2_animation_steps)
      
      #game loop
      run = True
      while run:
        #Draw Background
        
        frame = video_clip.get_frame(frame_index / fps)
        frame_surface = pygame.image.fromstring(frame.tobytes(), (screen_width, screen_height), 'RGB')
        screen.blit(frame_surface, (0, 0))

        draw_bg_elements()

        if music_state == "on":          
                  button_list.sound_button_3.draw()
                  
        if music_state == "off":          
                  button_list.sound_button_4.draw()
                  
        if button_list.sound_button_3.check_clicked() or button_list.sound_button_4.check_clicked():
            if pygame.mixer.music.get_busy():
                  music_state = "off"
                  pygame.mixer.music.pause()
            else:
                  music_state = "on"
                  pygame.mixer.music.unpause()
        
        clock.tick(FPS)

        #Update Count down
        if intro_count <= -1 and pause_menu == False:   
          #move_fighters  
            fighter_1.move(screen_width,screen_height, screen, fighter_2)
            fighter_2.move(screen_width,screen_height, screen, fighter_1)
            
            
            if current_round < No_of_rounds:
              if No_of_rounds > 1:
               if fighter_1.health <=0:
                  text_width,text_height = fonts.round_over_font.size(player2_name + " WINS ROUND " + str(current_round))
                  drawing_text(player2_name + " WINS ROUND " + str(current_round),fonts.round_over_font,colors.RED, ((screen_width/2)-(text_width/2)),(screen_height/3)-80)
                  button_list.button29.draw()

                  if button_list.button29.check_clicked():
                      ilangam_hatana(time,location,music_state,No_of_rounds,current_round+1,player1_score,player2_score+1,False,player1_name,player2_name)
                      return
               if fighter_2.health <=0:
                  text_width,text_height = fonts.round_over_font.size(player1_name + " WINS ROUND " + str(current_round))         
                  drawing_text(player1_name + " WINS ROUND " + str(current_round),fonts.round_over_font,colors.RED, ((screen_width/2)-(text_width/2)),(screen_height/3)-80)
                  button_list.button29.draw()
                  
                  if button_list.button29.check_clicked(): 
                      ilangam_hatana(time,location,music_state,No_of_rounds,current_round+1,player1_score+1,player2_score,False,player1_name,player2_name)
                      return
            
            
            if No_of_rounds == 1 or No_of_rounds == current_round:
               if fighter_1.health <=0:
                  Images.draw_black_square((0,0),(1280,380))
                  text_width,text_height = fonts.round_over_font.size(player2_name + " WINS ROUND "+ str(current_round))
                  drawing_text(player2_name + " WINS ROUND "+ str(current_round),fonts.round_over_font,colors.RED, ((screen_width/2)-(text_width/2)),(screen_height/3)+60)
                  drawing_text(str(player1_score) + " : " + str(player2_score+1),fonts.round_over_font,colors.WHITE, (screen_width/2)-60,(screen_height/3)-10)
                  if player1_score > (player2_score+1):
                     text_width,text_height = fonts.round_over_font.size(player1_name + " WINS THE BATTLE!")
                     drawing_text(player1_name + " WINS THE BATTLE!",fonts.round_over_font,colors.YELLOW, ((screen_width/2)-(text_width/2)),(screen_height/3)-80)
                  else:
                     text_width,text_height = fonts.round_over_font.size(player2_name + " WINS THE BATTLE!")
                     drawing_text(player2_name + " WINS THE BATTLE!",fonts.round_over_font,colors.YELLOW, ((screen_width/2)-(text_width/2)),(screen_height/3)-80)
                     
                  button_list.button30.draw()
                  
                  if button_list.button30.check_clicked():
                      transition()
                      if music_state == "on":
                          menu_background_music = music("fight_background_music")
                          menu_background_music.play_background_music() 
                      return
               if fighter_2.health <=0:
                  Images.draw_black_square((0,0),(1280,380))
                  text_width,text_height = fonts.round_over_font.size(player1_name + " WINS ROUND "+ str(current_round))
                  drawing_text(player1_name + " WINS ROUND "+ str(current_round),fonts.round_over_font,colors.RED, ((screen_width/2)-(text_width/2)),(screen_height/3)+60)
                  drawing_text(str(player1_score+1) + " : " + str(player2_score),fonts.round_over_font,colors.WHITE, (screen_width/2)-60,(screen_height/3)-10)
                  if (player1_score+1) > player2_score:
                     text_width,text_height = fonts.round_over_font.size(player1_name + " WINS THE BATTLE!")
                     drawing_text(player1_name + " WINS THE BATTLE!",fonts.round_over_font,colors.YELLOW, ((screen_width/2)-(text_width/2)),(screen_height/3)-80)
                  else:
                     text_width,text_height = fonts.round_over_font.size(player2_name + " WINS THE BATTLE!")
                     drawing_text(player2_name + " WINS THE BATTLE!",fonts.round_over_font,colors.YELLOW, ((screen_width/2)-(text_width/2)),(screen_height/3)-80)
                  
                  button_list.button30.draw()
                  
                  if button_list.button30.check_clicked():
                      transition() 
                      if music_state == "on":
                          menu_background_music = music("menu_background_music")
                          menu_background_music.play_background_music() 
                      return
            
        elif(intro_count>-2) and pause_menu == False:
          #display count timer
          if(intro_count>0):
            drawing_text("ROUND "+ str(current_round),fonts.round_font,colors.WHITE, (screen_width/2)-170,(screen_height/3)-100)
            if (intro_count<4):
                  drawing_text(str(intro_count),fonts.count_font,colors.RED, screen_width/2-30,screen_height/3)
              
                  
          if(intro_count<1):
            drawing_text("FIGHT!",fonts.round_font,colors.RED, (screen_width/2)-155,(screen_height/3)-100)
          
          #update count timer
          if (pygame.time.get_ticks() - last_count_update) >= 1000:
              intro_count -= 1
              last_count_update = pygame.time.get_ticks()
              



      #update fighters
        if pause_menu == False:
          fighter_1.update(fighter_2)
          fighter_2.update(fighter_1)
            
                

      #draw fighters
        fighter_1.draw(screen)
        fighter_2.draw(screen)
        
        if pause_button_clicked == False:
          button_list.button18.draw()
          if button_list.button18.check_clicked() or key[pygame.K_ESCAPE]:
            pause_menu = True
            pause_menu_state = "on"
            pause_button_clicked = True

        if pause_menu == False:
          pause_menu_state = "off"
               
        if pause_menu == True:
           
          Images.draw_black_square((0,600),(1280,120))
          drawing_text("PAUSE MENU",fonts.menu_font,'white',580,620)
          if pause_menu_state == "on" and new_game_state == False:
            button_list.button19.draw()
            button_list.button20.draw()
            button_list.button21.draw()
            button_list.button22.draw()
          if button_list.button22.check_clicked():
                new_game_state = True
                pause_menu = True
                pause_menu_state = "on"

          if pause_menu == True and pause_menu_state == "on":
             
            if key_bindings == False: 
              if button_list.button19.check_clicked():
                pause_menu = False
                pause_menu_state = "off"
                pause_button_clicked = False
              if button_list.button21.check_clicked():
                music_state == "on"
                transition()
                if music_state == "on":
                  menu_background_music = music("menu_background_music")
                  menu_background_music.play_background_music()
                return 
                
              if button_list.button20.check_clicked():
                pause_menu = True
                key_bindings = True
            if key_bindings == True:
              screen.blit(Images.paper_background_image,(-70,-310))
              Images.draw_black_square((0,600),(1280,120))
              button_list.button23.draw()
              screen.blit(Images.key_binding_image,(50,50))
              
              if button_list.button23.check_clicked():
                    pause_menu = True
                    pause_menu_state = "on"
                    key_bindings = False
 
            if new_game_state == True:
                    transition()
                    ilangam_hatana(time,location,music_state,No_of_rounds,1,0,0,True,player1_name="PLAYER 1",player2_name="PLAYER 2")
                    return
  
      #event handler
        for event in pygame.event.get():
          if event.type == pygame.QUIT:
            run = False
            sys.exit()
          
            
  
         
          if event.type == pygame.KEYDOWN:  

                  if event.key == pygame.K_ESCAPE and pause_menu == False:
                      pause_menu = True
                      pause_menu_state = "on"
                      pause_button_clicked = True
                  elif event.key == pygame.K_ESCAPE and pause_menu == True:
                      pause_menu = False
                      pause_menu_state = "off"
                      pause_button_clicked = False

        

        frame_index += 1
        if frame_index >= int(fps * video_clip.duration):
              frame_index = 0

        cursor(screen)
        #update display
        pygame.display.update()


      pygame.quit()
      quit()