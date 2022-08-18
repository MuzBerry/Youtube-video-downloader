from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
from moviepy import *
from moviepy.editor import VideoFileClip
from pytube import YouTube
import shutil


#functions
def select_path():
    #dowload file to users desired locaton
    path = filedialog.askdirectory()
    path_loc.config(text=path)

def download_vid():
    #get user path
    get_link = link_col.get()
    #get selected path
    user_path = path_loc.cget("text")
    screen.title('Downloading...')
    #Download Video
    mp4_video = YouTube(get_link).streams.get_highest_resolution().download()
    vid_clip = VideoFileClip(mp4_video)
    vid_clip.close()
    #move file to selected directory
    shutil.move(mp4_video, user_path)
    screen.title('Download Complete! Download Another File...')
    


#UI
#blank canvas
screen = Tk()
title = screen.title("Video Downloader")
canvas= Canvas(screen, width=350,height=400)
canvas.pack()

#logo
img = ImageTk.PhotoImage(Image.open("logo.jpg"))  
img = Image.open('logo.jpg')
#logo resize
img = img.resize((192, 120))
img = ImageTk.PhotoImage(img)
#logo placement
canvas.create_image(175,70,image=img)

#text and Columb
link_col=Entry(screen,width=35)
link_lab= Label(screen,text = "Video URL: ")
#Add text and columb to canvas
canvas.create_window(175,175, window=link_col)
canvas.create_window(175,150, window=link_lab)

#download button
down_btn = Button(screen, text ="Download video",command=download_vid)
#add download button on canvas
canvas.create_window(175,280,window=down_btn )

#path button and text
path_loc = Label(screen,text="Choose a downlaod location")
path_btn = Button(screen, text ="Path",command=select_path)
#add path button on canvas
canvas.create_window(175,240, window=path_loc)
canvas.create_window(175,210,window=path_btn, height= 25, width=50)


screen.mainloop()