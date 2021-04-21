# importing modules
import youtube_dl
import tkinter as tk
from tkinter import *
from tkinter import filedialog, messagebox


# Method to select destination downloaded Audio file path
def setDownloadPath():
    # Location to initial download directory
    downloadDirectory = filedialog.askdirectory(
        initialdir="/Users/ritur/Downloads")
    # Setting the directory
    downloadPath.set(downloadDirectory)


# Downloading function
def downloadvideo():
    # Get the videoLink from the link label
    youTube_Link = videoLink.get()
    # Fetching the downloading directory
    downloadFolder = downloadPath.get()
    # Setting the configuration for download file
    videofiledowloadoptions = {
        # Saving file name as title to destination
        'outtmpl': downloadFolder+"/%(title)s.%(ext)s",
    }
    # YoutubeDL() takes configuration as argument
    with youtube_dl.YoutubeDL(videofiledowloadoptions) as videodownload:
        # Link to the youtube video which have to be downloaded
        # YoutubeDL().download() takes link as argument
        videodownload.download([youTube_Link])
    # Displaying the message
    messagebox.showinfo("Done", "Video Downloaded Successfully")


# Downloading function
def downloadaudio():
    # Get the videoLink from the link label
    youTube_Link = videoLink.get()
    # Fetching the downloading directory
    downloadFolder = downloadPath.get()
    # Setting the configuration for download file
    audiofiledowloadoptions = {
        # Setting download audio to be in best format
        'format': 'bestaudio/best',
        # Saving file name as title to destination
        'outtmpl': downloadFolder+"/%(title)s.%(ext)s",
        # Conversion of video to audio
        'postprocessors': [{
            # Extraction of audio from video
            'key': 'FFmpegExtractAudio',
            # Fromat of saved audio file
            'preferredcodec': 'mp3',
            # Bitrate quality of the sound
            'preferredquality': '320'
        }],
    }
    # Downloading the audio file using the module method
    # YoutubeDL() takes configuration as argument
    with youtube_dl.YoutubeDL(audiofiledowloadoptions) as audiodownload:
        # Link to the youtube video which have to be downloaded
        # YoutubeDL().download() takes link as argument
        audiodownload.download([youTube_Link])
    # Displaying the message
    messagebox.showinfo("Done", "Downloaded in Audio Form")


# meta information
def information():
    # Get the videoLink from the link label
    youTube_Link = videoLink.get()
    ydl_opts = {}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        meta = ydl.extract_info(youTube_Link, download=False) 
    title=meta['title']
    uploaddate=meta['upload_date']
    uploader=meta['uploader']
    views=meta['view_count']
    likes=meta['like_count']
    dislike=meta['dislike_count']
    # creating a new window
    # creating tk class object
    root=Tk()
    # Setting the size of the window
    root.geometry("200x150")
    # Disabling resizing property
    # root.resizable(False, False)
    # Setting Background Color
    root.config(background="black")
    # Setting Title
    root.title("Video")
    # setting Label for the informations
    informationlabel=Label(root,text=f"Title: - {title} \nUpload Date: - {uploaddate}\nUploader: - {uploader}\nView: - {views}\nLikes: - {likes}\nDislike: - {dislike}", bg="green")
    # Poistioning of the label
    informationlabel.place(x=30,y=25)
    # Infinite loop to run the window
    root.mainloop()


# creating tk class object
root = tk.Tk()
# Setting the size of the window
root.geometry("700x100")
# Disabling resizing property
# root.resizable(False, False)
# Setting Title
root.title("Youtube Audio Downloader")
# Setting Background Color
root.config(background="black")
# Variables required
# Link variable
videoLink = StringVar()
# Download Path Variable
downloadPath = StringVar()
# Creating tkinter widgets
# YouTube Link Lable name
videolinkLabel = Label(root, text="YouTube Link :", bg="blue")
# Poistioning of the label
videolinkLabel.grid(row=1, column=0, pady=5, padx=5)
# Textarea for the youtube link
YouTubeURLText = Entry(root, width=75, textvariable=videoLink)
# Poistioning of the Entry
YouTubeURLText.grid(row=1, column=1, pady=5, padx=5, columnspan=2)
# Download folder Lable name
downloadpathLabel = Label(root, text="Donwload Location :", bg="blue")
# Poistioning of the label
downloadpathLabel.grid(row=2, column=0, pady=5, padx=5)
# Textarea to show the download path folder
downloadpathText = Entry(root, width=50, textvariable=downloadPath)
# Poistioning of the Entry
downloadpathText.grid(row=2, column=1, pady=5, padx=5)
# Button to run the setDownloadPath method
pathsettingButton = Button(root, text="SetPath", command=setDownloadPath, width=15, bg="green")
# Poistioning of the Button
pathsettingButton.grid(row=2, column=2, pady=5, padx=5)
# Button to show video information
informationButton = Button(root, text="Informations", command=information, width=15, bg="green")
# Poistioning of the Button
informationButton.grid(row=3, column=0, pady=5, padx=5)
# Button to run the download method
downloadaudioButton = Button(root, text="DOWNLOAD AUDIO", command=downloadaudio, width=30, bg="green")
# Poistioning of the Button
downloadaudioButton.grid(row=3, column=1, pady=5, padx=5)
# Button to run the download method
downloadvideoButton = Button(root, text="DOWNLOAD VIDEO", command=downloadvideo, width=30, bg="green")
# Poistioning of the Button
downloadvideoButton.grid(row=3, column=2, pady=5)
# Infinite loop to run the program
root.mainloop()