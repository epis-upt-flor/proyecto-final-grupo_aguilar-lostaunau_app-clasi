from .entities.User import User

class ModelUser():
    
    @classmethod
    def login(self,db,user):
        try:
            cursor = db.connection.cursor()
            sql = """ SELECT id_usuario, id_medico, Usuario, Clave, Estado, PalabraSecreta FROM Usuarios
            WHERE Usuario = '{}'""".format(user.usuario)
            cursor.execute(sql)
            row = cursor.fetchone()
            if row != None:
                user = User(row[0],row[1],row[2],User.check_password(row[3],user.clave),row[4],row[5])
                return user
            else:
                return None
        except Exception as ex:
            raise Exception(ex)