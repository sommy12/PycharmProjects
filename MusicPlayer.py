from tkinter import *
from tkinter import ttk, filedialog as fd, messagebox as ms, font
from ttkthemes import themed_tk as tk
import pygame
import time
import os
from PIL import Image, ImageTk
from mutagen.mp3 import MP3
import threading
import moviepy.editor as mp

pygame.init()
root = tk.ThemedTk()
root.get_themes()
root.set_theme('arc')
root.iconbitmap('sing_4td_icon.ico')
root.geometry('1250x650')
root.title('MUSIC_PLAYER')

fonts = font.Font(family='Verdana', size=12, weight='bold')
photo = ImageTk.PhotoImage(Image.open('beyond-belief-948952.jpg'))
play_photo = ImageTk.PhotoImage(Image.open('play-button.png'))
pause_photo = ImageTk.PhotoImage(Image.open('pause.png'))
stop_photo = ImageTk.PhotoImage(Image.open('stop.png'))

playlist = []
paused = False

#functions
class functions():
    def open_file(self):
        self.filepath = fd.askopenfilename()
        print(self.filepath)
        main.add_to_playlist()

    def add_to_playlist(self):
        self.file = os.path.basename(self.filepath)
        index = 0
        list.insert(index, self.file)
        playlist.insert(index, self.filepath)
        index += 1
        list.pack(fill=Y, side='left')

    def play_file(self):
        global paused
        if paused:
            pygame.mixer_music.unpause()
            if len(self.nowplaying) >= 25:
                nowplaying_frame.config(text='Now_Playing-:-' + self.nowplaying[0:25] + '...')
            else:
                nowplaying_frame.config(text='Now_Playing-:-' + self.nowplaying)
            paused = False
        else:
            try:
                global played
                self.selectedsong = list.curselection()
                self.selectedsongs = int(self.selectedsong[0])
                self.playsong = playlist[self.selectedsongs]
                print(self.playsong)
                pygame.mixer_music.load(self.playsong)
                pygame.mixer_music.play()
                self.nowplaying = os.path.basename(self.playsong)
                root.title(self.nowplaying)


                # length of music config
                mp3_file_len = os.path.splitext(self.file)
                if mp3_file_len[1] == '.mp3':
                    audio = MP3(self.playsong)
                    self.total_length = audio.info.length
                else:
                    wav_file_len = pygame.mixer.Sound(self.playsong)
                    self.total_length = wav_file_len.get_length()

                mins, secs = divmod(self.total_length, 60)
                min = round(mins)
                sec = round(secs)
                time_format = '{:02d}:{:02d}'.format(min, sec)
                music_lenght_label.config(text=time_format)
                t1 = threading.Thread(target=main.time_details, args=(self.total_length,))
                t1.start()
                main.currenttime()
                if len(self.nowplaying) >= 25:
                    nowplaying_frame.config(text='Now_Playing-:-' + self.nowplaying[0:25] + '...')
                else:
                    nowplaying_frame.config(text='Now_Playing-:-' + self.nowplaying)
            except:
                ms.showinfo('WARNING', "Couldn't play song! \n Try Selecting a Song" )

    def currenttime(self):
        pass

    def time_details(self, t):
        global paused
        global rewind
        value = 0
        x = 0
        while x <= t and pygame.mixer_music.get_busy():
            if paused:
                continue
            else:
                mins, secs = divmod(x, 60)
                min = round(mins)
                sec = round(secs)
                time_format = '{:02d}:{:02d}'.format(min, sec)
                music_current_time_label.config(text=time_format)
                time.sleep(1)
                x += 1
                value += 1

                p.config(value=value, maximum=self.total_length)

    def pausefile(self):
        global paused
        paused = True
        pygame.mixer_music.pause()
        if len(self.nowplaying) >= 25:
            nowplaying_frame.config(text='Music_Paused-:-' + self.nowplaying[0:25] + '...')
        else:
            nowplaying_frame.config(text='Music_Paused-:-' + self.nowplaying)


    def stop_file(self):
       pygame.mixer_music.stop()
       if len(self.nowplaying) >= 25:
           nowplaying_frame.config(text='Music_Stopped-:-' + self.nowplaying[0:25] + '...')
       else:
           nowplaying_frame.config(text='Music_Stopped-:-' + self.nowplaying)


    def set_volume(self, val=99):
        volume = int(val) / 100
        pygame.mixer_music.set_volume(volume)


main = functions()



#menu config
menu = Menu(root)
root.config(bg='silver', menu=menu)

submenu1 = Menu(menu, bg='grey', fg='white', activebackground='silver')
submenu2 = Menu(menu, bg='grey', fg='white', activebackground='silver')

menu.add_cascade(menu=submenu1, label='File')
menu.add_separator()
menu.add_separator()
menu.add_cascade(menu=submenu2, label='Media')


submenu1.add_command(label='Open', command=main.open_file)
submenu1.add_command(label='Playlist')
submenu1.add_separator()


submenu2.add_command(label='Play', command=main.play_file)
submenu2.add_command(label='Pause', command=main.pausefile)
submenu2.add_separator()
submenu2.add_command(label='Stop', command=main.stop_file)
submenu2.add_separator()
submenu2.add_command(label='Exit', command = root.quit)


#skeleton_frames config
frame = Frame(root, height=3, bg='white')
frame.pack(fill=X, side='top')

emptyframe = Frame(root, height=300, bg='white')
emptyframe.pack(fill=X, side='top')

listframe1 = Label(emptyframe, width=1000, height=500, bg='silver', image=photo)
listframe1.pack(fill=Y, side='right')

listframe = Label(emptyframe, width=20, height=50, bg='grey')
listframe.pack(fill=Y, side='left')

controlframe = Frame(root, height=300, bg='silver')
controlframe.pack(fill=X, side='top')


#main_frames config
playlist_text_frame = Label(listframe, text='Current_Playlist', bg='grey')
playlist_text_frame.pack(side='top', padx=10, pady=10)

list = Listbox(listframe, height=30, width=70, bg='grey')
list.pack(fill=Y, side='bottom')


nowplaying_frame = Label(controlframe, text='Now_Playing',
                         relief='raised', bg='silver', width=40)
nowplaying_frame.grid(row=1, column=0, padx=10, pady=10)


music_lenght_label = Label(controlframe, text='00-:-00', bg='silver')
music_lenght_label.grid(row=1, column=2, padx=0, pady=10)

p = ttk.Progressbar(controlframe, orient=HORIZONTAL, length=300, mode='determinate')
p.grid(row=1, column=3, padx=5, pady=5)

music_current_time_label = Label(controlframe, text='00-:-00', bg='silver')
music_current_time_label.grid(row=1, column=4, padx=0, pady=10)

spaceframe = Frame(controlframe, height=20, width=40, bg='silver')
spaceframe.grid(row=1, column=7, padx=10, pady=10)

buttons_frame = Frame(controlframe, width=400, height=30, bg='silver')
buttons_frame.grid(row=1, column=9, padx=20, pady=10)

stop_button = ttk.Button(buttons_frame, text='stop', width=50, command= main.stop_file, image=stop_photo)
stop_button.grid(row=1, column=0, padx=10, pady=10)


play_button =  ttk.Button(buttons_frame, text='play',width=40, command=main.play_file, image=play_photo)
play_button.grid(row=1, column=2, padx=10, pady=10)

pause_button =  ttk.Button(buttons_frame, text='pause',width=10, command=main.pausefile, image=pause_photo)
pause_button.grid(row=1, column=3, padx=10, pady=10)

spaceframe = Frame(controlframe, height=20, width=70, bg='silver')
spaceframe.grid(row=1, column=10, padx=10, pady=10)

volume_scale = Scale(controlframe, bg='grey',
                     relief='sunken', orient='horizontal', from_=0, to_=100,
                     command = main.set_volume)
volume_scale.set(40)
volume_scale.grid(row=1, column=12, padx=10, pady=10)

mainloop()



