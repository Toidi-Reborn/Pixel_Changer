#from PIL import Image

from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import ast
import locale
import collections
import os
import PyPDF2
import cups
import subprocess


fileToChange = ""
newFileName = ""



class imageload:
    
    def __init__(self):
        tacp = "dfgfdsfg"


        '''
        img = Image.open('images/myLogoSprite.png')
        img = img.convert('RGBA')
        data = img.getdata()

        newData = []
        for item in data:
            if item[0] == 255 and item[1] == 255 and item[2] == 255:
                newData.append((255, 255, 255, 0))
            else:
                newData.append(item)

        img.putdata(newData)
        img.save('images/myLogoSpriteLightdsfsdfdfsfsd.png', 'PNG')
        
        '''
    

    def openFile(self):
        from PIL import Image
        fileToChange =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("png files","*.png"),("all files","*.*")))
        self.img = Image.open(fileToChange)
        fileToChangeBox.set(fileToChange)
        self.img = self.img.convert('RGBA')


    def saveLocation(self):
        newFileName =  filedialog.asksaveasfilename(initialdir = "/",title = "Select file",filetypes = (("png files","*.png"),("all files","*.*")))
        newFileNameBox.set(newFileName)

    def submit(self):
        load = fileToChangeBox.get()
        save = newFileNameBox.get()
        print(load, save)
        data = self.img.getdata()

        newData = []
        for item in data:
            if item[0] == 255 and item[1] == 255 and item[2] == 255:
                newData.append((255, 255, 255, 0))
            else:
                newData.append(item)

        self.img.putdata(newData)
        self.img.save(save, 'PNG')
        



class frameSetUp:
    
    def __init__(self):
        self.tFrame = Frame(gui, pady=10, height=10)
        self.mFrame = Frame(gui, pady=10, height=30)
        self.tFrame.grid(row=0, column=0, sticky='n')
        self.mFrame.grid(row=1, column=0, sticky='n')
        Grid.columnconfigure(gui, 0, weight=1)
        Grid.rowconfigure(gui, 0, weight=1)
        self.topFrame()
        self.midFrame()
        
    
    def topFrame(self):
        Label(self.tFrame, text="Image Changer").grid(row=0, column=0)

    def midFrame(self):
        Label(self.mFrame, text="File to Change: ").grid(row=0, column=0, sticky=N)
        Entry(self.mFrame, textvariable=fileToChangeBox, width=100).grid(row=0, column=1, padx=5)
        Button(self.mFrame, text="Select File", command= lambda x="sfdsf": ll.openFile()).grid(row=0, column=2, padx=5)
        
        Label(self.mFrame, text="New File: ").grid(row=1, column=0, sticky=N)
        Entry(self.mFrame, textvariable=newFileNameBox, width=100).grid(row=1, column=1, padx=5)
        #Label(self.mFrame, text="Overight Original File? ").grid(row=1, column=0, columnspan=3, sticky=N)
        Button(self.mFrame, text="Select Location", command= lambda x="dfsf": ll.saveLocation()).grid(row=1, column=2, padx=5)
        Button(self.mFrame, text="Process Image Change", command= lambda x="rgdgr": ll.submit()).grid(row=2, column=0, columnspan=3, padx=5)
        


    


gui = Tk()
gui.title("Pixel Changer")


fileToChangeBox = StringVar()
newFileNameBox = StringVar()

screenHP = gui.winfo_screenheight()
screenWP = gui.winfo_screenwidth()
screenH = screenHP - 1000
screenW = screenWP - 1000
#gui.geometry('%dx%d+%d+%d' % (500, 500, screenW / 2, 50))



ll = imageload()

frameSetUp()
gui.mainloop()