# initializing the modules 
import os
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askdirectory
from pygame import mixer
from tkinter import messagebox as mx


mixer.init()
# module initialization end

win = Tk()
win.title('RAP')
win.configure(bg='#bceaf7')
win.wm_iconbitmap("icon.ico")
win.geometry('520x600')
win.maxsize(520, 600)
win.minsize(520, 600)

# first label 
def action():
    mx.showinfo(title='About Us', message='Name : Raut Audio Player\nVersion : 2.0\nCreator : Ranjit Raut')

mainmenu = Menu(win)
sub_file = Menu(mainmenu, tearoff=False)
sub_file.add_command(label="Exit", command=win.destroy)
mainmenu.add_cascade(menu=sub_file, label="File")

submenu = Menu(mainmenu, tearoff=False)
submenu.add_command(label='About Us', command=action)
mainmenu.add_cascade(menu=submenu, label="About")


# ********************************************************Next drop down is here**********************************
# file_menu = Menu(win)



win.config(menu=mainmenu)







label00 = Label(win, text='Raut Audio Player', bg='#bceaf7', cursor='target', fg='red')
label00.pack()

# png images

img1 = PhotoImage(file='images/play.png')
img2 = PhotoImage(file='images/pause.png')
img3 = PhotoImage(file='images/next.png')
img4 = PhotoImage(file='images/previous.png')
img = PhotoImage(file='images/download.png')


photo = PhotoImage(file='images/real.png')
# label 2
label_0 = Label(win, image=photo, bg='#bceaf7', cursor='heart')
label_0.pack()

# declaring the list of songs 
listofsongs =[]
index = 0

var = StringVar()
label1 = Label(win, textvariable=var, foreground='blue', bg='#bceaf7')
label1.pack(side=TOP, fill=X)

# declaring function 
def main_func_directory():
    global index
    directory = askdirectory()
    os.chdir(directory)
    # directory = os.chdir(r'D:\RAP\file')
    for files in os.listdir(directory):
        if files.endswith('.mp3'):
            listofsongs.append(files)
    mixer.music.load(listofsongs[0]) 
    var.set(listofsongs[index])
    mixer.music.play()   

main_func_directory()
frame = LabelFrame(win)
frame.pack(fill=BOTH)

listbox = Listbox(frame, bg='#bceaf7')
listbox.pack(side=LEFT, fill=BOTH, expand=True)

scrollbar = Scrollbar(frame, bg='#bceaf7')
scrollbar.pack(side=RIGHT, fill=BOTH)
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

for item in listofsongs:
    listbox.insert(0, item)

def playmusic():
    global index
    mixer.music.load(listofsongs[index])
    mixer.music.play()
    var.set(listofsongs[index])
    

def nextmusic():
    global index
    index +=1
    mixer.music.load(listofsongs[index])
    mixer.music.play()
    var.set(listofsongs[index])
    

def prevmusic():
    global index
    index -=1
    mixer.music.load(listofsongs[index])
    mixer.music.play()
    var.set(listofsongs[index])


def stopmusic():
    mixer.music.stop()
    var.set('')

# binding effects
def beforehover1(event):
    bottom.config(text="Press to Play", bg='#bceaf7')

def afterhover1(event):
    
    bottom.config(text="Raut Audio Player Version-2.0")

def beforehover2(event):
    bottom.config(text="Press to Stop", bg='#bceaf7')

def afterhover2(event):
    bottom.config(text="Raut Audio Player Version-2.0")

def beforehover3(event):
    bottom.config(text="Press to Play Next", bg='#bceaf7')

def afterhover3(event):
    bottom.config(text="Raut Audio Player Version-2.0")

def beforehover4(event):
    bottom.config(text="Press to Play Previous ", bg='#bceaf7')

def afterhover4(event):
    bottom.config(text="Raut Audio Player Version-2.0")

# def beforehover(event):
#     bottom.config(text="Press to Download Your mp3 ", bg='#bceaf7')

# def afterhover(event):
#     bottom.config(text="Raut Audio Player Version-2.0")



# listofsongs.reverse()

# frame 
frame_1 = Frame(win)

# loadmusic = ttk.Button(frame_1, command=main_func_directory, image=img, cursor='heart')
# loadmusic.pack(side=LEFT, padx=2, pady=3)


prevmusic = ttk.Button(frame_1, command=prevmusic, image=img4, cursor='heart')
prevmusic.pack(side=LEFT, padx=2, pady=3)

playmusic = ttk.Button(frame_1, command=playmusic, image=img1, cursor='heart')
playmusic.pack(side=LEFT, padx=2, pady=3)

stopmusic = ttk.Button(frame_1, command=stopmusic, image=img2, cursor='heart')
stopmusic.pack(side=LEFT, padx=2, pady=3)

nextmusic = ttk.Button(frame_1, command=nextmusic, image=img3, cursor='heart')
nextmusic.pack(side=LEFT, padx=2, pady=3)

frame_1.pack(side=BOTTOM)

# function binding effects
playmusic.bind('<Enter>', beforehover1)
playmusic.bind('<Leave>', afterhover1)

stopmusic.bind('<Enter>', beforehover2)
stopmusic.bind('<Leave>', afterhover2)

nextmusic.bind('<Enter>', beforehover3)
nextmusic.bind('<Leave>', afterhover3)

prevmusic.bind('<Enter>', beforehover4)
prevmusic.bind('<Leave>', afterhover4)

# loadmusic.bind('<Enter>', beforehover)
# loadmusic.bind('<Leave>', afterhover)

# last label of the program
bottom = Label(win, text="Raut Audio Player Version-2.0", bd=1, bg='#bceaf7')
bottom.pack(side=BOTTOM, fill=X)

# end of the program
win.mainloop()
