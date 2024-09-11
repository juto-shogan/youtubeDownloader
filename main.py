import tkinter
from tkinter import *
from pytube import YouTube


class vidSystem:
    def __init__(self, url):
        self.url = url
        self.yt = YouTube(url)
    
    def vidname(self):
        return self.yt.title
    
    def vidDownload(self):
        try:
            
            stream = self.yt.streams.get_highest_resolution()
            
            stream.download().filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()
        
        except Exception as e:
            print(f"error occured: {e}")
        

    

def download_video():
    # Get URL and download path from entries
    url = url_entry.get()
    downloader = vidSystem(url)
    downloader.vidDownload()    


root = Tk()

root.geometry("500x200")
root.resizable(width=False, height=False)
root.title('MY DOWNLOADER')


ytDownloader_text = Label(root, text= "DOWNLOAD BEST QUALITY NOW" )
ytDownloader_text.grid(row=1, column=4)


url_entry = Entry(root, width=35, borderwidth=5)
url_entry.grid(row=2, column=4)
url_text = Label(root, text= "LINK:" )
url_text.grid(row=2, column=1)

download_b = Button(root, text="DOWNLOAD", padx=80, pady=20, command=download_video)
download_b.grid(row=3, column=4)

button_quit = Button(root, text="EXIT PROGRAM", command=root.quit)
button_quit.grid(row=5, column=5)



root.mainloop()





 
 
 



