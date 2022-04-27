from pytube import YouTube
from moviepy.editor import *
from tkinter import *
from tkinter.filedialog import askdirectory


AvaliableVideoList = ["None"]
ListofList = {"None":"None"}

root = Tk()
root.title("Youtube downloader")
canvas = Canvas(root,width=400,height=450)
canvas.pack()

def Updating(var):
    global AvaliableVideoList
    global ListofList
    try:
        AvaliableVideoList = []
        ListofList = {}
        VideoLink = var.get()
        List = YouTube(VideoLink).streams
        for i in List:
            if (i.type == "video") and (i.is_progressive):
                ListofList[f"Resolution = {i.resolution},File = .{i.subtype},FPS = {i.fps}"] = (i.resolution,i.subtype,i.fps)
        AvaliableVideoList = ListofList.copy().keys()
        Avaliable = OptionMenu(root,var1,*AvaliableVideoList)
        canvas.create_window(200,400,window=Avaliable)
    except:
        pass


def downloading():
        PathGet = Path.get()
        VideoLink = var.get()
        SelectGet = ListofList[var1.get()]
        # print(VideoLink)
        # print(YouTube(VideoLink).streams)
        Mp4 = YouTube(VideoLink).streams.filter(file_extension=SelectGet[1],resolution=SelectGet[0],fps=SelectGet[2])
        try:
            Video = Mp4.first().download(output_path=PathGet)
            Video = VideoFileClip(Mp4)
            Video.close()
        except:
            pass

app_title = Label(root,text="Download video from youtube",font=("Arial",20,"bold"))
canvas.create_window(200,50,window=app_title)
URL = Label(root,text="Input link URL")
canvas.create_window(200,100,window=URL)


var = StringVar()
var.trace("w", lambda name, index,mode, var=var: Updating(var))

var1 = StringVar()
var1.set("None")

link = Entry(root,width=60,textvariable=var)
canvas.create_window(200,150,window=link)
downloadBtn = Button(text="Download",command=downloading)
canvas.create_window(200,200,window=downloadBtn)
Path_label = Label(root,text="Enter path")
canvas.create_window(200,250,window=Path_label)
Path = Entry(root,width=60)
canvas.create_window(200,300,window=Path)
Avaliable_label = Label(root,text="Select")
canvas.create_window(200,350,window=Avaliable_label)
Avaliable = OptionMenu(root,var1,*AvaliableVideoList)
canvas.create_window(200,400,window=Avaliable)

root.mainloop()
