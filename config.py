class Config:
    DEBUG = False
    TESTING = False
    SECRET_KEY = 'tu_clave_secreta'  # Reemplaza con una clave segura
    API_TOKEN = 'tu_token_secreto'  # Reemplaza con un token seguro

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    # Configuraciones específicas para producción...
    pass
# Selecciona la configuración según el entorno
FLASK_ENV = 'development'  # Cambia a 'production' según tu entorno
if FLASK_ENV == 'production':
    app_config = ProductionConfig()
else:
    app_config = DevelopmentConfig()
