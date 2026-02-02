from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "live_gjCtdSDme4taUqyq0brU5LY3MrJ0Ocmmg8fXfgYYDLqxNXnNsVyf4DkjsVDXmTta" 

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/buscar')
def buscar():
    return render_template('buscar.html')

@app.route('/resultado', methods=['GET'])
def resultado():
    raza = request.args.get("raza")

    if not raza:
        return render_template("resultado.html", perro=None)

    url = "https://api.thedogapi.com/v1/breeds"
    headers = {
        "x-api-key": API_KEY
    }

    respuesta = requests.get(url, headers=headers).json()

    resultado = None

    if isinstance(respuesta, list):
        for perro in respuesta:
            if raza.lower() in perro["name"].lower():
                resultado = perro
                break

    return render_template("resultado.html", perro=resultado)

if __name__ == '__main__':
    app.run(debug=True)
