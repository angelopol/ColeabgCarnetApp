from tkinter.messagebox import *

def IsCedula(CodClie, window = False, messages = True):
    for i in CodClie:  
        if i not in '0123456789.':
            if messages == True:
                if window != False:
                    showerror("Error en el número de cédula",
                    "El número de cédula introducido contiene caracteres NO NÚMERICOS, intente de nuevo, si el problema persiste contacte con el soporte.", parent = window)
                else:
                    showerror("Error en el número de cédula",
                    "El número de cédula introducido contiene caracteres NO NÚMERICOS, intente de nuevo, si el problema persiste contacte con el soporte.")
            return False
    return True

def IsNumber(number, window = False, messages = True):
    for i in number:
        if i not in '0123456789':
            if messages == True:
                if window != False:
                    showerror("Error en el número",
                    "El número introducido contiene caracteres NO NÚMERICOS, intente de nuevo, si el problema persiste contacte con el soporte.", parent = window)
                else:
                    showerror("Error en el número",
                    "El número introducido contiene caracteres NO NÚMERICOS, intente de nuevo, si el problema persiste contacte con el soporte.")
            return False
    return True

def AreLetters(word):
    for i in word:
        if i not in 'qwertyuiopasdfghjklzxcvbnmñQWERTYUIOPASDFGHJKLZXCVBNÑMáéíóúÁÉÍÓÚ':
            return False
    return True

def AreWords(word):
    for i in word:
        if i not in 'qwertyuiopasdfghjklzxcvbnmñQWERTYUIOPASDFGHJKLZXCVBNÑMáéíóúÁÉÍÓÚ ':
            return False
    return True

def IsEspace(string):
    for i in string:
        if i not in ' ':
            return False
    return True
    
def PutPoints(CodClie):

    if CodClie.find(".") == -1:
        CodClie = '{:,}'.format(int(CodClie)).replace(',', '.')

        return CodClie
    return CodClie

def RemovePoints(CodClie):
    if str(CodClie).find('.') != -1:
        cedula = CodClie.split(sep=".")
        CodClie = ""

        for i in cedula:
            CodClie = CodClie + i
    return CodClie

def OnlyNumbers(number):
    if IsNumber(number, False, False) == False:
        Number = ""
        for i in str(number):
            if i in '0123456789':
                Number = Number + i
        number = Number
    return number

def OnlyWords(words):
    if AreWords(words) == False:
        Words = ""
        for i in str(words):
            if i in 'qwertyuiopasdfghjklzxcvbnmñQWERTYUIOPASDFGHJKLZXCVBNÑMáéíóúÁÉÍÓÚ ':
                Words = Words + i
        words = Words
    return words

def OnlyCedula(CodClie):
    if IsCedula(CodClie, False, False) == False:
        cedula = ""
        for i in str(CodClie):
            if i in '0123456789.':
                cedula = cedula + i
        CodClie = cedula
    return CodClie

def placeholder(StringVar, entry, value):

    entry.config(fg='#424242')

    global counter
    counter = 0
    def OnEntry(event):
        global counter
        if StringVar.get() == value:
            if counter == 0:
                entry.delete(0, "end") 
                entry.config(fg='black')
            counter = 1
    entry.bind('<FocusIn>', OnEntry)
    entry.insert(0, value)

def OutCedulaLiveCT(cedula, CedulaEntry):

    global OutCedulaStatus
    OutCedulaStatus = 0

    def trace(var, index, mode):
        global OutCedulaStatus

        CodClie = cedula.get()

        CedulaEntry.delete(0, "end")

        ci = ""
        pre = ""
        for i  in CodClie:
            if i not in '0123456789':
                if len(CodClie) >= 8 or len(CodClie) <= 10:
                    if CodClie.find(i) == 1:
                        if i == "-":
                            pre = pre + i
                    if CodClie.find(i) == 0:
                        if i in 'QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm':
                            pre = pre + i
            else:
                ci = ci + i
        CodClie = ci

        if len(CodClie) > 8:
            CodClie = CodClie[:-1]

        if len(pre) > 2:
            pre = pre[:-1]

        if len(CodClie) >= 7 and len(CodClie) <= 8:
            OutCedulaStatus = 1
            CedulaEntry.config(fg='black')

        else:
            OutCedulaStatus = 0
            CedulaEntry.config(fg='red')

        CodClie = pre + CodClie

        CedulaEntry.insert(0, CodClie)

    cedula.trace_add('write', trace)

def GetOutCedulaStatus():
    global OutCedulaStatus
    return OutCedulaStatus

def CedulaLiveCT(cedula, CedulaEntry, Function = "", MenuBar = False, status = False, partial = False):

    global CedulaStatus
    CedulaStatus = 0

    def trace(var, index, mode):
        global CedulaStatus

        CodClie = cedula.get()

        CedulaEntry.delete(0, "end")

        if len(CodClie) > 10:
            CodClie = CodClie[:-1]

        CodClie = OnlyNumbers(CodClie)

        if len(CodClie) <= 9 and len(CodClie) >= 1:

            CodClie = PutPoints(CodClie)

        if status == True:

            if len(CodClie) >= 9 and len(CodClie) <= 10:
                CedulaStatus = 1
                CedulaEntry.config(fg='black')

            else:
                CedulaStatus = 0
                CedulaEntry.config(fg='red')

        if partial == True:

            if len(CodClie) >= 5 and len(CodClie) <= 10:
                CedulaStatus = 1
                CedulaEntry.config(fg='black')

                if Function == "NewCarnet":
                    if MenuBar != False:
                        MenuBar.entryconfig("Abogado", state='normal')
                        MenuBar.entryconfig("Familiar", state='normal')
                        MenuBar.entryconfig("Exonerado", state='normal')
            else:
                CedulaStatus = 0
                CedulaEntry.config(fg='red')

                if Function == "NewCarnet":
                    if MenuBar != False:
                        MenuBar.entryconfig("Abogado", state='disabled')
                        MenuBar.entryconfig("Familiar", state='disabled')
                        MenuBar.entryconfig("Exonerado", state='disabled')

        CedulaEntry.insert(0, CodClie)

    cedula.trace_add('write', trace)

def GetCedulaStatus():
    global CedulaStatus
    return CedulaStatus

def NumberLiveCT(number, NumberEntry):

    def trace(var, index, mode):

        Number = number.get()

        NumberEntry.delete(0, "end")

        if len(Number) > 10:
            Number = Number[:-1]

        Number = OnlyNumbers(Number)

        if len(Number) <= 9 and len(Number) >= 1:

            Number = PutPoints(Number)

        if len(Number) >= 2 and len(Number) <= 10:
            NumberEntry.config(fg='black')
        else:
            NumberEntry.config(fg='red')

        NumberEntry.insert(0, Number)

    number.trace_add('write', trace)

def StringLiveCT(String, StringEntry):

    def trace(var, index, mode):

        upper = 0
        lower = 0
        espace = 0

        TempString = String.get()

        StringEntry.delete(0, "end")

        TempString = OnlyWords(TempString)

        for l in TempString:

            if AreLetters(l):

                if l.isupper() == True:
                    upper = upper + (29/24)
                else:
                    lower = lower + 1

            elif IsEspace(l):

                espace = espace + (29/60)

        maximun = 29 - (upper + lower + espace)

        if maximun < -0.9:

            TempString = TempString[:-1]

        if len(TempString) >= 3 and len(TempString) <= 29:
            StringEntry.config(fg='black')
        else:
            StringEntry.config(fg='red')

        StringEntry.insert(0, TempString)

    String.trace_add('write', trace)