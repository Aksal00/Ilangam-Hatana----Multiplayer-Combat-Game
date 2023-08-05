import pygame
import Images
import sys

pygame.init()

def cursor(screen):
  pygame.mouse.set_visible(False)
  m_x,m_y = pygame.mouse.get_pos()
  screen.blit(Images.cursor,(m_x,m_y))