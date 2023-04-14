# Importar las bibliotecas necesarias
from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive
import io

# Autenticar las credenciales
gauth = GoogleAuth()

# Autenticar en una ventana del navegador
gauth.LocalWebserverAuth() 


directorio_credenciales = './conexion/credentials_module.json'

# INICIAR SESION
def login():
    GoogleAuth.DEFAULT_SETTINGS['client_config_file'] = directorio_credenciales
    gauth = GoogleAuth()
    gauth.LoadCredentialsFile(directorio_credenciales)
    
    if gauth.credentials is None:
        gauth.LocalWebserverAuth(port_numbers=[8092])
    elif gauth.access_token_expired:
        gauth.Refresh()
    else:
        gauth.Authorize()
        
    gauth.SaveCredentialsFile(directorio_credenciales)
    credenciales = GoogleDrive(gauth)
    return credenciales

def download_imagine_for_id(id_drive,ruta_descarga):
    credenciales = login()
    archivo = credenciales.CreateFile({'id': id_drive}) 
    nombre_archivo = archivo['title']
    archivo.GetContentFile(ruta_descarga + nombre_archivo)

if __name__ == "__main__":
    download_imagine_for_id('1TIwsxZr04XmOU9T5Io8FgCYIsxyl-YZd', './imagen/')