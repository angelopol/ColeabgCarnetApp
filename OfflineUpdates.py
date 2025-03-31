import tools
import DatabaseFunctions as db
import pyodbc
import pymssql
import pymysql
import time

while True:

    if tools.IsConnected():

        try:

            process = 0
            process2 = 0
            
            connection = db.ConnectLocal(False)
            if connection == False:
                print("Error de conexión con base de datos local.")
            connection2 = db.ConnectCloud(False)
            if connection2 == False:
                print("Error de conexión con base de datos en la nube PYMSSQL.")
            cnxn = db.ConnectCloudPyodbc()
            if cnxn == False:
                print("Error de conexión con base de datos en la nube PYODBC.")

            cursor = connection.cursor()  
            consult =("SELECT * FROM offlineconsults WHERE execute = 0 ORDER BY InsertAt")  
            cursor.execute(consult)  
            row = cursor.fetchone()

            if row == None:
                print("Ninguna migración pendiente.")
            else:

                cursorCount = connection.cursor()  
                consultCount =("SELECT COUNT(*) FROM offlineconsults WHERE execute = 0")  
                cursorCount.execute(consultCount)  
                rowCount = cursorCount.fetchone()

                print("Migraciones pendientes: " + str(rowCount[0]))

                while row:

                    columns = row[3].split(sep=",")
                    values = row[4].split(sep=",")
                    for i in range(len(values)):
                        values[i] = values[i].replace("~", "'")

                    cursor2 = connection2.cursor()  
                    consult2 =("SELECT * FROM SOLV WHERE CodClie = {} AND Status = 1").format(values[columns.index("CodClie")])  
                    cursor2.execute(consult2)
                    row2 = cursor2.fetchone()

                    if row2 != None:
                        
                        consult3 = "UPDATE SOLV SET CarnetNum2 = {} WHERE CodClie = {} AND Status = 1;".format(values[columns.index("CarnetNum2")], values[columns.index("CodClie")])
                        cursor3 = cnxn.cursor()  
                        cursor3.execute(consult3)
                        cnxn.commit()

                        consultExecute = "UPDATE offlineconsults SET execute = 1 WHERE id = {}".format(row[0])
                        cursorExecute = connection.cursor()
                        cursorExecute.execute(consultExecute)
                        connection.commit()

                        process = process + 1

                    else:

                        consult3 = "INSERT INTO SOLV({}) VALUES({})".format(row[3], row[4].replace("~", "'"))
                        cursor3 = cnxn.cursor()  
                        cursor3.execute(consult3)
                        cnxn.commit()

                        consultExecute = "UPDATE offlineconsults SET execute = 1 WHERE id = {}".format(row[0])
                        cursorExecute = connection.cursor()
                        cursorExecute.execute(consultExecute)
                        connection.commit()

                        process2 = process2 + 1

                    row = cursor.fetchone()
            
        except:

            print("Ha ocurrido un error.")

    else:

        print("No posees conexión a internet")

    if process != 0:

        print("Número de cambios: " + str(process))

    else:

        print("Sin cambios.")

    if process2 != 0:

        print("Número de inserciones: " + str(process))

    else:

        print("Sin inserciones.")

    print("Tiempo de espera de 1 minuto.")

    time.sleep(60)