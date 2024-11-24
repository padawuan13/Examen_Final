from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    # Página principal con los botones para los ejercicios
    return render_template('index.html')

@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        # Recoger datos del formulario
        name = request.form['name']
        age = int(request.form['age'])
        quantity = int(request.form['quantity'])

        # Calcular el total sin descuento
        precio_por_tarro = 9000
        total_sin_descuento = quantity * precio_por_tarro

        # Determinar el descuento según la edad
        if 18 <= age <= 30:
            descuento = 0.15  # 15%
        elif age > 30:
            descuento = 0.25  # 25%
        else:
            descuento = 0.0   # Sin descuento para menores de 18

        # Calcular el descuento y el total a pagar
        descuento_aplicado = total_sin_descuento * descuento
        total_a_pagar = total_sin_descuento - descuento_aplicado

        # Renderizar la misma plantilla con los resultados
        return render_template(
            'ejercicio1.html',
            name=name,
            total_sin_descuento=total_sin_descuento,
            descuento_aplicado=descuento_aplicado,
            total_a_pagar=total_a_pagar,
            show_results=True
        )
    else:
        # Renderizar el formulario sin resultados
        return render_template('ejercicio1.html', show_results=False)

# Ruta para el Ejercicio 2
@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    message = None  # Inicializa el mensaje como None
    if request.method == 'POST':
        # Obtén los valores enviados desde el formulario
        username = request.form['username']
        password = request.form['password']

        # Verifica las credenciales
        if username == 'juan' and password == 'admin':
            message = 'Bienvenido Administrador juan'
        elif username == 'pepe' and password == 'user':
            message = 'Bienvenido Usuario pepe'
        else:
            message = 'Usuario o contraseña incorrectos'

    # Renderiza la página con el mensaje correspondiente
    return render_template('ejercicio2.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)
