from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        name = request.form['name']
        age = int(request.form['age'])
        quantity = int(request.form['quantity'])

        precio_por_tarro = 9000
        total_sin_descuento = quantity * precio_por_tarro

        if 18 <= age <= 30:
            descuento = 0.15
        elif age > 30:
            descuento = 0.25
        else:
            descuento = 0.0

        descuento_aplicado = total_sin_descuento * descuento
        total_a_pagar = total_sin_descuento - descuento_aplicado

        return render_template(
            'ejercicio1.html',
            name=name,
            total_sin_descuento=total_sin_descuento,
            descuento_aplicado=descuento_aplicado,
            total_a_pagar=total_a_pagar,
            show_results=True
        )
    else:
        return render_template('ejercicio1.html', show_results=False)

@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    message = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username == 'juan' and password == 'admin':
            message = 'Bienvenido Administrador juan'
        elif username == 'pepe' and password == 'user':
            message = 'Bienvenido Usuario pepe'
        else:
            message = 'Usuario o contraseña incorrectos'

    return render_template('ejercicio2.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)
