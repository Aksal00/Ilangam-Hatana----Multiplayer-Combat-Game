import pygame
import sys
from pygame import mixer
from moviepy.editor import VideoFileClip
from audio import music

pygame.init()

def transition():
    video_path = "assets/videos/transition.mp4"
    play_video_as_background(video_path,1,"transition")
    return

def intro():
    video_path = "assets/videos/aksal_games_intro.mp4"
    play_video_as_background(video_path,1,"intro")
    return

def play_video_as_background(video_path, repeat_times=1,sound=""):
    pygame.init()
    mixer.init()
    
    # Set up the window
    screen_width = 1280 
    screen_height = int(screen_width*(9/16))
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Ilangam Hatana")

    
    if sound =="intro":
        intro_background_music = music("intro_music")
        intro_background_music.play_background_music()
    
    if sound == "transition":
        intro_background_music = music("transition")
        intro_background_music.play_background_music()

    # Load the video file
    video_clip = VideoFileClip(video_path)

    # Resize the video to fit the screen
    video_clip = video_clip.resize((screen_width, screen_height))

    # Variables for controlling the video playback
    frame_index = 0
    fps = video_clip.fps
    clock = pygame.time.Clock()

    while repeat_times > 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN or pygame.mouse.get_pressed()[0]: 
                return

        # Get the current frame from the video and blit it on the screen
        frame = video_clip.get_frame(frame_index / fps)
        frame_surface = pygame.image.fromstring(frame.tobytes(), (screen_width, screen_height), 'RGB')
        screen.blit(frame_surface, (0, 0))
        
        pygame.display.flip()
        

        # Move to the next frame, and loop back to the beginning if the end is reached
        frame_index += 1
        if frame_index >= int(fps * video_clip.duration):
            frame_index = 0
            repeat_times -= 1

        # Control the frame rate to match the video's frame rate
        clock.tick(fps)

if __name__ == "__main__":
    # Replace "path_to_your_video_file.mp4" with the actual path to your video file
    video_path = "path_to_your_video_file.mp4"

    # The video will repeat 3 times before stopping (change the number as needed)
    repeat_times = 1
    sound = ""
    play_video_as_background(video_path, repeat_times,sound)
