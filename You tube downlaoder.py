from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube
folder_name= ""
def openLocation():
    global folder_name
    folder_name= filedialog.askdirectory()
    if (len(folder_name)>1):
        locerror.config(text=folder_name,fg="green")
    else:
        locerror.config(text="Please Choose Folder!", fg="red")
def videodownlaoder():
    choice = ytdchoices.get()
    url = ytdEntry.get()
    if(len(url)>1):
        ytdError.config(text="")
        yt= YouTube(url)

        if choice == choices[0]:
            select = yt.streams.filter(progressive=True).first()
        elif(choice == choices[1]):
            select = yt.streams.filter(progressive=True, file_extension='mp4').last()
        elif(choice == choices[2]):
            select = yt.streams.filter(audio_only=True).first()
        else:
            ytdError.config(text="Paste link again", fg="red")

        select.download(folder_name)
        ytdError.config(text="Download Completed")


root = Tk()
root.title("You Tube Downloader")
root.geometry("400x550")
root.columnconfigure(0, weight=1)
ytdLabel = Label(root, text="Enter the URL of the video ", font=("Bonbon", 15))
ytdLabel.grid()
ytdEntryVar = StringVar()
ytdEntry = Entry(root, width=50, textvariable=ytdEntryVar)
ytdEntry.grid()
ytdError = Label(root, text="Error Msg", fg="Red", font=("Bonbon", 10))
ytdError.grid()
saveLabel = Label(root, text="Save the Video", font=("Bonbon", "15", "bold"))
saveLabel.grid()
saveEnt = Button(root, width=10, bg="Red", fg="White", text="Choose Path", command=openLocation)
saveEnt.grid()
locerror = Label(root, text="Error in Path", fg="red", font=("Bonbon", 15))
locerror.grid()
ytdqlty = Label(root, text="Video Quality", font=("Bonbon", 15))
ytdqlty.grid()
choices = ["720p", "144p", "Only Audio"]
ytdchoices = ttk.Combobox(root, values=choices)
ytdchoices.grid()
downloadbtn= Button(root,text="Download",width=10, bg="red",fg="white", command=videodownlaoder)
downloadbtn.grid()
developerlabel = Label(root, text="Shubham Project", font=("Bonbon",15))
developerlabel.grid()
root.mainloop()
