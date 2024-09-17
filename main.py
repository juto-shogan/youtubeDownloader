import tkinter 
from tkinter import *
from tkinter import messagebox
from pytubefix import YouTube


class vidSystem:
    def __init__(self, url, path):
        self.url = url
        self.path = path
        self.yt = YouTube(url)
    
    def vidname(self):
        return self.yt.title
    
    def vidDownload(self):
        try:
            global path  # Assuming path is a global variable set in download_video
            stream = self.yt.streams.get_highest_resolution()
            stream.download().filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(path)
            messagebox.showinfo("Download Complete!", f"The video '{self.vidname()}' has been downloaded to {path}!")
        
        except Exception as e:
            messagebox.showerror("Download Error", f"An error occurred during download: {e}")

    

def download_video():
    # Get URL and download path from entries
    url = url_entry.get()
    path = path_entry.get()
    if not url:
        messagebox.showwarning("Invalid URL", "Please enter a valid YouTube video URL.")
        return
    
    if not path:
        messagebox.showinfo("Download Cancelled", "No download location chosen.")
        return
        
    downloader = vidSystem(url, path)
    downloader.vidDownload()    


root = Tk()
root.geometry("500x200")
root.resizable(width=False, height=False)
root.configure(bg="#f0f0f0")
root.title('MY DOWNLOADER')



ytDownloader_text = Label(root, text= "DOWNLOAD BEST QUALITY NOW" )
ytDownloader_text.grid(row=1, column=4)


url_entry = Entry(root, width=35, borderwidth=5)
url_entry.grid(row=2, column=4)
url_text = Label(root, text= "LINK:" )
url_text.grid(row=2, column=1)


path_entry = Entry(root, width=35, borderwidth=5)
path_entry.grid(row=3, column=4)
path_text = Label(root, text= "PATH:" )
path_text.grid(row=3, column=1)



download_b = Button(root, text="DOWNLOAD", padx=80, pady=20, bg= 'blue', command=download_video)
download_b.grid(row=4, column=4)

button_quit = Button(root, text="EXIT PROGRAM", command=root.quit)
button_quit.grid(row=5, column=5)



root.mainloop()
