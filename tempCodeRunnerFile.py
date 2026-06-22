
import pygame

def play_music(folder,song_name,mp3_files):
     
     file_path = os.path.join(folder,song_name)#=> join folder and mp3files with a slash{\}, like original ones 
     if not os.path.exists(file_path):  
        print("file not found")
        return