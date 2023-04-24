from db import obtener_conexion


def agregar_paciente(codigo_paciente, nombre, apellido, fecha,edad,DNI,sexo,pais,ciudad,direccion,celular,email):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor1:
        cursor1.execute("""INSERT INTO Paciente (codigo_paciente, Nombres, Apellidos, Fecha_Naci, Edad, DNI, Sexo, Pais, Ciudad, Direccion, Celular, Email) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",(codigo_paciente, nombre, apellido, fecha, edad, DNI, sexo, pais, ciudad, direccion, celular, email))
    conexion.commit()
    conexion.close()
    
def agregar_historial(codigo_paciente, codigo_medico, fecha, descripcion,resultado):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor1:
        cursor1.execute("""INSERT INTO Historial (codigo_medico, codigo_paciente, Fecha, Descripcion, Resultado)
            VALUES (%s, %s, %s, %s, %s)""",(codigo_medico, codigo_paciente, fecha, descripcion, resultado))
    conexion.commit()
    conexion.close()
    
def obtener_paciente():
    conexion = obtener_conexion()
    pacientes = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT id_paciente, codigo_paciente, Nombres, Apellidos, Fecha_Naci, Edad, DNI, Sexo, Pais, Ciudad, Direccion, Celular, Email FROM Paciente ORDER BY id_paciente ASC")
        pacientes = cursor.fetchall()
    conexion.close()
    return pacientes

def obtener_medico(user):
    conexion = obtener_conexion()
    medicos = []
    with conexion.cursor() as cursor:
        cursor.execute("""SELECT Medico.codigo_medico, Medico.Nombres, Medico.Apellidos, Medico.Fecha_Naci, Medico.DNI, Medico.Especialidad, Medico.Direccion, Medico.Celular, Medico.Pais, Email, Medico.Pais, Email, Medico.Sexo, Medico.Edad
                    FROM Usuarios INNER JOIN Medico ON Usuarios.Usuario = (%s)""",(user))
        medicos = cursor.fetchall()
    conexion.close()
    return medicos

def obtener_historial():
    conexion = obtener_conexion()
    historials = []
    with conexion.cursor() as cursor:
        cursor.execute("""SELECT id_historial, codigo_medico, codigo_paciente, Fecha, Descripcion, Resultado FROM Historial ORDER BY id_historial ASC""")
        historials = cursor.fetchall()
    conexion.close()
    return historials

