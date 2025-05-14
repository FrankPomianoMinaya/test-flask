from flask import Flask, request, jsonify
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os
from dotenv import load_dotenv
load_dotenv()
credentials = os.getenv("CREDENTIALS")

app = Flask(__name__)

# Definir los alcances (scopes) necesarios
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

# Autenticarse usando el archivo de credenciales descargado
creds = ServiceAccountCredentials.from_json_keyfile_name(
    credentials, scope)

client = gspread.authorize(creds)

# Abrir una hoja de cálculo por su nombre
sheet = client.open("Prueba de CRM").sheet1

@app.route('/form_submission', methods=['POST'])
def form_submission():
    datos = request.form
    print(datos)
    data = request.form  # Recibe los datos del formulario como 'form data'
    
    nombre = data.get('name')
    telefono = data.get('field_9194d5d')
    email = data.get('email')
    mensaje = data.get('message')

    # Guardar los datos en Google Sheets
    save_to_google_sheets(nombre,telefono, email, mensaje)

    return jsonify({"message": "Formulario recibido con éxito"}), 200

def save_to_google_sheets(nombre,telefono, email, mensaje):
    # Guarda los datos en Google Sheets
    form_data = [nombre,telefono, email, mensaje]
    sheet.append_row(form_data)

if __name__ == '_main_':
    app.run(debug=True)

