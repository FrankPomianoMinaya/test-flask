#import gspread
#from oauth2client.service_account import ServiceAccountCredentials
#import os
#from dotenv import load_dotenv
#load_dotenv()
#credentials = os.getenv("CREDENTIALS")
# Definir los alcances (scopes) necesarios
#scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
# Autenticarse usando el archivo de credenciales descargado
# creds = ServiceAccountCredentials.from_json_keyfile_name(
#     credentials, scope)
import pyodbc
# client = gspread.authorize(creds)

# Abrir una hoja de cálculo por su nombre
# sheet = client.open("Prueba de CRM").sheet1

# def save_to_google_sheets(nombre, email, mensaje):
#     # Guarda los datos en Google Sheets
#     form_data = [nombre, email, mensaje]
#     sheet.append_row(form_data)

# # Leer los datos de la hoja
# data = sheet.get_all_records()

# # Mostrar los datos obtenidos
# print(data)
#data = request.json
nombre = "Juan"
email = "temp@gmail.com"
mensaje = "Esto es una prueba"

# Configura la conexión
server = r'DESKTOP-44IC9KG\MSSQLSERVER_1'
database = 'test'
username = 'user_test'
password = 'user_777'

conn_str = (
    f'DRIVER={{ODBC Driver 17 for SQL Server}};'
    f'SERVER={server};'
    f'DATABASE={database};'
    f'UID={username};'
    f'PWD={password}'
)

# Conexión
conn = pyodbc.connect(conn_str)
cursor = conn.cursor()
cursor.execute("SELECT * FROM tabla_test")

row = cursor.fetchone()

print(row)

cursor.close()

# Guardar los datos en Google Sheets
#save_to_google_sheets(nombre, email, mensaje)

