import pandas as pd
import kagglehub
from kagglehub import KaggleDatasetAdapter
from flask import Flask, render_template, request, jsonify

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
def calc_risk(hours, sleep, stress, anxiety, activity):
    score = (
        hours * 0.3 +
        (10 - sleep) * 0.25 +
        stress * 0.2 +
        anxiety * 0.2 +
        (7 - activity) * 0.05
    )

    risk = round((score / 10) * 100)

    return min(risk, 100)


@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    hours = float(data.get('hours', 0))
    sleep = float(data.get('sleep', 1))
    stress = float(data.get('stress', 1))
    anxiety = float(data.get('anxiety', 1))
    activity = float(data.get('activity', 0))

    risk = calc_risk(hours, sleep, stress, anxiety, activity)

    if risk < 35:
        level = "Riesgo bajo"
        message = "El perfil muestra indicadores saludables. Se recomienda mantener buenos hábitos digitales, descanso adecuado y actividad física constante."
        color = "low"
    elif risk < 65:
        level = "Riesgo moderado"
        message = "Riesgo moderado detectado. Se sugiere reducir el tiempo en redes, mejorar la calidad del sueño y monitorear niveles de estrés."
        color = "medium"
    else:
        level = "Riesgo alto"
        message = "Riesgo alto detectado. Se recomienda intervención profesional, acompañamiento familiar y reducción significativa del uso de redes sociales."
        color = "high"

    return jsonify({
        'risk': risk,
        'level': level,
        'message': message,
        'color': color
    })



@app.route('/analisis')
def analisis():
    return render_template('analisis.html')


@app.route('/infoproyecto')
def infoproyecto():
    return render_template('infoproyecto.html')

if __name__ == '__main__':
    app.run(debug=True)