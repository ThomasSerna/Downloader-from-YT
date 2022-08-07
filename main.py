# By xThoms

try:
    from tkinter import *
    from tkinter import messagebox as mb
    from pytube import YouTube
except:
    raise OSError('Error importing libraries.')

def audyt(link: str = None): #Function to download audio
    try:
        name = f'{YouTube(link).title}'
        if '.' in name:
            a = []
            for i in name.strip():
                if i == '.': pass
                else: a.append(i)                
            name = ''.join(a)
    except:
        mb.showwarning('¡Wrong link!', 'You put a wrong link, try a link "youtu.be" or "youtube.com"')
        raise
    try:
        YouTube(link).streams.get_audio_only().download(filename=f'{name}.mp3')      
    except:
        print('Download failed.')
        global error
        error = True

def vidst(link: str = None): #Funcion para descargar video
    try:
        name = f'{YouTube(link).title}'
        if '.' in name:
            a = []
            for i in name.strip():
                if i == '.': pass
                else: a.append(i)                
            name = ''.join(a)
    except:
        mb.showwarning('¡Wrong link!', 'You put a wrong link, try a link "youtu.be" or "youtube.com"')
        raise
    try:
        YouTube(link).streams.get_highest_resolution().download(filename=f'{name}.mp4')      
    except:
        print('Download failed.')
        global error
        error = True

def gv():
    error = False
    vidst(str(l.get()))
    if error == True: mb.showerror('Download error!', 'There was an error downloading the video.')
    else: mb.showinfo("Download successful!", "Video downloaded successfully")

def ga():
    error = False
    audyt(str(l.get()))
    if error == True: mb.showerror('Download error!', 'There was an error downloading the song.')
    else: mb.showinfo("Download successful!", "Song downloaded successfully")

rt = Tk() #El siguiente codigo hace parte del sistema grafico e interfaz

rt.title('xThoms')
rt.iconbitmap('icon.ico')
rt.state('zoomed')


l = StringVar()

tt = Label(rt, text="Video and audio downloader from Youtube")
tt.pack(anchor=CENTER)
tt.config(font=('pass',35))
image = PhotoImage(file='yt.png')
Label(rt, image=image).pack(side='right')

label = Label(rt, text="Link")
label.pack()
label.config(font=('pass',10))
Entry(rt, justify=CENTER, textvariable=l).pack()
Label(rt,text='\n\n\nBy xThoms\n\n\n\n').pack()
Button(rt,text='Download on video', command=gv,justify=CENTER).pack()
Label(rt,text='\n').pack()
Button(rt,text='Download in audio', command=ga, justify=CENTER).pack()

rt.mainloop()