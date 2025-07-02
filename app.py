from flask import Flask, request, jsonify
#import gspread
#from oauth2client.service_account import ServiceAccountCredentials
#import os
#from dotenv import load_dotenv
#load_dotenv()
#credentials = os.getenv("CREDENTIALS")

app = Flask(__name__)

# Definir los alcances (scopes) necesarios
#scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

# Autenticarse usando el archivo de credenciales descargado
#creds = ServiceAccountCredentials.from_json_keyfile_name(
#    credentials, scope)

#client = gspread.authorize(creds)

# Abrir una hoja de cálculo por su nombre
#sheet = client.open("Prueba de CRM").sheet1

@app.route('/')
def index():
    return 'Hello from Flask!'


@app.route('/test')
def test():
    return 'This is a test route.'

@app.route('/webhook', methods=['POST'])
def form_submission():
    data = request.form  # Recibe los datos del formulario como 'form data'
    print(data)
    nombre = data.get('Nombres y Apellidos')
    telefono = data.get('Teléfono / Celular')
    email = data.get('Correo Electrónico')
    mensaje = data.get('Mensaje')

    # Guardar los datos en Google Sheets
    #save_to_google_sheets(nombre,telefono, email, mensaje)

    return jsonify({"message": "Formulario recibido con éxito"}), 200

#def save_to_google_sheets(nombre,telefono, email, mensaje):
#    # Guarda los datos en Google Sheets
#    form_data = [nombre,telefono, email, mensaje]
#    sheet.append_row(form_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

