# Importar las bibliotecas necesarias
from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive
import io
#from PIL import Image

# Autenticar las credenciales
gauth = GoogleAuth()

# Autenticar en una ventana del navegador
gauth.LocalWebserverAuth() 


directorio_credenciales = 'credentials_module.json'

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


def read_imagine_for_id(id_drive,ruta_descarga):
    credenciales = login()
    archivo = credenciales.CreateFile({'id': id_drive}) 
    nombre_archivo = archivo['title']
    archivo.GetContentFile(ruta_descarga + nombre_archivo)

if __name__ == "__main__":
    ruta_archivo = '/home/falv/Escritorio/fondo.jpg'
    id_folder = '0AI_9cD6f9EEZUk9PVA'
    id_drive = '1LVdc-DUwr30kfrA30cVO3K92RVh56pmw'
    ruta_descarga = '/home/falv/Descargas/'    

# Leer la imagen
#content = file.GetContentString()
#image = Image.open(io.BytesIO(content))

'''
# Acceder al archivo de imagen en Google Drive
file_id = 'tu_id_de_archivo' # Reemplazar con la ID de tu archivo de imagen
drive = GoogleDrive(gauth)
file = drive.CreateFile({'id': file_id})

'''


'''
Este código utiliza la biblioteca Pillow (PIL) para leer la imagen desde un objeto de bytes y 
devuelve la imagen como un objeto de imagen.
También puedes utilizar la ruta de acceso a tu archivo de imagen en Google Drive en lugar de la ID 
de archivo en el siguiente código:


# Acceder al archivo de imagen en Google Drive por la ruta de acceso
file_path = '/ruta/de/archivo/imagen.png' # Reemplazar con la ruta de acceso de tu archivo de imagen
file = drive.CreateFile({'title': file_path.split('/')[-1]})
file_path_ids = [x['id'] for x in drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()]
for fid in file_path_ids:
    f = drive.CreateFile({'id': fid})
    if f['title'] == file_path.split('/')[-1]:
        file = f
        break

# Leer la imagen
content = file.GetContentString()
image = Image.open(io.BytesIO(content))

'''