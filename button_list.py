import pygame
from button import Button 
from image_button import Image_Button
from sound_button import Sound_Button


screen_width = 1280
screen_height = int(screen_width*(9/16))
screen = pygame.display.set_mode((screen_width,screen_height))
menu_font = pygame.font.Font("assets/fonts/ApeMount-WyPM9.ttf",24)

#defining Main menu buttons
starting_button = Button('CLICK TO START', (500, 550),(260,40),menu_font,screen)
button1 = Button('PLAY', (50, 605),(260,40),menu_font,screen)
button2 = Button('DEVELOPER', (650, 605),(260,40),menu_font,screen)
button3 = Button('KEY BINDINGS', (350, 605),(260,40),menu_font,screen)
button4 = Button('QUIT', (950, 605),(260,40),menu_font,screen)
#options menu buttons
button5 = Button('DEFAULT', (210, 70),(320,40),menu_font,screen)
button6 = Button('AHALA WALA', (210, 320),(320,40),menu_font,screen)
button7 = Button('OPEN CANTEEN', (750, 70),(320,40),menu_font,screen)
button8 = Button('GAL PITTENIYA', (750, 320),(320,40),menu_font,screen)
button9 = Button('BACK TO MAIN MENU', (700, 650),(360,40),menu_font,screen)
button10 = Button('YES', (400, 655),(200,40),menu_font,screen)
button11 = Button('NO', (700, 655),(200,40),menu_font,screen)
button12 = Button('ON', (900, 55),(200,40),menu_font,screen)
button13 = Button('OFF', (1080, 55),(200,40),menu_font,screen)
#player names page buttons
button14 = Button('1', (300, 320),(100,40),menu_font,screen)
button15 = Button('3', (600, 320),(100,40),menu_font,screen)
button16 = Button('5', (900, 320),(100,40),menu_font,screen)
button17 = Button('BACK TO MAIN MENU', (700, 650),(320,40),menu_font,screen)
#Ilangam Hatana Buttons
button18 = Button('PAUSE', (560, 10),(160,40),menu_font,screen)
button19 = Button('RESUME', (50, 670),(260,40),menu_font,screen)
button20 = Button('KEY BINDINGS', (650, 670),(260,40),menu_font,screen)
button21 = Button('QUIT', (950, 670),(260,40),menu_font,screen)
button22 = Button('NEW GAME', (350, 670),(260,40),menu_font,screen)
button23 = Button('BACK TO PAUSE MENU', (450, 600),(360,40),menu_font,screen)
button24 = Button('YES', (400, 655),(200,40),menu_font,screen)
button25 = Button('NO', (700, 655),(200,40),menu_font,screen)
button26 = Button('PLAY', (280, 650),(150,40),menu_font,screen)
button27 = Button('CHANGE LOCATION',(700,400),(320,40),menu_font,screen)
button28 = Button('BACK',(700, 650),(150,40),menu_font,screen)
button29 = Button('CONTINUE',(540, 300),(200,40),menu_font,screen)
button30 = Button('CONTINUE',(540, 390),(200,40),menu_font,screen)
button31 = Button('BACK', (550, 610),(150,40),menu_font,screen)
#developer page buttons 
button32 = Button('LINKEDIN',(350, 530),(210,40),menu_font,screen)
button33 = Button('GITHUB', (650, 530),(210,40),menu_font,screen)

#Image_buttons
image_button_1 = Image_Button("assets/Images/Location1.png",[165, 165],[340, 180],screen)         
image_button_2 = Image_Button("assets/Images/Location2.png",[715, 165],[340, 180],screen)
image_button_3 = Image_Button("assets/Images/day_button.jpg",[630, 490],[160, 90],screen)
image_button_4 = Image_Button("assets/Images/night_button.jpg",[880, 490],[160, 90],screen)

#sound_button
sound_button_1 = Sound_Button("assets/Images/sound_on.png",[1200, 30],[40, 40],screen)
sound_button_2 = Sound_Button("assets/Images/sound_off.png",[1200, 30],[40, 40],screen)
sound_button_3 = Sound_Button("assets/Images/sound_on.png",[620, 60],[40, 40],screen)
sound_button_4 = Sound_Button("assets/Images/sound_off.png",[620, 60],[40, 40],screen)