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

# uses current directory to load the image file for the icon
root.iconphoto(False, tk.PhotoImage(file='irevive.png'))




def show_popup():
    popup = tk.Toplevel()
    popup.geometry("300x200")  # set the width and height of the window
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
    popup.geometry("300x300")  # set the width and height of the window
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
    messagebox.showinfo("", "Please put the device into dfu")
    # Display a message box with a yes/no option
    response = messagebox.askyesno("iphone?", "Do you have a A9 device?")

    # Check the user's response and execute the appropriate command
    if response == 1:  # Yes
        # Run the command in a subprocess
        process = subprocess.Popen(["./palera1n-macos-universal", "-cf"], preexec_fn=os.setsid)

        # Wait for 8 seconds or until the process completes
        for i in range(20):
            if process.poll() is not None:
                break
            time.sleep(1)

        # If the process is still running, terminate it
        if process.poll() is None:
            os.killpg(os.getpgid(process.pid), signal.SIGTERM)


        os.system("./palera1n-macos-universal -cf")
    if response == 0:  # No
        os.system("./palera1n-macos-universal -cf")
    messagebox.showinfo("", "After the device boots you can boot the fake fs")
    
def boot_fakefs():
    messagebox.showinfo("", "Please put the device into dfu")
    # Display a message box with a yes/no option
    response = messagebox.askyesno("iphone?", "Do you have a A9 device?")

    # Check the user's response and execute the appropriate command
    if response == 1:  # Yes
        # Run the command in a subprocess
        process = subprocess.Popen(["./palera1n-macos-universal", "-f"], preexec_fn=os.setsid)

        # Wait for 8 seconds or until the process completes
        for i in range(20):
            if process.poll() is not None:
                break
            time.sleep(1)

        # If the process is still running, terminate it
        if process.poll() is None:
            os.killpg(os.getpgid(process.pid), signal.SIGTERM)


        os.system("./palera1n-macos-universal -f")
    if response == 0:  # No
        os.system("./palera1n-macos-universal -f")
    messagebox.showinfo("", "Now start the bypass")





def startcheckra1n():



    os.system("open ./checkra1n.app")




def showDFUMessage():
    messagebox.showinfo("Step 1","Put your iDevice into DFU mode.\n\nClick Ok once its ready in DFU mode to proceed.")
    

def enterRecMode():

    os.system("./device/ideviceinfo > ./device/lastdevice.txt")
    time.sleep(2)

    f = open("./device/lastdevice.txt", "r")
    fileData = f.read()
    f.close()
    # Find the UDID
    start = 'UniqueDeviceID: '
    end = 'UseRaptorCerts:'
    s = str(fileData)

    foundData = s[s.find(start) + len(start):s.rfind(end)]
    UDID = str(foundData)
    LAST_CONNECTED_UDID = str(UDID)
    print("Kicking device into recovery mode...")
    os.system(f"./device/ideviceenterrecovery {LAST_CONNECTED_UDID}")

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

    global LAST_CONNECTED_UDID, LAST_CONNECTED_IOS_VER

    # Step 1: Detect connected device
    print("Searching for connected device...")
    os.system("idevicepair unpair")
    os.system("idevicepair pair")
    os.system("./device/ideviceinfo > ./device/lastdevice.txt")
    time.sleep(2)

    f = open("./device/lastdevice.txt", "r")
    fileData = f.read()
    f.close()

    if "ERROR:" in fileData:
        # No device was detected, so retry user!
        print("ERROR: No device found!")
        messagebox.showinfo("No device detected! 0x404","Try disconnecting and reconnecting your device.")
        return  # stop function execution here
    else:
        # We definitely have something connected...

        # Find the UDID
        start = 'UniqueDeviceID: '
        end = 'UseRaptorCerts:'
        s = str(fileData)

        foundData = s[s.find(start) + len(start):s.rfind(end)]
        UDID = str(foundData)
        LAST_CONNECTED_UDID = str(UDID)
        
        
        


        if len(UDID) > 38:
            # Stop automatic detection
            timerStatus = 0


                
        else:
            print("Couldn't find your device")
            messagebox.showinfo("","No device connected")
            return  # stop function execution here
        showinfo("", "We will now save the activation files. Be sure to jailbreak your device first")
        print("Starting save")

        os.system("bash ./save.sh")

        print("activation files saved\n")
        showinfo('save Success!', 'activation files saved!')
        

    
def restore():

    global LAST_CONNECTED_UDID, LAST_CONNECTED_IOS_VER

    # Step 1: Detect connected device
    print("Searching for connected device...")
    os.system("idevicepair unpair")
    os.system("idevicepair pair")
    os.system("./device/ideviceinfo > ./device/lastdevice.txt")
    time.sleep(2)

    f = open("./device/lastdevice.txt", "r")
    fileData = f.read()
    f.close()

    if "ERROR:" in fileData:
        # No device was detected, so retry user!
        print("ERROR: No device found!")
        messagebox.showinfo("No device detected! 0x404","Try disconnecting and reconnecting your device.")
        return  # stop function execution here
    else:
        # We definitely have something connected...

        # Find the UDID
        start = 'UniqueDeviceID: '
        end = 'UseRaptorCerts:'
        s = str(fileData)

        foundData = s[s.find(start) + len(start):s.rfind(end)]
        UDID = str(foundData)
        LAST_CONNECTED_UDID = str(UDID)
        
        
        


        if len(UDID) > 38:
            # Stop automatic detection
            timerStatus = 0


                
        else:
            print("Couldn't find your device")
            messagebox.showinfo("","No device connected")
            return  # stop function execution here
            
        showinfo("", "We will now bypass your device. Be sure to jailbreak your device first")
        print("Starting bypass...")
        os.system("bash ./restore.sh")

        print("Device is bypassed\n")
        showinfo('bypass Success!', 'Device is now bypassed!')
        

    


root.title('Twitter: @hackt1vator')
frame.pack()



#BIG title on program
mainText = Label(root, text="iRevive",font=('Helveticabold', 24))
mainText.place(x=310, y=170)

img2 = Image.open("iRevive.jpg")
NewIMGSize2 = img2.resize((1000,1000), Image.ANTIALIAS)
new_image2 = ImageTk.PhotoImage(NewIMGSize2)
label = Label(frame, image = new_image2)
label.place(x=0, y=0)

#label
my_label2 = Label(frame,
                 text = "passcode Bypass")
my_label2.place(x=300, y=230)

#label
my_label3 = Label(frame,
                 text = "ver 1.0")
my_label3.place(x=10, y=420)



cButton1 = tk.Button(frame,
                   text="bypass ios 12-16.5",
                   command=show_popup2,
                   state="normal")
cButton1.place(x=270, y=360)
cButton5 = tk.Button(frame,
                   text="enter recovery",
                   command=enterRecMode,
                   state="normal")
cButton5.place(x=10, y=10)
cButton6 = tk.Button(frame,
                 text="exit recovery",
                 command=exitRecMode,
                 state="normal")
cButton6.place(x=580, y=10)
cButton7 = tk.Button(frame,
                   text="start checkra1n",
                   command=startcheckra1n,
                   state="normal")
cButton7.place(x=530, y=200)
cButton9 = tk.Button(frame,
                   text="start palera1n",
                   command=show_popup,
                   state="normal")
cButton9.place(x=50, y=200)


cbeginExploit2 = tk.Button(frame,
                   text="Twitter!",
                   command=opentwitter,
                   state="normal")
cbeginExploit2.place(x=580, y=410)

root.geometry("700x450")

root.resizable(False, False)

root.eval('tk::PlaceWindow . center')


root.mainloop()

