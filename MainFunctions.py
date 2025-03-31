from PIL import ImageTk
import tkinter
from tkinter import *
from tkinter.messagebox import *
from tkinter import ttk
from datetime import datetime
from datetime import timedelta
import ImageFunctions
from os.path import exists
import AcceleratorsFunctions as af
import tools
import DatabaseFunctions as db
import corrections as ct

def ShowTemplate(TemplatePath, CodClie, CodClieAbogado = False):

    TemplateName = (TemplatePath.split(sep="\\"))[-1]
    options = tools.FileRead('configuration/options.txt')

    root = tkinter.Tk()
    root.iconbitmap("assets/logo.ico")
    tools.CenterWindow("1000", "653", root)
    root.resizable(False,False)
    root.title("Seleccione finalizar para imprimir el carnet.")

    MenuBar = tkinter.Menu(root)

    MenuNew = tkinter.Menu(MenuBar, tearoff=False)
    MenuBar.add_cascade(menu=MenuNew, label="Nuevo")
    MenuNew.add_command(label="Nuevo", accelerator="Ctrl+N", command=lambda: NewCarnet(root))

    MenuSave = tkinter.Menu(MenuBar, tearoff=False)
    MenuBar.add_cascade(menu=MenuSave, label="Guardar")

    if TemplateName == 'AbgTemplate.png' or TemplateName == 'AbgTemplateExo.png':

        MenuSave.add_command(label="Guardar", accelerator="Ctrl+G", command= lambda: af.save(root, cedula.get(), TemplateName, apellidos.get(), nombres.get(), inpre.get(), ImagePath, FechaInscripcion= FechaInscripcion.get(), NumeroInscripcion= NumeroInscripcion.get(), folio= folio.get()))

    elif TemplateName == 'FamTemplate.png':

        MenuSave.add_command(label="Guardar", accelerator="Ctrl+G", command= lambda: af.save(root, cedula.get(), TemplateName, apellidos.get(), nombres.get(), inpre.get(), ImagePath, sangre= sangre.get(), telefono= telefono.get()))

    MenuSearch = tkinter.Menu(MenuBar, tearoff=False)
    MenuBar.add_cascade(menu=MenuSearch, label="Buscar")

    if TemplateName == 'AbgTemplate.png' or TemplateName == 'AbgTemplateExo.png':

        MenuSearch.add_command(label="Buscar", accelerator="Ctrl+B", command= lambda: af.search(cedula.get(), ApellidosEntry, NombresEntry, CedulaEntry, InpreEntry, MenuBar, profile, root, TemplateName, NumeroInscripcionEntry=  NumeroInscripcionEntry, FolioEntry= FolioEntry, messages= True))
    
    elif TemplateName == 'FamTemplate.png':

        MenuSearch.add_command(label="Buscar", accelerator="Ctrl+B", command= lambda: af.search(cedula.get(), ApellidosEntry, NombresEntry, CedulaEntry, InpreEntry, MenuBar, profile, root, TemplateName, SangreEntry= SangreEntry, TelefonoEntry= TelefonoEntry, messages= True))

    MenuClear = tkinter.Menu(MenuBar, tearoff=False)
    MenuBar.add_cascade(menu=MenuClear, label="Limpiar")

    if TemplateName == 'AbgTemplate.png' or TemplateName == 'AbgTemplateExo.png':

        MenuClear.add_command(label="Limpiar", accelerator="Ctrl+L", command= lambda: af.clear(ApellidosEntry, NombresEntry, CedulaEntry, InpreEntry, FechaInscripcionEntry, NumeroInscripcionEntry, FolioEntry, None, None, EmisionEntry, VencimientoEntry))

    elif TemplateName == 'FamTemplate.png':
        
        MenuClear.add_command(label="Limpiar", accelerator="Ctrl+L", command= lambda: af.clear(ApellidosEntry, NombresEntry, CedulaEntry, InpreEntry, None, None, None, SangreEntry, TelefonoEntry, EmisionEntry, VencimientoEntry))
    
    MenuChange = tkinter.Menu(MenuBar, tearoff=False)
    MenuBar.add_cascade(menu=MenuChange, label="Cambiar")
    MenuChange.add_command(label="Cambiar", accelerator="Ctrl+M", command=lambda: af.change(TemplateName, cedula.get(), root))

    if TemplateName == 'AbgTemplate.png' or TemplateName == 'AbgTemplateExo.png':

        MenuFill = tkinter.Menu(MenuBar, tearoff=False)
        MenuBar.add_cascade(menu=MenuFill, label="Rellenar")
        MenuFill.add_command(label="Rellenar", accelerator="Ctrl+R", command= lambda: af.fill(cedula.get(), ApellidosEntry, NombresEntry, CedulaEntry, InpreEntry, FechaInscripcionEntry, NumeroInscripcionEntry, FolioEntry, MenuBar, root, messages= True))

    if TemplateName == 'AbgTemplate.png' or TemplateName == 'AbgTemplateExo.png':

        MenuFinish = tkinter.Menu(MenuBar, tearoff=False)
        MenuBar.add_cascade(menu=MenuFinish, label="Finalizar")
        MenuFinish.add_command(label="Finalizar", accelerator="Ctrl+F", command= lambda: af.finish(TemplateName, cedula.get(), CodClieAbogado, root, emision.get(), vencimiento.get(), apellidos.get(), nombres.get(), inpre.get(), ImagePath, FechaInscripcion= FechaInscripcion.get(), NumeroInscripcion= NumeroInscripcion.get(), folio= folio.get()))

    elif TemplateName == 'FamTemplate.png':

        MenuFinish = tkinter.Menu(MenuBar, tearoff=False)
        MenuBar.add_cascade(menu=MenuFinish, label="Finalizar")
        MenuFinish.add_command(label="Finalizar", accelerator="Ctrl+F", command= lambda: af.finish(TemplateName, cedula.get(), CodClieAbogado, root, emision.get(), vencimiento.get(), apellidos.get(), nombres.get(), inpre.get(), ImagePath, sangre= sangre.get(), telefono= telefono.get()))

    template = ImageTk.PhotoImage(file=TemplatePath)
    TemplateLabel = tkinter.Label(root, image=template)
    TemplateLabel.place(x=0,y=0)

    apellidos = tkinter.StringVar()
    ApellidosEntry = tkinter.Entry(root, textvariable = apellidos, width = "29", font = ("Arial Bold", 19), fg = 'black', bg="white")
    ApellidosEntry.place(x = 270, y = 250)
    ct.StringLiveCT(apellidos, ApellidosEntry)

    nombres = tkinter.StringVar()
    NombresEntry = tkinter.Entry(root, textvariable = nombres, width = "29", font = ("Arial Bold", 19), fg = 'black', bg="white")
    NombresEntry.place(x = 265, y = 310)
    ct.StringLiveCT(nombres, NombresEntry)

    cedula = tkinter.StringVar()
    CedulaEntry = tkinter.Entry(root, textvariable = cedula, width = "9", font = ("Arial Bold", 19), fg = 'black', bg="white")
    CedulaEntry.place(x = 197, y = 370)
    CedulaEntry.insert(0, CodClie)
    ct.CedulaLiveCT(cedula, CedulaEntry, partial= True)

    inpre = tkinter.StringVar()
    InpreEntry = tkinter.Entry(root, textvariable = inpre, width = "9", font = ("Arial Bold", 19), fg = 'black', bg="white")
    InpreEntry.place(x = 235, y = 430)
    ct.NumberLiveCT(inpre, InpreEntry)

    CalendarImage = ImageTk.PhotoImage(file='assets/calendar.png')
            
    if TemplateName == 'AbgTemplate.png' or TemplateName == 'AbgTemplateExo.png':

        FechaInscripcion = tkinter.StringVar()
        FechaInscripcionEntry = tkinter.Entry(root, textvariable = FechaInscripcion, width = "9", font = ("Arial Bold", 19), fg = 'black', bg="white")
        FechaInscripcionEntry.place(x = 355, y = 490)
        FechaInscripcionEntry.config(state="disabled")

        FechaCalendarButton = tkinter.Button(root, command=lambda: tools.SetDate(root, FechaInscripcionEntry), image=CalendarImage)
        FechaCalendarButton.place(x = 503,y = 488)

        NumeroInscripcion = tkinter.StringVar()
        NumeroInscripcionEntry = tkinter.Entry(root, textvariable = NumeroInscripcion, width = "9", font = ("Arial Bold", 19), fg = 'black', bg="white")
        NumeroInscripcionEntry.place(x = 365, y = 550)
        ct.NumberLiveCT(NumeroInscripcion, NumeroInscripcionEntry)

        folio = tkinter.StringVar()
        FolioEntry = tkinter.Entry(root, textvariable = folio, width = "9", font = ("Arial Bold", 19), fg = 'black', bg="white")
        FolioEntry.place(x = 140, y = 595)
        ct.placeholder(folio, FolioEntry, "Folio")
        ct.NumberLiveCT(folio, FolioEntry)

    elif TemplateName == 'FamTemplate.png':

        sangre = tkinter.StringVar()
        SangreEntry = tkinter.Entry(root, textvariable = sangre, width = "5", font = ("Arial Bold", 19), fg = 'black', bg="white")
        SangreEntry.place(x = 335, y = 490)

        def SangreTrace(var, index, mode):
            Sangre = ((sangre.get()).upper())

            SangreEntry.delete(0, "end")

            if len(Sangre) > 4:
                Sangre = Sangre[:-1]

            if Sangre != "A+" and Sangre != "A-" and Sangre != "B+" and Sangre != "B-" and Sangre != "AB+" and Sangre != "AB-" and Sangre != "O+" and Sangre != "O-" and Sangre != "OHR+":
                SangreEntry.config(fg='red')
            else:
                SangreEntry.config(fg='black')

            SangreEntry.insert(0, Sangre)

        sangre.trace_add('write', SangreTrace)

        telefono = tkinter.StringVar()
        TelefonoEntry = tkinter.Entry(root, textvariable = telefono, width = "12", font = ("Arial Bold", 19), fg = 'black', bg="white")
        TelefonoEntry.place(x = 140, y = 595)
        ct.placeholder(telefono, TelefonoEntry, "N° de teléfono")

        def TelefonoTrace(var, index, mode):

            Telefono = telefono.get()

            TelefonoEntry.delete(0, "end")

            if len(Telefono) > 13:
                Telefono = Telefono[:-1]

            Telefono = ct.OnlyNumbers(Telefono)

            separated = ""
            for i in Telefono:
                separated = separated + i
                if len(separated) == 4 or len(separated) == 8:
                    separated = separated + "-"
            Telefono = separated

            if len(Telefono) == 13:
                TelefonoEntry.config(fg='black')
            else:
                TelefonoEntry.config(fg='red')

            TelefonoEntry.insert(0, Telefono)

        telefono.trace_add('write', TelefonoTrace)

    now = datetime.strptime((str(datetime.now()).split(sep=" "))[0], "%Y-%m-%d")

    if(TemplateName == 'AbgTemplateExo.png'):
        CalFix = True
        VencimientoDate = now.strftime('%d-%m-%Y')
    else:
        CalFix = False
        VencimientoDate = (now + timedelta(days=int(options[0]))).strftime('%d-%m-%Y')

    emision = tkinter.StringVar()
    EmisionEntry = tkinter.Entry(root, textvariable = emision, width = "9", font = ("Arial Bold", 19), fg = 'black', bg="white")
    EmisionEntry.place(x = 801, y = 150)
    ct.placeholder(emision, EmisionEntry, now.strftime('%d-%m-%Y'))
    EmisionEntry.config(state="disabled")

    vencimiento = tkinter.StringVar()
    VencimientoEntry = tkinter.Entry(root, textvariable = vencimiento, width = "9", font = ("Arial Bold", 19), fg = 'black', bg="white")
    if(TemplateName != 'AbgTemplateExo.png'):
        VencimientoEntry.place(x = 801, y = 180)
    ct.placeholder(vencimiento, VencimientoEntry, VencimientoDate)
    VencimientoEntry.config(state="disabled")

    CalendarButton = tkinter.Button(root, command=lambda: tools.SetDate(root, EmisionEntry, VencimientoEntry, False, CalFix), image=CalendarImage)
    CalendarButton.place(x = 948,y = 165)

    global count1
    count1 = 0

    def ProfileButton():

        global count1

        ImageFunctions.SelectImage(cedula.get(), root)

        count1 = 1

    ProfileImage = ImageTk.PhotoImage(file='assets/ProfileImageButton.png')
    profile = tkinter.Button(root, command = ProfileButton, borderwidth=0, image=ProfileImage)
    profile.place(x=691,y=266)

    global ImagePath
    ImagePath = ""

    def motion(event):

        global count1
        global ImagePath
        global ProfileImage

        if count1 == 1:

            Paths = ImageFunctions.SavePaths()

            if exists(Paths[2]) and Paths[3] == 1:

                ProfileImage = ImageTk.PhotoImage(file=Paths[2])
                profile.config(image=ProfileImage)
                ImagePath = Paths[2]
                count1 = 0

    global presioned
    presioned = []

    def key(event):

        global presioned

        presioned.append(event.keysym)

        if presioned[0] != "Control_L":

            presioned.clear()
        
        tools.shortcut(presioned, 2, "Control_L", lambda: NewCarnet(root), "n")

        if TemplateName == 'AbgTemplate.png' or TemplateName == 'AbgTemplateExo.png':
            tools.shortcut(presioned, 2, "Control_L", lambda: af.save(root, cedula.get(), TemplateName, apellidos.get(), nombres.get(), inpre.get(), ImagePath, FechaInscripcion= FechaInscripcion.get(), NumeroInscripcion = NumeroInscripcion.get(), folio= folio.get()), "g")
        elif TemplateName == 'FamTemplate.png':
            tools.shortcut(presioned, 2, "Control_L", lambda: af.save(root, cedula.get(), TemplateName, apellidos.get(), nombres.get(), inpre.get(), ImagePath, sangre=sangre.get(), telefono = telefono.get()), "g")
        
        if TemplateName == 'AbgTemplate.png' or TemplateName == 'AbgTemplateExo.png':
            tools.shortcut(presioned, 2, "Control_L", lambda: af.search(cedula.get(), ApellidosEntry, NombresEntry, CedulaEntry, InpreEntry, MenuBar, profile, root, TemplateName, FechaInscripcionEntry= FechaInscripcionEntry, NumeroInscripcionEntry=  NumeroInscripcionEntry, FolioEntry= FolioEntry, messages= True), "b")
        elif TemplateName == 'FamTemplate.png':
            tools.shortcut(presioned, 2, "Control_L", lambda: af.search(cedula.get(), ApellidosEntry, NombresEntry, CedulaEntry, InpreEntry, MenuBar, profile, root, TemplateName, SangreEntry= SangreEntry, TelefonoEntry= TelefonoEntry, messages= True), "b")
           
        if TemplateName == 'AbgTemplate.png' or TemplateName == 'AbgTemplateExo.png':
            tools.shortcut(presioned, 2, "Control_L", lambda: af.clear(ApellidosEntry, NombresEntry, CedulaEntry, InpreEntry, FechaInscripcionEntry, NumeroInscripcionEntry, FolioEntry, None, None, EmisionEntry, VencimientoEntry), "l")
        elif TemplateName == 'FamTemplate.png':
            tools.shortcut(presioned, 2, "Control_L", lambda: af.clear(ApellidosEntry, NombresEntry, CedulaEntry, InpreEntry, None, None, None, SangreEntry, TelefonoEntry, EmisionEntry, VencimientoEntry), "l")
        
        tools.shortcut(presioned, 2, "Control_L", lambda: af.change(TemplateName, cedula.get(), root), "m")
        
        if TemplateName == 'AbgTemplate.png' or TemplateName == 'AbgTemplateExo.png':
            tools.shortcut(presioned, 2, "Control_L", lambda: af.fill(cedula.get(), ApellidosEntry, NombresEntry, CedulaEntry, InpreEntry, FechaInscripcionEntry, NumeroInscripcionEntry, FolioEntry, MenuBar, root, messages= True), "r")
        
        if TemplateName == 'AbgTemplate.png' or TemplateName == 'AbgTemplateExo.png':
            tools.shortcut(presioned, 2, "Control_L", lambda: af.finish(TemplateName, cedula.get(), CodClieAbogado, root, emision.get(), vencimiento.get(), apellidos.get(), nombres.get(), inpre.get(), ImagePath, FechaInscripcion= FechaInscripcion.get(), NumeroInscripcion= NumeroInscripcion.get(), folio= folio.get()), "f")
        elif TemplateName == 'FamTemplate.png':
            tools.shortcut(presioned, 2, "Control_L", lambda: af.finish(TemplateName, cedula.get(), CodClieAbogado, root, emision.get(), vencimiento.get(), apellidos.get(), nombres.get(), inpre.get(), ImagePath, sangre= sangre.get(), telefono= telefono.get()), "f")

        if len(presioned) == 2:

            presioned.clear()
            
    root.bind("<Key>", key) 
    root.bind('<Motion>', motion)
    root.config(menu=MenuBar)

    if CodClieAbogado != False:

        if tools.IsConnected():

            connection = db.ConnectCloud()
            if connection != False:
                
                CodClieAbogado = ct.RemovePoints(CodClieAbogado)

                row = db.SelectCountLikeCodClie("SACLIE", connection, CodClieAbogado)

                if int(row[0]) == 1:

                    consult = db.SelectLikeCodClie("SACLIE", connection, CodClieAbogado)
                    registros2 = consult[0]
                    cursor = consult[1] 
                    if registros2 != False:

                        InpreEntry.insert(0, registros2[4])

                elif int(row[0]) > 1:

                    consult = db.SelectLikeCodClie("SACLIE", connection, CodClieAbogado)
                    registros2 = consult[0]
                    cursor = consult[1] 
                    if registros2 != False:
                    
                        ventana = tkinter.Toplevel()
                        ventana.iconbitmap("assets/logo.ico")
                        ventana.transient(root)
                        ventana.resizable(False,False)
                        tools.CenterWindow("500", "300", ventana)
                        ventana.title('Presiona "Enter" para confirmar tu selección')
                        ventana.focus()

                        style = ttk.Style()
                        style.configure("Treeview.Heading", font=("Arial Bold", 12))
                        style.configure("Treeview", font=("Arial Bold", 10))
                        
                        tv = ttk.Treeview(ventana, columns=("col1", "col2", "col3"), height= 30, selectmode="browse")
                        tv.column("#0", width=100)
                        tv.column("col1", width=80, anchor=CENTER)
                        tv.column("col2", width=300, anchor=CENTER)
                        tv.column("col3", width=0, anchor=CENTER)
                            
                        tv.heading("#0", text="Cédula")
                        tv.heading("col1", text="Inpre", anchor=CENTER)
                        tv.heading("col2", text="Nombre completo", anchor=CENTER)
                            
                        tv.pack(side='left') # supongo que sabes usar pack

                        ejscrollbar= ttk.Scrollbar(ventana,orient=VERTICAL,command=tv.yview)
                        ejscrollbar.pack(side='right',fill='y')
                        tv.configure(yscrollcommand=ejscrollbar.set) 

                        def get_selected_items():

                            selected_items = tv.selection()

                            if len(selected_items) == 0:
                                    
                                showwarning("Error de selección",
                                "Seleccione una persona primero", parent = root)
                            
                            else:
                                
                                for item in selected_items:

                                    values = (tv.item(item)["values"])
                    
                                InpreEntry.insert(0, values[0])
                                
                            ventana.destroy()  

                        while registros2:

                            tv.insert("", END, text= registros2[0], values=(registros2[4], registros2[1]))

                            registros2 = cursor.fetchone()  

                        def key(event):

                            if event.keysym == "Return":
                                    
                                yesorno = askyesno(title= "¿Desea confirmar la seleccion?", message= "¿Desea confirmar la seleccion?", parent = ventana)

                                if yesorno == True:
                                    
                                    get_selected_items()
                        
                        ventana.bind("<Key>", key) 

                elif int(row[0]) == 0:
                    
                    showwarning("Cédula no encontrada",
                        "El número de cédula introducido no se encuentra registrado en la base de datos del Colegio de Abogados del Estado Carabobo, intente de nuevo, si el problema persiste contacte con el soporte.", parent = root)
                    
                    NewCarnet(root)

    if TemplateName == 'AbgTemplate.png' or TemplateName == 'AbgTemplateExo.png':
        search = af.search(CodClie, ApellidosEntry, NombresEntry, CedulaEntry, InpreEntry, MenuBar, profile, root, TemplateName, FechaInscripcionEntry= FechaInscripcionEntry, NumeroInscripcionEntry=  NumeroInscripcionEntry, FolioEntry= FolioEntry)
    elif TemplateName == 'FamTemplate.png':
        search = af.search(CodClie, ApellidosEntry, NombresEntry, CedulaEntry, InpreEntry, MenuBar, profile, root, TemplateName, SangreEntry= SangreEntry, TelefonoEntry= TelefonoEntry)

    if search == False:
        if TemplateName == 'AbgTemplate.png' or TemplateName == 'AbgTemplateExo.png':
            af.fill(CodClie, ApellidosEntry, NombresEntry, CedulaEntry, InpreEntry, FechaInscripcionEntry, NumeroInscripcionEntry, FolioEntry, MenuBar, root)
    else:
        ImagePath = af.ReturnImagePath()

    root.focus()
    root.mainloop()

def NewCarnet(root = False):

    def CarnetAbogados(CodClie, exo = False):

        if ct.IsCedula(CodClie, root) == False:
            return
        
        if len(CodClie) == 0:
            showwarning("Error de usuario",
                    "Es necesario rellenar el campo CEDULA DEL ABOGADO, intente de nuevo, si el problema persiste contacte con el soporte.", parent = root)
            return

        if tools.IsConnected():

            connection = db.ConnectCloud()
            if connection == False:
                return
            
            CodClie = ct.RemovePoints(CodClie)
            
            result = db.SelectCountLikeCodClie("SACLIE", connection, CodClie)
            if int(result[0]) == 0:
                showwarning("Cédula no encontrada",
                    "El número de cédula introducido no se encuentra registrado en la base de datos del Colegio de Abogados del Estado Carabobo, intente de nuevo, si el problema persiste contacte con el soporte.", parent = root)

        root.destroy()

        CodClie = ct.PutPoints(CodClie)

        if exo == False:
            ShowTemplate(r"TemplateImages\AbgTemplate.png", CodClie)
        else:
            ShowTemplate(r"TemplateImages\AbgTemplateExo.png", CodClie)

    def CarnetFamiliar(CodClie):

        def InputFamiliar(CodClieAbogado, root):

            def NextButtonFunction(CodClieAbogado, CedulaFam, root, window):

                if len(CedulaFam) == 0:
                    showwarning("Error de usuario",
                            "Es necesario rellenar los campos CEDULA DEL ABOGADO y NUMERO DE CARNET, intente de nuevo, si el problema persiste contacte con el soporte.", parent = root)
                    return
                
                window.destroy()
                root.destroy()

                ShowTemplate(r"TemplateImages\FamTemplate.png", CedulaFam, CodClieAbogado)

            window = tkinter.Toplevel()
            window.resizable(False,False)
            window.title('Presiona "Enter" para confirmar tu selección')
            tools.CenterWindow("300", "213", window)
            window.transient(root)
            window.iconbitmap("assets/logo.ico")
            window.focus()

            CedulaFam = tkinter.StringVar()
            CedulaFamLabel = tkinter.Label(window, text = "CEDULA DEL FAMILIAR", font = ("Arial Bold", 19))
            CedulaFamLabel.place(x = 5, y = 0)
            CedulaFamEntry = tkinter.Entry(window, textvariable = CedulaFam, width = "9", font = ("Arial Bold", 19), fg = 'black', bg="white")
            CedulaFamEntry.place(x = 87, y = 50)
            ct.CedulaLiveCT(CedulaFam, CedulaFamEntry, partial= True)

            def key(event):

                if event.keysym == "Return":

                    if ct.GetCedulaStatus() == 1:
                        
                        yesorno = askyesno(title= "¿Desea confirmar la seleccion?", message= "¿Desea confirmar la seleccion?", parent = window)

                        if yesorno == True:

                            if tools.IsConnected():
                                row = db.SelectCountLikeCodClie("SACLIE", connection, CedulaFam.get())
                                if int(row[0]) != 0:
                                    showwarning("Error de cedula",
                                        "La cedula ingresada puede que pertenezca a un abogado, intente de nuevo, si el problema persiste contacte con el soporte.", parent= window)
                                
                            NextButtonFunction(CodClieAbogado, CedulaFam.get(), root, window)

                    else:
                        showwarning("Error de usuario",
                            "Hay un error en el campo de entrada CEDULA DEL FAMILIAR, intente de nuevo, si el problema persiste contacte con el soporte.", parent= window)
            
            window.bind("<Key>", key) 

        if ct.IsCedula(CodClie, root) == False:
            return
        
        if len(CodClie) == 0:
            showwarning("Error de usuario",
                    "Es necesario rellenar el campo CEDULA DEL ABOGADO, intente de nuevo, si el problema persiste contacte con el soporte.", parent = root)
            return

        if tools.IsConnected():

            connection = db.ConnectCloud()
            if connection == False:
                return
            
            CodClie = ct.RemovePoints(CodClie)

            row = db.SelectCountLikeCodClie("SACLIE", connection, CodClie)

            if int(row[0]) == 1:

                InputFamiliar(CodClie, root)

            elif int(row[0]) > 1:

                consult = db.SelectLikeCodClie("SACLIE", connection, CodClie)
                registros2 = consult[0]
                cursor = consult[1] 
                if registros2 == False:
                    return
                
                ventana = tkinter.Toplevel()
                ventana.transient(root)
                ventana.resizable(False,False)
                tools.CenterWindow("500", "313", ventana)
                ventana.title('Presiona "Enter" para confirmar tu selección')
                ventana.iconbitmap("assets/logo.ico")
                ventana.focus()

                style = ttk.Style()
                style.configure("Treeview.Heading", font=("Arial Bold", 12))
                style.configure("Treeview", font=("Arial Bold", 10))
                
                tv = ttk.Treeview(ventana, columns=("col1", "col2", "col3"), height= 30, selectmode="browse")
                tv.column("#0", width=100)
                tv.column("col1", width=80, anchor=CENTER)
                tv.column("col2", width=300, anchor=CENTER)
                tv.column("col3", width=0, anchor=CENTER)
                    
                tv.heading("#0", text="Cédula")
                tv.heading("col1", text="Inpre", anchor=CENTER)
                tv.heading("col2", text="Nombre completo", anchor=CENTER)
                    
                tv.pack(side='left') # supongo que sabes usar pack

                ejscrollbar= ttk.Scrollbar(ventana,orient=VERTICAL,command=tv.yview)
                ejscrollbar.pack(side='right',fill='y')
                tv.configure(yscrollcommand=ejscrollbar.set) 

                def get_selected_items():

                    selected_items = tv.selection()

                    if len(selected_items) == 0:
                            
                        showwarning("Error de selección",
                        "Seleccione una persona primero", parent = ventana)

                        return
                    
                    else:
                        
                        for item in selected_items:

                            txt = (tv.item(item)["text"])
            
                        InputFamiliar(txt, root)
                        
                    ventana.destroy()

                while registros2:

                    tv.insert("", END, text= registros2[0], values=(registros2[4], registros2[1]))

                    registros2 = cursor.fetchone()  

                def key(event):

                    if event.keysym == "Return":
                            
                        yesorno = askyesno(title= "¿Desea confirmar la seleccion?", message= "¿Desea confirmar la seleccion?", parent = ventana)

                        if yesorno == True:
                            
                            get_selected_items()
                
                ventana.bind("<Key>", key) 

            elif int(row[0]) == 0:
                
                showwarning("Cédula no encontrada",
                    "El número de cédula introducido no se encuentra registrado en la base de datos del Colegio de Abogados del Estado Carabobo, intente de nuevo, si el problema persiste contacte con el soporte.", parent = root)

                return
        
        else:

            InputFamiliar(CodClie, root)

    if root != False:

        root.destroy()

    root = tkinter.Tk()
    root.resizable(False,False)
    tools.CenterWindow("300", "150", root)
    root.title("Elaboración de carnets")
    root.iconbitmap("assets/logo.ico")
    root.focus()

    MenuBar = tkinter.Menu()

    MenuAbg = tkinter.Menu(MenuBar, tearoff=False)
    MenuBar.add_cascade(menu=MenuAbg, label="Abogado")
    MenuAbg.add_command(label="Abogado", accelerator="Ctrl+O", command= lambda: CarnetAbogados(cedula.get()))

    MenuFam = tkinter.Menu(MenuBar, tearoff=False)
    MenuBar.add_cascade(menu=MenuFam, label="Familiar")
    MenuFam.add_command(label="Familiar", accelerator="Ctrl+F", command= lambda: CarnetFamiliar(cedula.get()))

    MenuExo = tkinter.Menu(MenuBar, tearoff=False)
    MenuBar.add_cascade(menu=MenuExo, label="Exonerado")
    MenuExo.add_command(label="Exonerado", accelerator="Ctrl+E", command= lambda: CarnetAbogados(cedula.get(), True))

    MenuBar.entryconfig("Abogado", state='disabled')
    MenuBar.entryconfig("Familiar", state='disabled')
    MenuBar.entryconfig("Exonerado", state='disabled')
    
    root.config(menu=MenuBar)

    global cedula
    cedula = tkinter.StringVar()
    CedulaLabel = tkinter.Label(text = "CEDULA DEL ABOGADO", font = ("Arial Bold", 19))
    CedulaLabel.place(x = 0, y = 0)
    CedulaEntry = tkinter.Entry(root, textvariable = cedula, width = "9", font = ("Arial Bold", 19), fg = 'black', bg="white")
    CedulaEntry.place(x = 87, y = 50)
    ct.CedulaLiveCT(cedula, CedulaEntry, "NewCarnet", MenuBar, partial = True)

    global presioned
    presioned = []

    def key(event):

        global presioned

        presioned.append(event.keysym)

        if presioned[0] != "Control_L":

            presioned.clear()
        
        if MenuBar.entrycget("Abogado", 'state') != 'disabled':
            tools.shortcut(presioned, 2, "Control_L", lambda: CarnetAbogados(cedula.get()), "o")
        if MenuBar.entrycget("Familiar", 'state') != 'disabled':
            tools.shortcut(presioned, 2, "Control_L", lambda: CarnetFamiliar(cedula.get()), "f")
        if MenuBar.entrycget("Exonerado", 'state') != 'disabled':
            tools.shortcut(presioned, 2, "Control_L", lambda: CarnetAbogados(cedula.get(), True), "e")

        if len(presioned) == 2:

            presioned.clear()
            
    root.bind("<Key>", key) 

    root.mainloop()