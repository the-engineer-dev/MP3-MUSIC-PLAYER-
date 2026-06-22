import os 
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"

import pygame

def play_music(folder,song_name,mp3_files):
     
     file_path = os.path.join(folder,song_name)#=> join folder and mp3files with a slash{\}, like original ones 
     if not os.path.exists(file_path):  
        print("file not found")
        return

     pygame.mixer.music.load(file_path)
     pygame.mixer.music.play() 

     print(f"currently playing : {song_name}")
     loop = False 
     print("Commands : [P]ause,[R]esume,[S]top,[<]replay,[L]oop,[N]ext,[B]ack")


     while True:
          command = input("-> ")

          if (command.upper()=="P"):
            pygame.mixer.music.pause()
            print("Paused")

          elif (command.upper()=="R"):
                pygame.mixer.music.unpause()
                print("resumed")

          elif(command.upper()=="S"):
               pygame.mixer.music.stop()
               print("stopped")

          elif(command=="<"):
                print("replayed")
                pygame.mixer.music.stop()
                pygame.mixer.music.load(file_path)
                pygame.mixer.music.play() 

          elif(command.upper()=="L"):
                        loop = not loop
                        if loop:
                             pygame.mixer.music.play(loops=-1)
                             print("Loop ON")
                        else:
                             print("Loop OFF")
               
               
                        pygame.mixer.music.stop()
                        pygame.mixer.music.load(file_path)
                        pygame.mixer.music.play() 
          elif(command.upper()=="N"):
            current_index = mp3_files.index(song_name)
            if (current_index+1<len(mp3_files)-1):
                    play_music(folder,mp3_files[current_index+1],mp3_files) 
            else:
                 print("No next song")

          elif(command.upper()=="B"):
            current_index = mp3_files.index(song_name)
            if (current_index-1>=0):
                    play_music(folder,mp3_files[current_index-1],mp3_files) 
            else:
                 print("Cannot Go Back")
               
        


def main():

    try :
         pygame.mixer.init()# load and play audio
    except pygame.error as e :
        print("Audio Intiallisation Failed",e)
        
    
    folder="Music"

    if not os.path.isdir(folder):
        print(f"Folder'{folder}'Is Not Found")
    
    mp3_files =[file for file in os.listdir(folder) if file.endswith(".mp3") ] 

    if not mp3_files:
        print("No .mp3 files found")

    while True :
        print("==> MP3 PLAYER <==")
        print("MY SONG LIST")

        for index , song in enumerate(mp3_files , start=1):# enumerate=> used to gave the indexing to our sonngs title 
            print(f"{index}.{song}")

        choice_input  = input("\n Enter the song to play(or 'Q' to quit): ")

        if choice_input.upper() == "Q":
            print("\nMP3 PLayer Closes")
            break
        
        if not choice_input.isdigit():
                print("\nEnter the valid number ")
                continue
        
        choice = int(choice_input)-1

        if 0<=choice<=len(mp3_files):
              play_music(folder,mp3_files[choice],mp3_files)
        
        
             

        else:
             print("Invalid Choice")


if __name__=="__main__":
    main()
