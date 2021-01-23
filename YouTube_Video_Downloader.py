# Import Libraries

from tkinter import *
from pytube import YouTube


# Initializing Window

root = Tk()
root.geometry('500x300')
root.resizable(0,0)
root.title("YouTube Video Downloader")


# Enter Video URL

Label(root,text = 'Youtube Video Downloader', font = 'Arabic_Transparent 20 bold' , bg = 'white smoke').pack()


# Text Variable

link = StringVar()


# Heading

Label(root, text = 'Enter Video URL here:', font = 'Arabic_Transparent 15 bold').place(x = 150 , y = 60)
link_enter = Entry(root, width = 70, textvariable = link).place(x = 32, y = 90, height = 30)


# Function Definition

def Downloader():
     
    url = YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    Label(root, text = 'Download', font = 'Arabic_Transparent 15').place(x = 180 , y = 210)

def Exit():
    root.destroy()


# Button

Button(root, text = 'Download', font = 'Arabic_Transparent 15 bold' , bg = 'chartreuse2', padx = 2, command = Downloader).place(x = 230 , y = 150)
Button(root,text = '❌', font = 'Arabic_Transparent 15 bold' , command = Exit, bg = 'OrangeRed').place(x=170 , y=150)


root.mainloop()
