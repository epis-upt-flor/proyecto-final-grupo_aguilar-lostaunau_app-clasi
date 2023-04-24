from werkzeug.security import check_password_hash, generate_password_hash

class User():
    
    def __init__(self, id , idmedico, usuario, clave, estado, key="") -> None:
        self.id = id
        self.idmedico = idmedico
        self.usuario = usuario
        self.clave = clave
        self.estado = estado
        self.key = key
    
    @classmethod
    def check_password(self, hashed_clave, clave):
        return check_password_hash(hashed_clave, clave)