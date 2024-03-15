import time
from tkinter import *
from tkinter import filedialog
from pygame import mixer
import os
from PIL import Image, ImageTk

def AddMusic():
    path=filedialog.askdirectory()
    if path:
        os.chdir(path)
        songs=os.listdir(path)
        for song in songs:
            if song.endswith(".mp3"):
                Playlist.insert(END, song)

def PlayMusic():
    Music_Name= Playlist.get(ACTIVE)
    print(Music_Name)
    mixer.music.load(Playlist.get(ACTIVE))
    mixer.music.play()


root=Tk()
root.title("Vlayer")
root.geometry("485x700+290+10")
root.configure(background='#333333')
root.resizable(False,False)
mixer.init()

def load_gif_frames(file_path):
    gif = Image.open(file_path)
    frames = []
    try:
        while True:
            frames.append(ImageTk.PhotoImage(gif.copy()))
            gif.seek(len(frames)) # Move to next frame
    except EOFError:
        pass
    return frames

frames = load_gif_frames("a1.gif") # Load GIF frames
frame_count = len(frames)
current_frame = 0

def update():
    global current_frame
    frame = frames[current_frame]
    current_frame = (current_frame + 1) % frame_count
    label.configure(image=frame)
    root.after(40, update)

label = Label(root)
label.place(x=0, y=0)
update()

image_icon= PhotoImage(file="Logo.png")
root.iconphoto(False,image_icon)

Menu=PhotoImage(file="menu.png")
Label(root, image=Menu).place(x=0,y=580,width=485,height=100)

Frame_Music=Frame(root, bd=2, relief=RIDGE)
Frame_Music.place(x=0,y=585,width=485,height=100)

lower_frame = Frame(root,bg="#ffffff",width=485,height=180)
lower_frame.place(x=0,y=400)

ButtonPlay=PhotoImage(file="play1.png")
Button(root,image=ButtonPlay,bg="#FFFFFF",bd=0,height=60,width=60,command=PlayMusic).place(x=215,y=487)

ButtonStop=PhotoImage(file="stop1.png")
Button(root,image=ButtonStop,bg="#FFFFFF",bd=0,height=60,width=60,command=mixer.music.stop).place(x=130,y=487)

ButtonPause=PhotoImage(file="pause1.png")
Button(root,image=ButtonPause,bg="#FFFFFF",bd=0,height=60,width=60,command=mixer.music.pause).place(x=300,y=487)

Volume=PhotoImage(file="volume.png")
panel=Label(root,image=Volume).place(x=20,y=487)

Button(root,text="Browse", width=59, height=1,font=("calibri",12,"italic"),fg="Black",bg="#FFFFFF",command=AddMusic).place(x=0,y=550)

SCROLL=Scrollbar(Frame_Music)
Playlist=Listbox(Frame_Music,width=100,font=("Times new roman",10),bg="#333333",fg="grey",selectbackground="lightblue",cursor="hand2",bd=0,yscrollcommand=SCROLL.set)
SCROLL.config(command=Playlist.yview)
SCROLL.pack(side=RIGHT,fill=Y)
Playlist.pack(side=RIGHT,fill=BOTH)

root.mainloop()
