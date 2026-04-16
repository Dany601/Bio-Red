from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "holi, Word!"


@app.route("/Bio-Red/usuario/<nombre>/<apellido>")
def mostrar_usuario(nombre, apellido):
    return "Hola, {} {} ¿como estas?".format(nombre, apellido)

if __name__ == "__main__":
    app.run(debug=True) 