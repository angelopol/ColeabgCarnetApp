from tkinter.messagebox import *
import pymssql
import pymysql
import pyodbc
import tools

def ConnectLocal(messages = True):
    ConnectionInfo = tools.FileRead('configuration/LocalDB.txt')
    try:
        connection = pymysql.connect(host=ConnectionInfo[0], user=ConnectionInfo[1], password=ConnectionInfo[2], database=ConnectionInfo[3])
    except:
        if messages == True:
            showerror("Error de conexión a base de datos",
                    "No se puede realizar la conexión con la base de datos local, intente de nuevo, si el problema persiste contacte con el soporte.")
        return False
    return connection

def ConnectCloud(messages = True):
    ConnectionInfo = tools.FileRead('configuration/CloudDB.txt')
    try:
        connection = pymssql.connect(server=ConnectionInfo[0], user=ConnectionInfo[1], password=ConnectionInfo[2], database=ConnectionInfo[3])
    except:
        if messages == True:
            showerror("Error de conexión a base de datos",
                "No se puede realizar la conexión con la base de datos del Colegio de Abogados del Estado Carabobo, intente de nuevo, si el problema persiste contacte con el soporte.")
        return False
    return connection

def ConnectCloudPyodbc():
    ConnectionInfo = tools.FileRead('configuration/CloudDB.txt')
    server = ConnectionInfo[0]
    database = ConnectionInfo[3]
    username = ConnectionInfo[1]
    password = ConnectionInfo[2]

    try:
        cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    except:
        return False
    return cnxn

def SelectCodClie(TableName, connection, CodClie, messages = True):
    try:
        consult =("SELECT * FROM " + TableName + " WHERE CodClie = '{}'").format(CodClie) 
        cursor = connection.cursor()  
        cursor.execute(consult)  
        row = cursor.fetchone() 
    except:
        if messages == True:
            showerror("Error de busqueda", "No se realizo la busqueda en la base de datos, intente de nuevo, si el problema persiste contacte con el soporte.")
        return False, False
    return row, cursor

def SelectCountCodClie(TableName, connection, CodClie, messages = True):
    try:
        consult =("SELECT COUNT(*) FROM " + TableName + " WHERE CodClie = '{}'").format(CodClie) 
        cursor = connection.cursor()  
        cursor.execute(consult)  
        row = cursor.fetchone() 
    except:
        if messages == True:
            showerror("Error de busqueda", "No se realizo la busqueda en la base de datos, intente de nuevo, si el problema persiste contacte con el soporte.")
        return False   
    return row

def SelectLikeCodClie(TableName, connection, CodClie, messages = True):
    try:
        consult =("SELECT * FROM " + TableName + " WHERE CodClie like '%{}%'").format(CodClie) 
        cursor = connection.cursor()  
        cursor.execute(consult)  
        row = cursor.fetchone() 
    except:
        if messages == True:
            showerror("Error de busqueda", "No se realizo la busqueda en la base de datos, intente de nuevo, si el problema persiste contacte con el soporte.")
        return False, False
    return row, cursor

def SelectCountLikeCodClie(TableName, connection, CodClie, messages = True):
    try:
        consult =("SELECT COUNT(*) FROM " + TableName + " WHERE CodClie like '%{}%'").format(CodClie) 
        cursor = connection.cursor()  
        cursor.execute(consult)  
        row = cursor.fetchone() 
    except:
        if messages == True:
            showerror("Error de busqueda", "No se realizo la busqueda en la base de datos, intente de nuevo, si el problema persiste contacte con el soporte.")
        return False   
    return row

def SelectCodClieWithStatus(TableName, connection, CodClie, status, messages = True):
    try:
        consult =("SELECT * FROM " + TableName + " WHERE CodClie = '{}' and status = {}").format(CodClie, status)
        cursor = connection.cursor()  
        cursor.execute(consult)  
        row = cursor.fetchone()
    except:
        if messages == True:
            showerror("Error de busqueda", "No se realizo la busqueda en la base de datos, intente de nuevo, si el problema persiste contacte con el soporte.")
        return False, False
    return row, cursor

def UpdateMysqlCodClie(TableName, ColumnName, ColumnValue, CodClie, connection):
    consult =("UPDATE " + TableName + " set " + ColumnName + " = '{}' WHERE CodClie = '{}';").format(ColumnValue, CodClie) 
    cursor = connection.cursor()
    cursor.execute(consult)
    connection.commit()
    return

def UpdateCodClieWithStatus(TableName, ColumnName, ColumnValue, CodClie, status, connection):
    consult =("UPDATE " + TableName + " set " + ColumnName + " = '{}' WHERE CodClie = '{}' and Status = {};").format(ColumnValue, CodClie, status)
    cursor = connection.cursor()
    cursor.execute(consult)
    connection.commit()
    return

def insert(TableName, ColumnNames, values, connection):
    consult =("INSERT INTO " + TableName + "(" + ColumnNames + ")" + "VALUES({});").format(values)
    cursor = connection.cursor()
    cursor.execute(consult)
    connection.commit()
    return