from pytube import YouTube
import tkinter as tk
import sys

# Hi Darachu

def cli():
    for arg in sys.argv:
        print(arg)

def gui():
    root = tk.Tk()  
    root.title("PyTube Installer")
    root.geometry("300x200")

    link_box = tk.Entry(root)

    def download_video():
        yt_video = YouTube(link_box.get())
        yt_video.streams.filter(progressive=True, file_extension='mp4').first().download()

    submit_link = tk.Button(
                            root, 
                            text="Submit",
                            command=download_video
                            )

    link_box.pack()
    submit_link.pack()
    root.mainloop()

if len(sys.argv) == 1:
    gui()
else:
    cli()