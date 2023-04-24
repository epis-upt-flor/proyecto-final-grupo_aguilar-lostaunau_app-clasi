class Config:
    SECRET_KEY = 'ASDfg31defds'
    
class DevelopmentConfig(Config):
        DEBUG = True
        MYSQL_HOST = 'mysql-app-diagnostic.alwaysdata.net'
        MYSQL_USER = '287787'
        MYSQL_PASSWORD = 'tomascito97A'
        MYSQL_DB = 'app-diagnostic_pneumonia'

config = {'development' : DevelopmentConfig}