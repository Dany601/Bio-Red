import pandas as pd
import kagglehub
from kagglehub import KaggleDatasetAdapter
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/proyecto')
def proyecto():
     return render_template('proyecto.html')

@app.route('/dataset')
def dataset():
    url = "https://raw.githubusercontent.com/Dany601/Bio-Red/refs/heads/main/Teen_Mental_Health_Dataset.csv"

    try:
        df = pd.read_csv(url)

        columnas = df.columns.tolist()
        filas = df.head(50).values.tolist()

        total_registros = len(df)
        total_columnas = len(df.columns)

        return render_template(
            'dataset.html',
            columnas=columnas,
            filas=filas,
            total_registros=total_registros,
            total_columnas=total_columnas,
            error=None
        )

    except Exception as e:
        return render_template(
            'dataset.html',
            columnas=[],
            filas=[],
            total_registros=0,
            total_columnas=0,
            error=f"No se pudo cargar el dataset: {str(e)}"
        )
@app.route('/kpis')
def kpis():
    return render_template('kpis.html')

@app.route('/modelo')
def modelo():
    return render_template('modelo.html')

@app.route('/analisis')
def analisis():
    return render_template('analisis.html')


if __name__ == '__main__':
    app.run(debug=True)