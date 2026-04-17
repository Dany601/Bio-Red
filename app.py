from flask import Flask, render_template

app = Flask(__name__)

# Ruta principal
@app.route('/')
def home():
    return render_template('index.html')

# Otras rutas del menú (puedes completarlas luego)
@app.route('/proyecto')
def proyecto():
     return render_template('proyecto.html')


@app.route('/dataset')
def dataset():
    return render_template('dataset.html')

@app.route('/analisis')
def analisis():
    return render_template('analisis.html')

@app.route('/kpis')
def kpis():
    return render_template('kpis.html')

@app.route('/modelo')
def modelo():
    return render_template('modelo.html')

if __name__ == '__main__':
    app.run(debug=True)