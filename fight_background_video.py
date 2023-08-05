import pygame
from moviepy.editor import VideoFileClip
pygame.init()


def fight_background_video(time,location,screen):
#Load background video
      frame_index = 0
      clock = pygame.time.Clock()
      screen_width,screen_height = screen[0],screen[1]

      if location =="DEFAULT" and time == "DAY":
         video_path = "assets/videos/location1_day.mp4"
         video_clip = VideoFileClip(video_path)
         video_clip = video_clip.resize((screen_width, screen_height))
         fps = video_clip.fps

      elif location == "OPEN CANTEEN" and time == "DAY":
         video_path = "assets/videos/location2_day.mp4"
         video_clip = VideoFileClip(video_path)
         video_clip = video_clip.resize((screen_width, screen_height))
         fps = video_clip.fps

      elif location == "DEFAULT" and time == "NIGHT":
         video_path = "assets/videos/location1_night.mp4"
         video_clip = VideoFileClip(video_path)
         video_clip = video_clip.resize((screen_width, screen_height))
         fps = video_clip.fps

      elif location == "OPEN CANTEEN" and time == "NIGHT":
         video_path = "assets/videos/location2_night.mp4"
         video_clip = VideoFileClip(video_path)
         video_clip = video_clip.resize((screen_width, screen_height))
         fps = video_clip.fps

      return video_path,video_clip,fps