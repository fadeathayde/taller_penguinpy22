from flask import Flask, escape, request, render_template, url_for  #importar la libreria

app = Flask (__name__) #inicializamos la app con el nombre

@app.route('/') #definimos que en la ruta de inicio será aplicada la función hola
def hola():
    return 'Hi Penguins!'

@app.route('/coach')
def hola_coaches():
    nombre = 'Fabrizzio'
    devolver = request.args.get('nombre', nombre)
    return f'Hola, {escape(devolver)} '

@app.route('/inicio') #creamos la ruta de inicio
def inicio():
    return render_template('inicio.html')

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

app.run(debug=True) # para ejecutar