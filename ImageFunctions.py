import tkinter as tk
from PIL import ImageTk, Image, ImageDraw, ImageFont
from tkinter import filedialog
from PIL import Image
from tkinter.messagebox import *
import win32api
import cv2
import os
import tools

def FinallyImage(ProfilePath, TemplateName, emision, vencimiento, apellidos, nombres, inpre, FechaInscripcion, NumeroInscripcion, folio, CodClie, sangre, telefono, NotVencimiento = False):

    ImagePaste(TemplateName, ProfilePath, CodClie, ((ProfilePath.split(sep="."))[-1]))

    TextPaste(("PrintedImages/" + CodClie + "." + ((ProfilePath.split(sep="."))[-1])), emision, vencimiento, apellidos, nombres, inpre, FechaInscripcion, NumeroInscripcion, folio, CodClie, sangre, telefono, ((ProfilePath.split(sep="."))[-1]), NotVencimiento)

    return ("PrintedImages/" + CodClie + "." + ((ProfilePath.split(sep="."))[-1]))

def ImagePaste(TemplateName, ProfilePath, CodClie, extension):
    img1 = Image.open("TemplateImages/" + TemplateName)
    img2 = Image.open(ProfilePath).convert("RGBA")
    img1.paste(img2, (691,266), mask = img2)
    img1.save("PrintedImages/" + CodClie + "." + extension)

def TextPaste(TemplatePath, emision, vencimiento, apellidos, nombres, inpre, FechaInscripcion, NumeroInscripcion, folio, CodClie, sangre, telefono, extension, NotVencimiento = False):

    base = Image.open(TemplatePath).convert('RGBA')
    txt = Image.new('RGBA', base.size, (255,255,255,0))
    fnt2 = ImageFont.truetype('arialbd.ttf', 25)
    d = ImageDraw.Draw(txt)

    d.text((801,150), emision, font=fnt2, fill=(0,0,0,255))

    if NotVencimiento == False:
        d.text((801,180), vencimiento, font=fnt2, fill=(0,0,0,255))

    d.text((270,250), apellidos, font=fnt2, fill=(0,0,0,255))

    d.text((265,310), nombres, font=fnt2, fill=(0,0,0,255))

    d.text((197,370), CodClie, font=fnt2, fill=(0,0,0,255))

    d.text((235,430), inpre, font=fnt2, fill=(0,0,0,255))

    if sangre == None:

        d.text((355,490), FechaInscripcion, font=fnt2, fill=(0,0,0,255))

    else:

        d.text((335,490), sangre, font=fnt2, fill=(0,0,0,255))

    if telefono == None:

        d.text((362,550), NumeroInscripcion, font=fnt2, fill=(0,0,0,255))

        d.text((140,595), folio, font=fnt2, fill=(0,0,0,255))

    else:

        d.text((140,595), telefono, font=fnt2, fill=(0,0,0,255))

    out = Image.alpha_composite(base, txt)

    out.save("PrintedImages/" + CodClie + "." + extension)

def PrintImage(ImagePath):
    try:
        win32api.ShellExecute(0, "print", ImagePath, None,  ".",  0)
    except:
        showerror("Error de impresión",
                "No se puede imprimir el carnet, intente de nuevo, si el problema persiste contacte con el soporte.")
        return

def CropImage(ImagePath, right, down, left, up, NewImagePath):

    img = Image.open(ImagePath)
    #Right, Down, Left, Up
    area = (right, down, left, up)
    cropped_img = img.crop(area)
    cropped_img.save(NewImagePath)

def resize(name, NewName, width):

    basewidth = width
    img = Image.open(name)
    wpercent = (basewidth/float(img.size[0]))
    hsize = int((float(img.size[1])*float(wpercent)))
    img = img.resize((basewidth,hsize), Image.Resampling.LANCZOS)
    img.save(NewName)

class App(tk.Frame):
    
    def __init__( self, parent, w, h, ImagePath):
        tk.Frame.__init__(self, parent)
        self._createVariables(parent)
        self._createCanvas(w,h)
        self._createCanvasBinding()
        self.door = ImageTk.PhotoImage(file=ImagePath)
        self.doorl = self.canvas.create_image((w / 2),(h / 2), image=self.door)

    def _createVariables(self, parent):
        self.parent = parent
        self.rectx0 = 0
        self.recty0 = 0
        self.rectx1 = 0
        self.recty1 = 0
        self.rectid = None

    def _createCanvas(self, w, h):
        self.canvas = tk.Canvas(self.parent, width = w, height = h)
        self.canvas.grid(row=0, column=0, sticky='nsew')

    def _createCanvasBinding(self):
        self.canvas.bind( "<Button-1>", self.startRect )
        self.canvas.bind( "<ButtonRelease-1>", self.stopRect )
        self.canvas.bind( "<B1-Motion>", self.movingRect )

    def startRect(self, event):
        #Translate mouse screen x0,y0 coordinates to canvas coordinates
        self.rectx0 = self.canvas.canvasx(event.x)
        self.recty0 = self.canvas.canvasy(event.y) 
        #Create rectangle
        self.canvas.delete(self.rectid)
        self.StartedX = self.rectx0
        self.StartedY = self.recty0

        self.rectid = self.canvas.create_rectangle(
            self.rectx0, self.recty0, self.rectx0, self.recty0, width=4)

    def movingRect(self, event):
        #Translate mouse screen x1,y1 coordinates to canvas coordinates
        self.rectx1 = self.canvas.canvasx(event.x)
        self.recty1 = self.canvas.canvasy(event.y)
        #Modify rectangle x1, y1 coordinates

        width = abs(self.rectx0 - self.rectx1)
        height = abs(self.recty0 - self.recty1)

        if height == 0:

            self.canvas.delete(self.rectid)

        else:

            if (width / height) >= 0.74 and (width / height) <= 0.75:

                self.canvas.itemconfig(self.rectid, outline='green')

            else:

                self.canvas.itemconfig(self.rectid, outline='black')

        self.canvas.coords(self.rectid, self.rectx0, self.recty0,
                    self.rectx1, self.recty1)
            

    def stopRect(self, event):
        #Translate mouse screen x1,y1 coordinates to canvas coordinates
        self.rectx1 = self.canvas.canvasx(event.x)
        self.recty1 = self.canvas.canvasy(event.y)

        width = abs(self.rectx0 - self.rectx1)
        height = abs(self.recty0 - self.recty1)

        if height == 0:

            self.canvas.delete(self.rectid)

        else:

            if (width / height) >= 0.74 and (width / height) <= 0.75:

                self.FinallyX = self.rectx1
                self.FinallyY = self.recty1
                #Modify rectangle x1, y1 coordinates
                self.canvas.coords(self.rectid, self.rectx0, self.recty0,
                            self.rectx1, self.recty1)

            else:

                h = width / 0.744

                if self.recty0 < self.recty1:

                    self.recty1 = h + self.recty0

                else:

                    self.recty1 = self.recty0 - h

                width = abs(self.rectx0 - self.rectx1)
                height = abs(self.recty0 - self.recty1)

                self.FinallyX = self.rectx1
                self.FinallyY = self.recty1
                #Modify rectangle x1, y1 coordinates
                self.canvas.coords(self.rectid, self.rectx0, self.recty0,
                            self.rectx1, self.recty1)
                
                self.canvas.itemconfig(self.rectid, outline='green')

    def SavePosition(self):

        try:

            return self.StartedX, self.StartedY, self.FinallyX, self.FinallyY
        
        except:

            pass

def SelectImage(CodClie, root):

    def Select(ImagePath, NewImagePath, CropImagePath, root):

        img = cv2.imread(ImagePath,0)
        height, width = img.shape

        if width > 500:

            resize(ImagePath, NewImagePath, 500)

            img = cv2.imread(NewImagePath,0)
            height, width = img.shape

            ImagePath = NewImagePath

        else:

            img = Image.open(ImagePath)

            mul = (500 / height)

            img = img.resize(((int(width * mul) + 1),(int(height * mul) + 1)), Image.Resampling.LANCZOS)
            img.save(NewImagePath)

            img = cv2.imread(NewImagePath,0)
            height, width = img.shape

            ImagePath = NewImagePath

        global position
        position = None

        def close():

            right = 0
            down = 0
            left = 0
            up = 0

            global position
            global flag

            try:

                position = (CropPosition.SavePosition())

                if position[0] > position[2]:

                    left = position[0]
                    right = position[2]

                else:

                    left = position[2]
                    right = position[0]

                if position[1] > position[3]:

                    up = position[1]
                    down = position[3]

                else:

                    up = position[3]
                    down = position[1]

                rectangle.destroy()

                CropImage(ImagePath, right, down, left, up, CropImagePath)

                os.remove(ImagePath)

                img = cv2.imread(CropImagePath,0)
                height, width = img.shape

                img = Image.open(CropImagePath)

                mul = 312 / height

                img = img.resize((int(width * mul),int(height * mul)), Image.Resampling.LANCZOS)
                img.save(CropImagePath)

                flag = 1


            except:

                rectangle.destroy()

                os.remove(ImagePath)

        rectangle = tk.Toplevel()
        rectangle.transient(root)
        rectangle.resizable(False,False)
        tools.CenterWindow(width + 4, height + 4, rectangle)
        rectangle.title('Cierra la ventana o presiona "ENTER" para seleccionar.')
        rectangle.iconbitmap("assets/logo.ico")
        rectangle.focus()

        CropPosition = App(rectangle, width, height, ImagePath)

        def key(event):

            if event.keysym == "Return":
                    
                yesorno = askyesno(title= "¿Desea confirmar la seleccion?", message= "¿Desea confirmar la seleccion?")

                if yesorno == True:
                    
                    close()
        
        rectangle.bind("<Key>", key) 

        rectangle.protocol("WM_DELETE_WINDOW", close)

    def UploadAction():

        ImagePath = filedialog.askopenfilename()

        return ImagePath
    
    if len(CodClie) < 9 and len(CodClie) > 10:
        showerror("Error en el número de cedula", "El número de cedula no tiene la cantidad de caracteres correcta, intente de nuevo, si el problema persiste contacte con el soporte.", parent = root)    
        return
    
    global flag     
    flag = 0
    
    global ImagePath
    ImagePath = UploadAction()

    global extension
    extension = "png"

    global NewImagePath
    NewImagePath = "ProfilePhotos/" + CodClie + "." + extension

    global CropImagePath
    CropImagePath = "ProfilePhotos/cropped/" + CodClie + "." + extension

    try:
        Select(ImagePath, NewImagePath, CropImagePath, root)
    except:
        if ImagePath != "":
            showerror("Error de apertura",
                    "No se puede abrir el archivo seleccionado, intente de nuevo, si el problema persiste contacte con el soporte.")
        return

def SavePaths():

    global ImagePath
    global NewImagePath
    global CropImagePath
    global flag
    global extension

    return ImagePath, NewImagePath, CropImagePath, flag, extension 