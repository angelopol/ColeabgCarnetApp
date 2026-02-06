from tkinter import *
from tkinter import ttk
import tools
from tkinter.messagebox import *
from datetime import datetime
from PIL import ImageTk
import webbrowser
import MainFunctions as mf
import ImageFunctions as imf
import corrections as ct
import DatabaseFunctions as db

options = tools.FileRead('configuration/options.txt')

def save(window, CodClie, TemplateName, apellidos, nombres, inpre, ImagePath, FechaInscripcion = None, NumeroInscripcion = None, folio = None, sangre = None, telefono = None):
 
    if ct.IsCedula(CodClie, window) == False:
        return
    
    if len(CodClie) < 5 and len(CodClie) > 10:
        showerror("Error en el número de cedula", "El número de cedula no tiene la cantidad de caracteres correcta, intente de nuevo, si el problema persiste contacte con el soporte.", parent = window)    
        return
        
    connection = db.ConnectLocal()
    if connection == False:
        return

    if TemplateName == 'AbgTemplate.png' or TemplateName == 'AbgTemplateExo.png': 
            
        try:
            
            FechaInscripcion = datetime.strptime(FechaInscripcion,'%d-%m-%Y')

        except:

            showerror("Error en la fecha de inscripcion", "El formato de la fecha introducida es incorrecto, intente de nuevo, si el problema persiste contacte con el soporte.", parent = window)    
            return
        
        row = (db.SelectCodClie("savecarnets", connection, CodClie))[0]
        if row == False:
            return
        
        if row == None:
        
            try:

                consult =("INSERT INTO savecarnets(CodClie, template, apellidos, nombres, inpre, FechaInscripcion, NumeroInscripcion, folio, ImagePath) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')").format(CodClie, TemplateName, apellidos, nombres, inpre, FechaInscripcion, NumeroInscripcion, folio, ImagePath)
                cursor = connection.cursor()  
                cursor.execute(consult)
                connection.commit()

                showinfo("Carnet guardado", "Su carnet ha sido guardado de forma exitosa.", parent = window)

                return

            except:

               showerror("Error de guardado", "No se completo el guardado, intente de nuevo, si el problema persiste contacte con el soporte.", parent = window)
               return

        else:

            try:

                db.UpdateMysqlCodClie("savecarnets", "template", TemplateName, CodClie, connection)
                db.UpdateMysqlCodClie("savecarnets", "apellidos", apellidos, CodClie, connection)
                db.UpdateMysqlCodClie("savecarnets", "nombres", nombres, CodClie, connection)
                db.UpdateMysqlCodClie("savecarnets", "inpre", inpre, CodClie, connection)
                db.UpdateMysqlCodClie("savecarnets", "FechaInscripcion", FechaInscripcion, CodClie, connection)
                db.UpdateMysqlCodClie("savecarnets", "NumeroInscripcion", NumeroInscripcion, CodClie, connection)
                db.UpdateMysqlCodClie("savecarnets", "folio", folio, CodClie, connection)
                db.UpdateMysqlCodClie("savecarnets", "ImagePath", ImagePath, CodClie, connection)

                showinfo("Carnet guardado", "Su carnet ha sido guardado de forma exitosa.", parent = window)
                return

            except:

               showerror("Error de guardado", "No se completo el guardado, intente de nuevo, si el problema persiste contacte con el soporte.", parent = window)
               return


    if TemplateName == "FamTemplate.png":

        row = (db.SelectCodClie("savecarnets", connection, CodClie))[0]
        if row == False:
            return
        
        if row == None:

            try:

                consult =("INSERT INTO savecarnets(CodClie, template, apellidos, nombres, inpre, sangre, telefono, ImagePath) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')").format(CodClie, TemplateName, apellidos, nombres, inpre, sangre, telefono, ImagePath)
                cursor = connection.cursor()  
                cursor.execute(consult)
                connection.commit()

                showinfo("Carnet guardado", "Su carnet ha sido guardado de forma exitosa.", parent = window)

                return

            except:

                showerror("Error de guardado", "No se completo el guardado, intente de nuevo, si el problema persiste contacte con el soporte.", parent = window)
                return

        else:

            try:

                db.UpdateMysqlCodClie("savecarnets", "template", TemplateName, CodClie, connection)
                db.UpdateMysqlCodClie("savecarnets", "apellidos", apellidos, CodClie, connection)
                db.UpdateMysqlCodClie("savecarnets", "nombres", nombres, CodClie, connection)
                db.UpdateMysqlCodClie("savecarnets", "inpre", inpre, CodClie, connection)
                db.UpdateMysqlCodClie("savecarnets", "sangre", sangre, CodClie, connection)
                db.UpdateMysqlCodClie("savecarnets", "telefono", telefono, CodClie, connection)
                db.UpdateMysqlCodClie("savecarnets", "ImagePath", ImagePath, CodClie, connection)

                showinfo("Carnet guardado", "Su carnet ha sido guardado de forma exitosa.", parent = window)

                return

            except:

               showerror("Error de guardado", "No se completo el guardado, intente de nuevo, si el problema persiste contacte con el soporte.", parent = window)
               return


def search(CodClie, ApellidosEntry, NombresEntry, CedulaEntry, InpreEntry, MenuBar, profile, root, TemplateName, FechaInscripcionEntry = None, NumeroInscripcionEntry = None, FolioEntry = None, SangreEntry = None, TelefonoEntry = None, messages = False):

    global ImagePath
    
    def ChangeEntries(CodClie):

        consult = db.SelectLikeCodClie("savecarnets", connection, CodClie, messages)
        row = consult[0]
        cursor = consult[1] 
        if row == False:
            return False

        while row:

            FillApellidos = row[2]
            FillNombres = row[3]
            FillCedula = row[0]
            FillInpre = row[4]
            try:
                FillFecha = datetime.strptime((str(row[5]).split(sep=" "))[0], "%Y-%m-%d")
            except:
                FillFecha = ""
                pass
            FillFolio = row[7]
            FillNumero = row[6]
            FillImage = row[10]
            FillSangre = row[8]
            FillTelefono = row[9]

            row = cursor.fetchone()

        try:
            FillFecha = FillFecha.strftime('%d-%m-%Y')
        except:
            pass

        ApellidosEntry.delete(0, END)
        ApellidosEntry.insert(0, FillApellidos)

        NombresEntry.delete(0, END)
        NombresEntry.insert(0, FillNombres)

        CedulaEntry.delete(0, END)
        CedulaEntry.insert(0, FillCedula)

        InpreEntry.delete(0, END)
        InpreEntry.insert(0, FillInpre)

        if FechaInscripcionEntry != None:
            FechaInscripcionEntry.config(state="normal")
            FechaInscripcionEntry.delete(0, END)
            FechaInscripcionEntry.insert(0, FillFecha)
            FechaInscripcionEntry.config(state="disabled")

        if NumeroInscripcionEntry != None:
            NumeroInscripcionEntry.delete(0, END)
            NumeroInscripcionEntry.insert(0, FillNumero)

        if FolioEntry != None:
            FolioEntry.delete(0, END)
            FolioEntry.insert(0, FillFolio)

        if SangreEntry != None:
            SangreEntry.delete(0, END)
            SangreEntry.insert(0, FillSangre)

        if TelefonoEntry != None:
            TelefonoEntry.delete(0, END)
            TelefonoEntry.insert(0, FillTelefono)

        global ProfileImage
        global ImagePath
        ImagePath = FillImage
        
        try:
            ProfileImage = ImageTk.PhotoImage(file=ImagePath)
            profile.config(image=ProfileImage)
        except:
            ProfileImage = ImageTk.PhotoImage(file='assets/ProfileImageButton.png')
            profile.config(image=ProfileImage)
            pass

        return True

    connection = db.ConnectLocal(messages)
    if connection == False:
        return False

    if ct.IsCedula(CodClie, root, messages) == False:
        return False  
    
    if len(CodClie) < 5 and len(CodClie) > 10:
        showerror("Error en el número de cedula", "El número de cedula no tiene la cantidad de caracteres correcta, intente de nuevo, si el problema persiste contacte con el soporte.", parent = root)    
        return
    
    CodClie = ct.PutPoints(CodClie)

    row = db.SelectCountLikeCodClie("savecarnets", connection, CodClie, messages)

    if int(row[0]) == 1:

        consult = db.SelectLikeCodClie("savecarnets", connection, CodClie, messages)
        registros2 = consult[0]
        cursor = consult[1]
        if registros2 == False:
            return False
        
        while registros2:

            template = registros2[1]

            registros2 = cursor.fetchone()

        if template == TemplateName:

            ChangeEntries(CodClie)

            return True

        else:

            root.destroy()

            if template == "AbgTemplate.png":
                mf.ShowTemplate(r"TemplateImages\AbgTemplate.png", CodClie)
            elif template == "FamTemplate.png":
                mf.ShowTemplate(r"TemplateImages\FamTemplate.png", CodClie)

            return True

    elif int(row[0]) > 1:

        consult = db.SelectLikeCodClie("savecarnets", connection, CodClie, messages)
        registros2 = consult[0]
        cursor = consult[1]
        if registros2 == False:
            return False

        MenuBar.entryconfig("Buscar", state='disabled')
        ventana = Toplevel()
        ventana.transient(root)
        ventana.iconbitmap("assets/logo.ico")
        ventana.resizable(False,False)
        tools.CenterWindow("500", "313", ventana)
        ventana.title('Presiona "Enter" para confirmar tu selección')
        ventana.focus()

        style = ttk.Style()
        style.configure("Treeview.Heading", font=("Arial Bold", 12))
        style.configure("Treeview", font=("Arial Bold", 10))
        
        tv = ttk.Treeview(ventana, columns=("col1", "col2"), height= 30, selectmode="browse")
        tv.column("#0", width=100)
        tv.column("col1", width=80, anchor=CENTER)
        tv.column("col2", width=300, anchor=CENTER)
            
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

                if messages == True:
                    showwarning("Error de selección",
                    "Seleccione una persona primero", parent = ventana)

                return False
            
            else:
                
                for item in selected_items:

                    txt = (tv.item(item)["text"])
                    val = (tv.item(item)["values"])

                if val[2] == TemplateName:

                    ChangeEntries(txt)

                else:

                    root.destroy()

                    if val[2] == "AbgTemplate.png":
                        mf.ShowTemplate(r"TemplateImages\AbgTemplate.png", txt)
                    elif val[2] == "FamTemplate.png":
                        mf.ShowTemplate(r"TemplateImages\FamTemplate.png", txt)

            MenuBar.entryconfig("Buscar", state='normal')
            ventana.destroy() 
            return True 

        while registros2:

            tv.insert("", END, text= registros2[0], values=(registros2[4], registros2[3], registros2[1]))

            registros2 = cursor.fetchone()

        def on_close():

            MenuBar.entryconfig("Buscar", state='normal')
            ventana.destroy()

        ventana.protocol("WM_DELETE_WINDOW", on_close)     

        def key(event):

            if event.keysym == "Escape":
                
                on_close()

            elif event.keysym == "Return":
                    
                yesorno = askyesno(title= "¿Desea confirmar la seleccion?", message= "¿Desea confirmar la seleccion?", parent = ventana)

                if yesorno == True:
                    
                    get_selected_items()
        
        ventana.bind("<Key>", key) 

    elif int(row[0]) == 0:

        if messages == True:
        
            showwarning("Cédula no encontrada",
                "No se encuentra ningun carnet guardado que coincida con la Cédula de Identidad introducida, intente de nuevo, si el problema persiste contacte con el soporte.", parent = root)

        return False
    
def ReturnImagePath():

    global ImagePath

    return ImagePath

def clear(ApellidosEntry, NombresEntry, CedulaEntry, InpreEntry, FechaInscripcionEntry, NumeroInscripcionEntry, FolioEntry, SangreEntry, TelefonoEntry, EmisionEntry, VencimientoEntry):

    ApellidosEntry.delete(0, END)
    NombresEntry.delete(0, END)
    CedulaEntry.delete(0, END)
    InpreEntry.delete(0, END)

    if FechaInscripcionEntry != None:

        FechaInscripcionEntry.config(state="normal")
        FechaInscripcionEntry.delete(0, END)
        FechaInscripcionEntry.config(state="disabled")
    
    if NumeroInscripcionEntry != None:
        
        NumeroInscripcionEntry.delete(0, END)

    if FolioEntry != None:

        FolioEntry.delete(0, END)
    
    if SangreEntry != None:
        
        SangreEntry.delete(0, END)

    if TelefonoEntry != None:

        TelefonoEntry.delete(0, END)

    if EmisionEntry != None:

        EmisionEntry.delete(0, END)
    
    if VencimientoEntry != None:

        VencimientoEntry.delete(0, END)

def change(TemplateName, CodClie, root):

    root.destroy()

    if TemplateName == 'AbgTemplate.png' or TemplateName == 'AbgTemplateExo.png':

        if tools.IsConnected():
            connection = db.ConnectCloud()
            if connection == False:
                return

            row = db.SelectCountLikeCodClie("SACLIE", connection, CodClie)
            if int(row[0]) != 0:
                showwarning("Error de cedula",
                    "La cedula ingresada puede que pertenezca a un abogado, intente de nuevo, si el problema persiste contacte con el soporte.", parent= root)
                return

        window = Tk()
        window.iconbitmap("assets/logo.ico")
        window.resizable(False,False)
        window.title('Presiona "Enter" para confirmar tu selección')
        tools.CenterWindow("300", "113", window)
        window.focus()

        CedulaAbogado = StringVar()
        CedulaAbogadoLabel = Label(window, text = "CEDULA DEL ABOGADO", font = ("Arial Bold", 19))
        CedulaAbogadoLabel.place(x = 0, y = 0)
        CedulaAbogadoEntry = Entry(window, textvariable = CedulaAbogado, width = "9", font = ("Arial Bold", 19), fg = 'black', bg="white")
        CedulaAbogadoEntry.place(x = 87, y = 50)
        ct.CedulaLiveCT(CedulaAbogado, CedulaAbogadoEntry, partial= True)

        def key(event):

            if event.keysym == "Return":

                if ct.GetCedulaStatus() == 1:
                    
                    yesorno = askyesno(title= "¿Desea confirmar la seleccion?", message= "¿Desea confirmar la seleccion?", parent = window)

                    if yesorno == True:
                        CodClieAbogado = CedulaAbogado.get()

                        if ct.IsCedula(CodClieAbogado, window) == False:
                            return
                        
                        if len(CodClieAbogado) == 0:
                            showwarning("Error de usuario",
                                    "Es necesario rellenar el campo CEDULA DEL ABOGADO, intente de nuevo, si el problema persiste contacte con el soporte.", parent = window)
                            return
                        
                        if tools.IsConnected():

                            connection = db.ConnectCloud()
                            if connection == False:
                                return
                            
                            CodClieAbogado = ct.RemovePoints(CodClieAbogado)

                            row = db.SelectCountLikeCodClie("SACLIE", connection, CodClieAbogado)

                            if int(row[0]) == 1:
                                
                                window.destroy()
                                mf.ShowTemplate(r"TemplateImages\FamTemplate.png", CodClie, CodClieAbogado)

                            elif int(row[0]) > 1:

                                consult = db.SelectLikeCodClie("SACLIE", connection, CodClieAbogado)
                                registros2 = consult[0]
                                cursor = consult[1] 
                                if registros2 == False:
                                    return
                                
                                ventana = Toplevel()
                                ventana.iconbitmap("assets/logo.ico")
                                ventana.transient(window)
                                ventana.resizable(False,False)
                                tools.CenterWindow("500", "313", ventana)
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
                                        "Seleccione una persona primero", parent = ventana)

                                        return
                                    
                                    else:
                                        
                                        for item in selected_items:

                                            txt = (tv.item(item)["text"])

                                        window.destroy()
                                        mf.ShowTemplate(r"TemplateImages\FamTemplate.png", CodClie, txt)
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
                                    "El número de cédula introducido no se encuentra registrado en la base de datos del Colegio de Abogados del Estado Carabobo, intente de nuevo, si el problema persiste contacte con el soporte.", parent = window)

                                return
                            
                        else:
                            mf.ShowTemplate(r"TemplateImages\FamTemplate.png", CodClie, CodClieAbogado)
                else:
                    showwarning("Error de usuario",
                        "Hay un error en el campo de entrada CEDULA DEL ABOGADO, intente de nuevo, si el problema persiste contacte con el soporte.", parent= window)

        window.bind("<Key>", key)

    elif TemplateName == "FamTemplate.png":
        mf.ShowTemplate(r"TemplateImages\AbgTemplate.png", CodClie)

def fill(CodClie, ApellidosEntry, NombresEntry, CedulaEntry, InpreEntry, FechaInscripcionEntry, NumeroInscripcionEntry, FolioEntry, MenuBar, root, messages = False):

    def ChangeEntries(CodClie):

        consult = db.SelectLikeCodClie("SACLIE", connection, CodClie, messages)
        row = consult[0]
        cursor = consult[1] 
        if row == False:
            return False

        while row:

            FillDescrip = row[1]
            FillCedula = row[0]
            FillInpre = row[4]

            row = cursor.fetchone()

        consult = db.SelectLikeCodClie("SACLIE_08", connection, CodClie, messages)
        row = consult[0]
        cursor = consult[1] 
        if row == False:
            return False

        while row:

            FillFecha = datetime.strptime((str(row[4]).split(sep=" "))[0], "%Y-%m-%d")
            FillFolio = row[2]
            FillNumero = row[1]

            row = cursor.fetchone()

        FillDescrip = FillDescrip.split(sep=" ")

        FillApellidos = ""

        for i in reversed(range(2)):

            i = i + 1

            if i == 1:

                FillApellidos = FillApellidos + " " + FillDescrip[-i]

            elif i == 2:

                FillApellidos = FillApellidos + FillDescrip[-i]

            FillDescrip.remove(FillDescrip[-i])

        FillNombres = ""
        
        for i in range(len(FillDescrip)):

            if i == 0:

                FillNombres = FillNombres + FillDescrip[i] + " "

            elif i != len(FillDescrip):

                FillNombres = FillNombres + " " + FillDescrip[i]
        
        FillCodClie = ""

        for i in FillCedula:
            if i in '0123456789.':
                FillCodClie = FillCodClie + i

        FillCodClie = '{:,}'.format(int(FillCodClie)).replace(',', '.')

        FillInpre = '{:,}'.format(int(FillInpre)).replace(',', '.')

        FillNumero = '{:,}'.format(int(FillNumero)).replace(',', '.')
        
        FillFolio = '{:,}'.format(int(FillFolio)).replace(',', '.')

        FillFecha = FillFecha.strftime('%d-%m-%Y')

        ApellidosEntry.delete(0, END)
        ApellidosEntry.insert(0, FillApellidos)

        NombresEntry.delete(0, END)
        NombresEntry.insert(0, FillNombres)

        CedulaEntry.delete(0, END)
        CedulaEntry.insert(0, FillCodClie)

        InpreEntry.delete(0, END)
        InpreEntry.insert(0, FillInpre)

        FechaInscripcionEntry.config(state="normal")
        FechaInscripcionEntry.delete(0, END)
        FechaInscripcionEntry.insert(0, FillFecha)
        FechaInscripcionEntry.config(state="disabled")

        NumeroInscripcionEntry.delete(0, END)
        NumeroInscripcionEntry.insert(0, FillNumero)

        FolioEntry.delete(0, END)
        FolioEntry.insert(0, FillFolio)

        return True

    if tools.IsConnected():

        connection = db.ConnectCloud(messages)
        if connection == False:
            return False
        
        if ct.IsCedula(CodClie, root, messages) == False:
            return False
        
        if len(CodClie) < 5 and len(CodClie) > 10:
            showerror("Error en el número de cedula", "El número de cedula no tiene la cantidad de caracteres correcta, intente de nuevo, si el problema persiste contacte con el soporte.", parent = root)    
            return
    
        CodClie = ct.RemovePoints(CodClie)

        row = db.SelectCountLikeCodClie("SACLIE", connection, CodClie, messages)

        if int(row[0]) == 1:

            ChangeEntries(CodClie)

            return True

        elif int(row[0]) > 1:

            consult = db.SelectLikeCodClie("SACLIE", connection, CodClie, messages)
            registros2 = consult[0]
            cursor = consult[1] 
            if registros2 == False:
                return False

            MenuBar.entryconfig("Rellenar", state='disabled')
            ventana = Toplevel()
            ventana.iconbitmap("assets/logo.ico")
            ventana.transient(root)
            ventana.resizable(False,False)
            tools.CenterWindow("500", "313", ventana)
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
                    
                    if messages == True:
                        showwarning("Error de selección",
                        "Seleccione una persona primero", parent = ventana)

                    return False
                
                else:
                    
                    for item in selected_items:

                        txt = (tv.item(item)["text"])
        
                    ChangeEntries(txt)

                MenuBar.entryconfig("Rellenar", state='normal')
                ventana.destroy()  
                return True

            while registros2:

                tv.insert("", END, text= registros2[0], values=(registros2[4], registros2[1]))

                registros2 = cursor.fetchone()

            def on_close():

                MenuBar.entryconfig("Rellenar", state='normal')
                ventana.destroy()

            ventana.protocol("WM_DELETE_WINDOW", on_close)     

            def key(event):
    
                if event.keysym == "Escape":
                    
                    on_close()

                elif event.keysym == "Return":
                        
                    yesorno = askyesno(title= "¿Desea confirmar la seleccion?", message= "¿Desea confirmar la seleccion?", parent = ventana)

                    if yesorno == True:
                        
                        get_selected_items()
            
            ventana.bind("<Key>", key) 

        elif int(row[0]) == 0:

            if messages == True:
            
                showwarning("Cédula no encontrada",
                    "El número de cédula introducido no se encuentra registrado en la base de datos del Colegio de Abogados del Estado Carabobo, intente de nuevo, si el problema persiste contacte con el soporte.", parent = root)

            return False

    else:

        if messages == True:

            showerror("No hay conexión a internet",
                    "Usted no se encuentra conectado a internet, no podra usar esta función hasta que vuelva a estar en linea, si el problema persiste contacte con el soporte.", parent = root)

        return False

def finish(TemplateName, CodClie, CodClieAbogado, root, emision, vencimiento, apellidos, nombres, inpre, ImagePath, FechaInscripcion = None, NumeroInscripcion = None, folio = None, sangre = None, telefono = None):

    global options

    if (len(apellidos) < 3 and len(apellidos) > 29) or (len(nombres) < 3 and len(nombres) > 29):
        showerror("Error en los nombres", "El nombre no tiene la cantidad de caracteres correcta, intente de nuevo, si el problema persiste contacte con el soporte.", parent = root)    
        return
    
    if len(inpre) < 2 and len(inpre) > 10:
        showerror("Error en el número de inpre", "El inpre no tiene la cantidad de caracteres correcta, intente de nuevo, si el problema persiste contacte con el soporte.", parent = root)    
        return
    
    if ImagePath == "":
        showerror("Error en la imagen de perfil", "No ha seleccionado ninguna imagen, intente de nuevo, si el problema persiste contacte con el soporte.", parent = root)    
        return

    if TemplateName == 'AbgTemplate.png' or TemplateName == 'AbgTemplateExo.png':

        def FinishLine():
            solv = db.SelectCodClieWithStatus("SOLV", connection, CodClie, 1)
            if solv[0] == False:
                return
            elif solv[0] != None:
                try:
                    #save(root, PrintCodClie, TemplateName, apellidos, nombres, inpre, ImagePath, FechaInscripcion, NumeroInscripcion, folio, sangre, telefono)
                    FinallyImagePath = (imf.FinallyImage(ImagePath, TemplateName, emision, vencimiento, apellidos, nombres, inpre, FechaInscripcion, NumeroInscripcion, folio, PrintCodClie, sangre, telefono, TemplateName == 'AbgTemplateExo.png')).replace("/", "\\")
                    imf.PrintImage(FinallyImagePath)
                    yesorno = askyesno(title= "Impresión de carnet", message= "¿El carnet fue impreso correctamente?")
                    while yesorno == False:
                        imf.PrintImage(FinallyImagePath)
                        yesorno = askyesno(title= "Impresión de carnet", message= "¿El carnet fue impreso correctamente?")
                    mf.NewCarnet(root)
                except:
                    showerror("Error de Actualización", "No se pudieron actualizar los datos, intente de nuevo, si el problema persiste contacte con el soporte.")   
                    return
            elif solv[0] == None:
                consult = db.SelectLikeCodClie("SAFACT", connection, CodClie)
                registros2 = consult[0]
                cursor = consult[1] 
                if registros2 == False:
                    return
                
                ventana = Toplevel()
                ventana.iconbitmap("assets/logo.ico")
                ventana.transient(root)
                ventana.resizable(False,False)
                tools.CenterWindow("1000", "313", ventana)
                ventana.title('Presiona "Enter" para confirmar tu selección')
                ventana.focus()

                style = ttk.Style()
                style.configure("Treeview.Heading", font=("Arial Bold", 12))
                style.configure("Treeview", font=("Arial Bold", 10))
                
                tv = ttk.Treeview(ventana, columns=("col1", "col2", "col3"), height= 30, selectmode="browse")
                tv.column("#0", width=70)
                tv.column("col1", width=70, anchor=CENTER)
                tv.column("col2", width=652, anchor=CENTER)
                tv.column("col3", width=0, anchor=CENTER)
                    
                tv.heading("#0", text="N° de factura", anchor=CENTER)
                tv.heading("col1", text="Fecha", anchor=CENTER)
                tv.heading("col2", text="Nota", anchor=CENTER)
                    
                tv.pack(side='left') # supongo que sabes usar pack

                ejscrollbar= ttk.Scrollbar(ventana,orient=VERTICAL,command=tv.yview)
                ejscrollbar.pack(side='right',fill='y')
                tv.configure(yscrollcommand=ejscrollbar.set) 

                def get_selected_items():

                    selected_items = tv.selection()

                    if len(selected_items) == 0:
                            
                        showwarning("Error de selección",
                        "Seleccione una operación primero", parent = ventana)

                        return
                    
                    else:

                        solv = db.SelectCodClieWithStatus("SOLV", connection, CodClie, 1)
                        if solv[0] == False:
                            return
                        elif solv[0] != None:
                            try:
                                showinfo("Carnet actualizado", "¡Carnet actualizado con exito!", parent = root)
                                #save(root, PrintCodClie, TemplateName, apellidos, nombres, inpre, ImagePath, FechaInscripcion, NumeroInscripcion, folio, sangre, telefono)
                                FinallyImagePath = (imf.FinallyImage(ImagePath, TemplateName, emision, vencimiento, apellidos, nombres, inpre, FechaInscripcion, NumeroInscripcion, folio, PrintCodClie, sangre, telefono, TemplateName == 'AbgTemplateExo.png')).replace("/", "\\")
                                imf.PrintImage(FinallyImagePath)
                                yesorno = askyesno(title= "Impresión de carnet", message= "¿El carnet fue impreso correctamente?")
                                while yesorno == False:
                                    imf.PrintImage(FinallyImagePath)
                                    yesorno = askyesno(title= "Impresión de carnet", message= "¿El carnet fue impreso correctamente?")
                                mf.NewCarnet(root)
                            except:
                                showerror("Error de Actualización", "No se pudieron actualizar los datos, intente de nuevo, si el problema persiste contacte con el soporte.")   
                                return
                        elif solv[0] == None:
                        
                            for item in selected_items:

                                txt = (tv.item(item)["text"])
                
                            NumeroD = txt

                            try:
                                db.insert("SOLV", "NumeroD, hasta, CodClie, CarnetNum2, status", ("'{}', '{}', '{}', '{}', 1").format(NumeroD, hasta.get(), CodClie, "0"), connection)
                                showinfo("Carnet insertado", "¡Carnet insertado con exito!", parent = root)
                                #save(root, PrintCodClie, TemplateName, apellidos, nombres, inpre, ImagePath, FechaInscripcion, NumeroInscripcion, folio, sangre, telefono)
                                FinallyImagePath = (imf.FinallyImage(ImagePath, TemplateName, emision, vencimiento, apellidos, nombres, inpre, FechaInscripcion, NumeroInscripcion, folio, PrintCodClie, sangre, telefono, TemplateName == 'AbgTemplateExo.png')).replace("/", "\\")
                                imf.PrintImage(FinallyImagePath)
                                yesorno = askyesno(title= "Impresión de carnet", message= "¿El carnet fue impreso correctamente?")
                                while yesorno == False:
                                    imf.PrintImage(FinallyImagePath)
                                    yesorno = askyesno(title= "Impresión de carnet", message= "¿El carnet fue impreso correctamente?")
                                mf.NewCarnet(root)
                            except:
                                showerror("Error de Inserción", "No se pudieron insertar los datos, intente de nuevo, si el problema persiste contacte con el soporte.")   
                                return
                            
                    ventana.destroy()  

                while registros2:

                    FechaE = registros2[46]
                    FechaE = datetime.strftime(FechaE,'%Y-%m-%d %H:%M:%S.%f')
                    FechaE = FechaE.split(sep = ' ')
                    FechaE = FechaE[0]
                    FechaE = datetime.strptime(FechaE,'%Y-%m-%d')

                    OrdenC = registros2[73]
                    Notas = ""
                    
                    if OrdenC != None:
                        Notas = Notas + OrdenC

                    for i in range(6):
                        i = i + 81
                        if registros2[i] != None:
                            Notas = Notas + " " + registros2[i]

                    tv.insert("", END, text= registros2[1], values=(FechaE, Notas))

                    registros2 = cursor.fetchone()  

                hasta = StringVar()
                HastaLabel = Label(ventana, text = "Vencimiento", font = ("Arial Bold", 12))
                HastaLabel.place(x = 840, y = 10)
                HastaLabel2 = Label(ventana, text = "de solvencia", font = ("Arial Bold", 12))
                HastaLabel2.place(x = 840, y = 35)
                HastaEntry = Entry(ventana, textvariable = hasta, width = "9", font = ("Arial Bold", 19), fg = 'black', bg="white")
                HastaEntry.place(x = 798, y = 70)
                HastaEntry.config(state="disabled")
            
                global CalendarImage
                CalendarImage = ImageTk.PhotoImage(file='assets/calendar.png')
                HastaCalendarButton = Button(ventana, command=lambda: tools.SetDate(ventana, HastaEntry, YearMonthDay=True), image=CalendarImage)
                HastaCalendarButton.place(x = 935,y = 68)

                HelpLabel = Label(ventana, text = "Seleccione la operación", font = ("Arial Bold", 12))
                HelpLabel.place(x = 795, y = 200)
                HelpLabel2 = Label(ventana, text = "de solvencia", font = ("Arial Bold", 12))
                HelpLabel2.place(x = 840, y = 225)

                vinculo = options[1].replace("~", CodClie)
                def link():
                    webbrowser.open_new(vinculo)

                NavegatorButton = Button(ventana, text='Ver en navegador', font = ("Arial Bold", 12), fg="blue", command=link)
                NavegatorButton.place(x = 815, y= 265)
                
                def key(event):

                    if event.keysym == "Return":

                        if hasta.get() != "":
                            
                            yesorno = askyesno(title= "¿Desea confirmar la seleccion?", message= "¿Desea confirmar la seleccion?", parent = ventana)

                            if yesorno == True:
                                
                                get_selected_items()
                
                ventana.bind("<Key>", key) 

        if len(CodClie) < 5 and len(CodClie) > 10:
            showerror("Error en el número de cedula", "El número de cedula no tiene la cantidad de caracteres correcta, intente de nuevo, si el problema persiste contacte con el soporte.", parent = root)    
            return
        
        if len(NumeroInscripcion) < 2 and len(NumeroInscripcion) > 10:
            showerror("Error en el número de inscripción", "El número de inscripción no tiene la cantidad de caracteres correcta, intente de nuevo, si el problema persiste contacte con el soporte.", parent = root)    
            return
        
        if len(folio) < 2 and len(folio) > 10:
            showerror("Error en el número de folio", "El número de folio no tiene la cantidad de caracteres correcta, intente de nuevo, si el problema persiste contacte con el soporte.", parent = root)    
            return

        yesorno = askyesno(title= "¿Desea confirmar la seleccion?", message= "¿Desea confirmar la seleccion?", parent = root)
    
        if yesorno == True:

            PrintCodClie = CodClie
            CodClie = ct.RemovePoints(CodClie)

            if tools.IsConnected():

                connection = db.ConnectCloud()
                if connection == False:
                    return
                
                result = db.SelectCountLikeCodClie("SACLIE", connection, CodClie)
                
                if int(result[0]) == 0:
                    showwarning("Cédula no encontrada",
                        "El número de cédula introducido no se encuentra registrado en la base de datos del Colegio de Abogados del Estado Carabobo, intente de nuevo, si el problema persiste contacte con el soporte.", parent = root)
                    FinishLine()
                
                elif int(result[0]) == 1:

                    FinishLine()
                
                elif int(result[0]) > 1:

                    showwarning("Error 999",
                        "Error 999.", parent = root)
                    return

            else:

                showwarning("Sin conexión a internet.",
                    "Sin conexión a internet.", parent = root)

    elif TemplateName == "FamTemplate.png":

        def FinishLine():
            try:
                #save(root, PrintCodClie, TemplateName, apellidos, nombres, inpre, ImagePath, FechaInscripcion, NumeroInscripcion, folio, sangre, telefono)
                FinallyImagePath = (imf.FinallyImage(ImagePath, TemplateName, emision, vencimiento, apellidos, nombres, inpre, FechaInscripcion, NumeroInscripcion, folio, PrintCodClie, sangre, telefono)).replace("/", "\\")
                imf.PrintImage(FinallyImagePath)
                yesorno = askyesno(title= "Impresión de carnet", message= "¿El carnet fue impreso correctamente?")
                while yesorno == False:
                    imf.PrintImage(FinallyImagePath)
                    yesorno = askyesno(title= "Impresión de carnet", message= "¿El carnet fue impreso correctamente?")
                mf.NewCarnet(root)
            except:
                showerror("Error de Actualización", "No se pudieron actualizar los datos, intente de nuevo, si el problema persiste contacte con el soporte.")   
                return

        if len(CodClie) < 9 and len(CodClie) > 10:
            showerror("Error en el número de cedula", "El número de cedula no tiene la cantidad de caracteres correcta, intente de nuevo, si el problema persiste contacte con el soporte.", parent = root)    
            return
        
        if sangre != "A+" and sangre != "A-" and sangre != "B+" and sangre != "B-" and sangre != "AB+" and sangre != "AB-" and sangre != "O+" and sangre != "O-" and sangre != "OHR+":
            showerror("Error en el tipo de sangre", "El tipo de sangre no es correcto, intente de nuevo, si el problema persiste contacte con el soporte.", parent = root)    
            return
        
        if len(telefono) != 13:
            showerror("Error en el número de telefono", "El número de telefono no tiene la cantidad de caracteres correcta, intente de nuevo, si el problema persiste contacte con el soporte.", parent = root)    
            return

        yesorno = askyesno(title= "¿Desea confirmar la seleccion?", message= ("El número de cedula del abogado es: {}, ¿desea confirmar la seleccion?").format("0", CodClieAbogado), parent = root)
    
        if yesorno == True:

            PrintCodClie = CodClie
            CodClieAbogado = ct.RemovePoints(CodClieAbogado)
            CodClie = ct.RemovePoints(CodClie)

            if tools.IsConnected():

                connection = db.ConnectCloud()
                if connection == False:
                    return
                
                row = db.SelectCountLikeCodClie("SACLIE", connection, CodClie)
                if int(row[0]) != 0:
                    showwarning("Error de cedula",
                        "La cedula ingresada puede que pertenezca a un abogado, intente de nuevo, si el problema persiste contacte con el soporte.", parent= root)
                    return
                
                result = db.SelectCountLikeCodClie("SACLIE", connection, CodClieAbogado)
                
                if int(result[0]) == 0:
                    showwarning("Cédula no encontrada",
                        "El número de cédula introducido no se encuentra registrado en la base de datos del Colegio de Abogados del Estado Carabobo, intente de nuevo, si el problema persiste contacte con el soporte.", parent = root)
                    FinishLine()
                
                elif int(result[0]) == 1:
                    FinishLine()
                
                elif int(result[0]) > 1:
                    showwarning("Error 999",
                        "Error 999.", parent = root)
                    return

            else:
                showwarning("Sin conexión a internet.",
                    "Sin conexión a internet.", parent = root)