from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import os

creds = Credentials.from_authorized_user_file('./connection/credentials_module.json')
drive_service = build('drive', 'v3', credentials=creds)

folder_id = '1f1aZ4i1lYsRaW9ID76iHfGztKdmAsg21'
query = "parents='" + folder_id + "' and mimeType='image/jpeg'" # puedes cambiar 'image/jpeg' a cualquier otro tipo de archivo que quieras buscar
results = drive_service.files().list(q=query,fields="nextPageToken, files(id, name)").execute()

for file in results.get('files', []):
    filename = file.get('name')
    file_id = file.get('id')
    download_url = f"https://drive.google.com/uc?id={file_id}"
    if download_url:
        response = drive_service.files().get_media(fileId=file_id).execute()
        with open(os.path.join('./imagen/', filename), "wb") as f:
            f.write(response)

