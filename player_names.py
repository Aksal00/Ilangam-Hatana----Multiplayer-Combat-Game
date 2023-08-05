import pygame
import sys
import Images
import fonts
import colors
import button_list
from button import Button
from video import play_video_as_background,transition
from cursor import cursor


def get_player_names():
    pygame.init()

    # Set up the window
    screen_width = 1280
    screen_height = int(screen_width*(9/16))

    screen = pygame.display.set_mode((screen_width,screen_height))
    pygame.display.set_caption("Ilangam Hatana")


    def drawing_text(text,font,text_color,x,y):
        img = font.render(text,True,text_color)
        screen.blit(img,(x,y))

    def check_clicked(rect):
        if rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            return True

    # Text input boxes
    player1_input = "PLAYER 1"
    player2_input = "PLAYER 2"
    active_input = 1
    count_1 = 8
    count_2 = 8
    no_of_rounds = 3
    location = "DEFAULT"
    time = "DAY"
    location_selected = 0
    input_menu = True

    while True:
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
 #getting player names
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_TAB:
                    active_input = 2 if active_input == 1 else 1
                elif event.key == pygame.K_RETURN:
                    if active_input == 1:
                        active_input = 2
                    elif active_input == 2:
                        active_input = 1
                        
                elif event.key == pygame.K_UP:
                    if active_input == 2:
                        active_input = 1
                elif event.key == pygame.K_DOWN:
                    if active_input == 1:
                        active_input = 2

                elif event.key == pygame.K_BACKSPACE :
                    if active_input == 1 and count_1 > 0:
                        player1_input = player1_input[:-1]
                        count_1 -= 1
                    elif active_input == 2 and count_2 > 0:
                        player2_input = player2_input[:-1]
                        count_2 -= 1
                elif 32 <= event.key <= 126:
                    if active_input == 1 and count_1 <= 14 :
                        player1_input += event.unicode 
                        count_1 += 1
                        

                    elif active_input == 2 and count_2 <= 14 :
                        player2_input += event.unicode
                        count_2 += 1
                                    
        #screen.fill(WHITE)
        if input_menu == True and location_selected == 0:
            screen.blit(Images.main_menu_bg_image, (0,0))
            screen.blit(Images.paper_background_image, (-70,-310))
            screen.blit(Images.idle, (200,100))
            screen.blit(Images.idle_black, (200,160))
            Images.draw_black_square((0,600),(1280,120))
            button_list.button14.draw()
            button_list.button15.draw()
            button_list.button16.draw()
            button_list.button17.draw()
            button_list.button26.draw()
            button_list.button27.draw()
            button_list.image_button_3.draw()
            button_list.image_button_4.draw()


            if button_list.button14.check_clicked():
                no_of_rounds = 1
            if button_list.button15.check_clicked():
                no_of_rounds = 3
            if button_list.button16.check_clicked():
                no_of_rounds = 5
            if button_list.image_button_3.check_clicked():
                     time = "DAY"
                     button_list.image_button_3.selected_image_button(time,"DAY")
            if button_list.image_button_4.check_clicked():
                     time = "NIGHT"
                     button_list.image_button_4.selected_image_button(time,"NIGHT")
            if time == "DAY":
                     rect5 = pygame.draw.rect(screen, 'red', [630, 490, 160, 90], 5, 0)
            if time == "NIGHT":
                     rect6 = pygame.draw.rect(screen, 'red', [880, 490, 160, 90], 5, 0)
            if button_list.button17.check_clicked():
                transition()
                return time,location,0,0,0,0,"",""
            if button_list.button26.check_clicked() and count_1 !=0 and count_2 !=0:
                transition()
                return time,location,no_of_rounds,1,0,0,player1_input,player2_input
            if count_1 == 15 and active_input == 1:
                    drawing_text("Maximum character limit has reached!",fonts.menu_font,'red',525,175)
            if count_1 == 0 and active_input == 1:
                    drawing_text("Please enter a name for player 1!",fonts.menu_font,'red',525,175)  
            if count_2 == 15 and active_input == 2:
                    drawing_text("Maximum character limit has reached",fonts.menu_font,'red',525,235)
            if count_2 == 0 and active_input == 2:
                    drawing_text("Please enter a name for player 2!",fonts.menu_font,'red',525,235)
            if no_of_rounds == 1:      
                    rect3 = pygame.draw.rect(screen, 'red', [295, 315, 110, 50], 5, 100)
            elif no_of_rounds == 3:
                    rect4 = pygame.draw.rect(screen, 'red', [595, 315, 110, 50], 5, 100)
            elif no_of_rounds == 5:
                    rect5 = pygame.draw.rect(screen, 'red', [895, 315, 110, 50], 5, 100)
            # Render player names
            player_names_text = fonts.font.render("ENTER PLAYER NAMES", True, colors.BLACK)
            player1_text = fonts.font.render("PLAYER 1 NAME:  " + player1_input, True, colors.BLACK)
            player2_text = fonts.font.render("PLAYER 2 NAME:  " + player2_input, True, colors.BLACK)
            No_of_rounds_text = fonts.font.render("NUMBER OF ROUNDS: " + str(no_of_rounds), True, colors.BLACK)
            Location_text = fonts.font.render("LOCATION: " + location, True, colors.BLACK)
            Time_text = fonts.font.render("TIME: " + time, True, colors.BLACK)

            # Display active input
            active_color = colors.WHITE if active_input == 1 else colors.BLACK
            rect1 = pygame.draw.rect(screen, active_color, (fonts.font.render(player1_input+"   ",True,colors.BLACK)).get_rect(topleft=(525, 148)), 2,6)
            active_color = colors.WHITE if active_input == 2 else colors.BLACK
            rect2 = pygame.draw.rect(screen, active_color, (fonts.font.render(player2_input+"   ",True,colors.BLACK)).get_rect(topleft=(525, 208)), 2,6)

            screen.blit(player_names_text, (270, 90))
            screen.blit(player1_text, (290, 150))
            screen.blit(player2_text, (290, 210))
            screen.blit(No_of_rounds_text,(270,270))
            screen.blit(Location_text,(270,410))
            screen.blit(Time_text,(270,470))

            if check_clicked(rect1):
                active_input = 1
            elif check_clicked(rect2):
                active_input = 2

        if button_list.button27.check_clicked():
            location_selected = 1 
            input_menu = False

        if location_selected == 1 and input_menu == False:    
                screen.blit(Images.main_menu_bg_image, (0,0))
                screen.blit(Images.paper_background_image, (-70,-310))
                button_list.image_button_1.draw()
                button_list.image_button_2.draw()
                Images.draw_black_square((0,600),(1280,120))
                drawing_text("SELECT A LOCATION",fonts.menu_font_large,'Black',470,70)
                drawing_text("DEFAULT",fonts.menu_font,'Black',270,135)
                drawing_text("OPEN CANTEEN",fonts.menu_font,'Black',790,135)
                drawing_text("SELECTED LOCATION :- " +location,fonts.menu_font,'white',430,670)
                
                button_list.button31.draw()

                if button_list.image_button_1.check_clicked():
                     location = "DEFAULT"
                     button_list.image_button_1.selected_image_button(location,"DEFAULT")
                if button_list.image_button_2.check_clicked():
                     location = "OPEN CANTEEN"
                     button_list.image_button_2.selected_image_button(location,"OPEN CANTEEN")
                if button_list.button31.check_clicked():
                                input_menu = True
                                location_selected = 0
                if location == "DEFAULT":
                     rect3 = pygame.draw.rect(screen, 'red', [165, 165, 340, 180], 5, 0)
                     drawing_text("DEFAULT",fonts.menu_font,'red',270,135)         
                elif location == "OPEN CANTEEN":
                     rect4 = pygame.draw.rect(screen, 'red', [715, 165, 340, 180], 5, 0)
                     drawing_text("OPEN CANTEEN",fonts.menu_font,'red',790,135)

        
        cursor(screen)
        pygame.display.flip() 
        
        

if __name__ == "__main__":
    time,location,no_of_rounds,starting_round,player1_score,player2_score,player1_name, player2_name = get_player_names()
    print("Player 1 Name:", player1_name)
    print("Player 2 Name:", player2_name)

    