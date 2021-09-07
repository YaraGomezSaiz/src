from flask import Flask, render_template

app = Flask (__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template("about.html")


if __name__== '__main__':
    #en produccion si se realiza un cambio hay que reiniciar el servidor para que surja efecto los cambios
    # app.run() 

    #en pruebas se puede poner modo debug para que reinicie solo con cada cambio.
    app.run(debug=True)

