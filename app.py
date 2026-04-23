import pandas as pd
import kagglehub
from kagglehub import KaggleDatasetAdapter
from flask import Flask, render_template

app = Flask(__name__)

# Ajusta esta ruta local si ya descargaste el archivo CSV en tu equipo.
# Si la dejas vacía, kagglehub intentará cargar el dataset desde la fuente.
file_path = ""


def cargar_dataset():
    try:
        df = kagglehub.load_dataset(
            KaggleDatasetAdapter.PANDAS,
            "algozee/teenager-menthal-healy",
            file_path,
            # pandas_kwargs={"low_memory": False}  # Ajusta si tu CSV es muy grande
        )

        return df, None

    except Exception as e:
        return None, str(e)


@app.route("/analisis")
def analisis():
    df, error = cargar_dataset()

    if error:
        return render_template("analisis.html", error=error)

    preview = df.head(8)

    return render_template(
        "analisis.html",
        error=None,
        columnas=preview.columns.tolist(),
        filas=preview.fillna("").values.tolist(),
        total_registros=len(df),
        total_columnas=len(df.columns)
    )
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

@app.route('/kpis')
def kpis():
    return render_template('kpis.html')

@app.route('/modelo')
def modelo():
    return render_template('modelo.html')

if __name__ == '__main__':
    app.run(debug=True)