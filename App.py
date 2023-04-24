from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_mysqldb import MySQL
from config import config
from PIL import Image
from io import BytesIO
from datetime import datetime
import os
# Models
import random
from models.modelUser import ModelUser
import controlador_pneumonia
# Entities
from models.entities.User import  User
from models.entities.Paciente import  Paciente
from datetime import datetime
now = datetime.now()
#Modelo Entrenado
import Algoritmo.detection

app = Flask(__name__)
db=MySQL(app)


@app.route('/')
def Index():
    return render_template('index.html')

@app.route('/inicio')
def incio():
    if 'user' in session:
        medicos = controlador_pneumonia.obtener_medico(session["user"])
        return render_template('Inicio.html', medicos=medicos)
    else:
        return "Acceso Denegado"
        

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        usu = request.form.get("usuario")
        user = User(0,0,request.form['usuario'],request.form['clave'],0)
        logged_user = ModelUser.login(db,user)
        session["user"] = usu
        if logged_user != None:
            if logged_user.clave:
                return render_template('inicio.html')
            else:
                flash("Contraseña invalida!")
                #return render_template('index.html')
                return 'Datos invalidos!'
        else:
            flash("Usuario no encontrado...")
            #return render_template('index.html')
            return 'Datos no encontrados!'
    else:
        return 'No hay datos'    
    
@app.route('/paciente', methods=['GET','POST'])
def add_paciente():
    if request.method == 'POST':
        codigo_paciente = random.randint(0, 999999)
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        fecha = request.form['fecha']
        edad = request.form['edad']
        DNI = request.form['DNI']
        celular  = request.form['celular']
        pais = request.form['pais']
        ciudad = request.form['ciudad']
        sexo = request.form['sexo']
        direccion = request.form['direccion']
        email = request.form['email']
        controlador_pneumonia.agregar_paciente(codigo_paciente, nombre,apellido,fecha,edad,DNI,sexo,pais,ciudad,direccion,celular,email)
        return redirect("/pacientes")
    
@app.route('/clasificar', methods=['GET','POST'])
def clasificacion():
    if request.method == 'POST':
        codigo_paciente = request.form['codigo_paciente']
        codigo_medico = request.form['codigo_medico']
        now = datetime.now()
        fecha = now
        descripcion = request.form['descripcion']
        imag = request.files['url']
        ruta_archivo = os.path.join('C:\\xampp\\htdocs\\Pneumonia-app\\src\\Algoritmo\\chest_xray\\test\\test\\' + imag.filename)
        #imag.save(ruta_archivo)
        resultado = Algoritmo.detection.Clasificar(ruta_archivo)
        controlador_pneumonia.agregar_historial(codigo_medico, codigo_paciente,fecha,descripcion, resultado)
        return render_template('diagnostico.html')
    
@app.route("/diagnosticos")
def diagnosticos():
    if 'user' in session:
        pacientes = controlador_pneumonia.obtener_paciente()
        medicos = controlador_pneumonia.obtener_medico(session["user"])
        return render_template('diagnostico.html', pacientes=pacientes,medicos=medicos)
    else:
        return "Acceso Denegado"

@app.route("/pacientes")
def pacientes():
    if 'user' in session:
        pacientes = controlador_pneumonia.obtener_paciente()
        medicos = controlador_pneumonia.obtener_medico(session["user"])
        return render_template('paciente.html', pacientes=pacientes,medicos=medicos)
    else:
        return "Acceso Denegado"
    
@app.route("/historial")
def historial():
    if 'user' in session:
        historials = controlador_pneumonia.obtener_historial()
        #medicos = controlador_pneumonia.obtener_historial_p(session["user"])
        return render_template('historial.html', historials=historials)
    else:
        return "Acceso Denegado"

if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.run()