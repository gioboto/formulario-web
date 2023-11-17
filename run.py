from flask import Flask, render_template, request
from datetime import datetime, timedelta

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def formulario_fecha():
    if request.method == 'POST':
        try:
            fecha_ingresada = request.form['fecha']
            nombre_ingresado = request.form['nombre']
            fecha_obj = datetime.strptime(fecha_ingresada, '%Y-%m-%d')
            fecha_sumada = fecha_obj + timedelta(days=60)  # Suma dos meses (aproximadamente)
            nombre_egresado = nombre_ingresado
            return render_template('resultado.html', fecha_sumada=fecha_sumada, nombre_egresado=nombre_egresado)
        except ValueError:
            return render_template('error.html', mensaje='Formato de fecha incorrecto. Utiliza el formato YYYY-MM-DD.')
    return render_template('formulario.html')

# Manejo de error 404 (página no encontrada)
@app.errorhandler(404)
def pagina_no_encontrada(e):
    return render_template('error.html', mensaje='Página no encontrada'), 404

if __name__ == '__main__':
    app.run(debug=True, port=8080)

