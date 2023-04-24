import pymysql

def obtener_conexion():
    return pymysql.connect(host='mysql-app-diagnostic.alwaysdata.net',
                                user='287787',
                                password='tomascito97A',
                                db='app-diagnostic_pneumonia')
    
