# import system functions
import signal
import requests
import urllib.request
import os
import time
import re
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter.simpledialog import askstring
from tkinter.messagebox import showinfo
from subprocess import run
import subprocess
# load images in Tkinter python
from PIL import ImageTk, Image
# web
import webbrowser
# sounds
# from pygame import mixer

# Designed and developed by @hackt1vator

# cd the folder
script_path = os.path.dirname(os.path.abspath(__file__))

os.chdir(script_path)


# frame settings
root = tk.Tk()
frame = tk.Frame(root, width="500", height="250")
frame.pack(fill=BOTH,expand=True)
#tk.Entry(root).pack(fill='x')






def show_popup():
    popup = tk.Toplevel()
    popup.geometry("300x400")  # set the width and height of the window
    popup.title("palera1n")

    # center the window on the screen
    window_width = popup.winfo_reqwidth()
    window_height = popup.winfo_reqheight()
    position_right = int(popup.winfo_screenwidth() / 2 - window_width / 2)
    position_down = int(popup.winfo_screenheight() / 2 - window_height / 2)
    popup.geometry("+{}+{}".format(position_right, position_down))

    # create larger buttons
    button1 = tk.Button(popup, text="build fake fs", command=build_fakefs, width=20, height=5)
    button1.pack(pady=10)

    button2 = tk.Button(popup, text="boot fake fs", command=boot_fakefs, width=20, height=5)
    button1.pack(pady=10)
    button2.pack()
    
def show_popup2():
    popup = tk.Toplevel()
    popup.geometry("300x600")  # set the width and height of the window
    popup.title("bypass")

    # center the window on the screen
    window_width = popup.winfo_reqwidth()
    window_height = popup.winfo_reqheight()
    position_right = int(popup.winfo_screenwidth() / 2 - window_width / 2)
    position_down = int(popup.winfo_screenheight() / 2 - window_height / 2)
    popup.geometry("+{}+{}".format(position_right, position_down))

    # create larger buttons
    button1 = tk.Button(popup, text="save activation files", command=save, width=20, height=5)
    button1.pack(pady=10)

    button2 = tk.Button(popup, text="restore activation files", command=restore, width=20, height=5)
    button1.pack(pady=10)
    button2.pack()
    
    button2 = tk.Button(popup, text="delete activation files", command=delete, width=20, height=5)
    button1.pack(pady=10)
    button2.pack()

def build_fakefs():
    messagebox.showinfo("", "Please put the device first in recovery mode and then into dfu mode after the device is in dfu click ok")
 
    os.system("sudo ./palera1n-linux-x86_64 -cf")
    messagebox.showinfo("", "After the device boots you can boot the fake fs")
    
def boot_fakefs():
    messagebox.showinfo("", "Please put the device first in recovery mode and then into dfu mode after the device is in dfu click ok")
 
    os.system("sudo ./palera1n-linux-x86_64 -f")
    messagebox.showinfo("", "Now start the bypass")

def startcheckra1n():


    messagebox.showinfo("", "Please put the device first in recovery mode and then into dfu mode after the device is in dfu click ok")
    os.system("./checkra1n -c -V -E")




    

def exitRecMode():
    print("Kicking device out recovery mode...")
    os.system("./device/irecovery -n")

def quitProgram():
    print("Exiting...")
    os.system("exit")
    
def opentwitter():
    webbrowser.open('https://www.twitter.com/hackt1vator', new=2)
    
    


    


    
def delete():

    messagebox.showinfo("?","Do you really want to delete all saved activation files?")
    os.system("bash ./delete.sh")
    print("activation files deleted\n")
    showinfo('!', 'done!')
        




    

def save():


    showinfo("", "We will now save the activation files. Be sure to jailbreak your device first")
    print("Starting save")
        

    os.system("bash ./save.sh")
    time.sleep(5)

    folder_path = "./files"
    file_name = "activation_record.plist"
    file_path = os.path.join(folder_path, file_name)

    if os.path.exists(file_path):
        print("activation files saved\n")
        showinfo('save Success!', 'activation files saved!')
    else:
        print("activation files not saved\n")
        showinfo('save failed!', 'Save faild, try jailbreaking again!')




    
def restore():


            
        showinfo("", "We will now bypass your device. Be sure to jailbreak your device first")
        print("Starting bypass...")
        os.system("bash ./restore.sh")

        print("Device is bypassed\n")
        showinfo('bypass Success!', 'Device is now bypassed!')
        

    


root.title('Twitter: @hackt1vator')
frame.pack()



#BIG title on program
mainText = Label(root, text="iRevive",font=('Helveticabold', 24))
mainText.place(x=310, y=400)

img2 = Image.open("iRevive.jpg")
NewIMGSize2 = img2.resize((1000,1000), Image.ANTIALIAS)
new_image2 = ImageTk.PhotoImage(NewIMGSize2)
label = Label(frame, image = new_image2)
label.place(x=0, y=0)

#label
my_label2 = Label(frame,
                 text = "passcode Bypass")
my_label2.place(x=300, y=500)

#label
my_label3 = Label(frame,
                 text = "ver 1.1")
my_label3.place(x=10, y=700)



cButton1 = tk.Button(frame,
                   text="bypass ios 12-16.5",
                   command=show_popup2,
                   state="normal")
cButton1.place(x=270, y=600)
cButton6 = tk.Button(frame,
                 text="exit recovery",
                 command=exitRecMode,
                 state="normal")
cButton6.place(x=780, y=10)
cButton7 = tk.Button(frame,
                   text="start checkra1n",
                   command=startcheckra1n,
                   state="normal")
cButton7.place(x=700, y=400)
cButton9 = tk.Button(frame,
                   text="start palera1n",
                   command=show_popup,
                   state="normal")
cButton9.place(x=50, y=400)


cbeginExploit2 = tk.Button(frame,
                   text="Twitter!",
                   command=opentwitter,
                   state="normal")
cbeginExploit2.place(x=850, y=700)

root.geometry("1000x800")

root.resizable(False, False)

root.eval('tk::PlaceWindow . center')


root.mainloop()

