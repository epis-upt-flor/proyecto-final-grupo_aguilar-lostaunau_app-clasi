import tensorflow as tf
import numpy as np
from tensorflow import keras
from tensorflow.python.keras import layers
from tensorflow.python.keras.models import load_model
from tensorflow.python.keras.layers import Dense
import matplotlib.pyplot as plt
import joblib
from io import BytesIO
from PIL import Image

def Clasificar(ruta_archivo):
    try:
        # Cargamos el modelo
        model = keras.models.load_model('C:\\xampp\\htdocs\\Pneumonia-app\\src\\Algoritmo\\modelo_entrenado\\modelo_deteccion2.h5')
        # carga una imagen nueva para probar el modelo
        ruta_test1 = 'C:\\xampp\\htdocs\\Pneumonia-app\\src\\Algoritmo\\chest_xray\\test\\PNEUMONIA\\person1623_virus_2813.jpeg'
        ruta_test2 = 'C:\\xampp\\htdocs\\Pneumonia-app\\src\\Algoritmo\\chest_xray\\test\\NORMAL\\NORMAL2-IM-0323-0001.jpeg'
        img = keras.preprocessing.image.load_img(
            ruta_archivo, target_size=(224, 224)
        )
        img_array = keras.preprocessing.image.img_to_array(img)
        img_array = tf.expand_dims(img_array, 0)

        # realiza la predicción con el modelo
        predictions = model.predict(img_array)
        score = predictions[0]
        # muestra el resultado de la predicción
        if score > 0.5:
            return "1"
        else:
            return "0"
        #return respuesta
        # # Llamamos el history
        # history_cargado = joblib.load('C:\\xampp\\htdocs\\Pneumonia-app\\src\\Algoritmo\\historia\\history.joblib')
        # print(history_cargado)
        # # grafica la precisión del modelo
        # plt.plot(history_cargado['accuracy'])
        # plt.plot(history_cargado['val_accuracy'])
        # plt.title('Precisión del modelo')
        # plt.ylabel('Precisión')
        # plt.xlabel('Época')
        # plt.legend(['Entrenamiento', 'Validación'], loc='upper left')
        # plt.show()
    except Exception as ex:
        raise Exception(ex)