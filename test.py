import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os
from dotenv import load_dotenv
load_dotenv()
credentials = os.getenv("CREDENTIALS")
# Definir los alcances (scopes) necesarios
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

# Autenticarse usando el archivo de credenciales descargado
creds = ServiceAccountCredentials.from_json_keyfile_name(
    credentials, scope)

client = gspread.authorize(creds)

# Abrir una hoja de cálculo por su nombre
sheet = client.open("Prueba de CRM").sheet1

def save_to_google_sheets(nombre, email, mensaje):
    # Guarda los datos en Google Sheets
    form_data = [nombre, email, mensaje]
    sheet.append_row(form_data)

# # Leer los datos de la hoja
# data = sheet.get_all_records()

# # Mostrar los datos obtenidos
# print(data)
#data = request.json
nombre = "Juan"
email = "temp@gmail.com"
mensaje = "Esto es una prueba"

# Guardar los datos en Google Sheets
save_to_google_sheets(nombre, email, mensaje)