from flask import Flask, render_template, request
from controlador import controladorIndex

app=Flask(__name__)


@app.route('/')
def index():
    dataResult = {
        "estadoEntero": '',
        "estadoReales":'',
        "estadoNotacion": '',
        "estadoEmail": ''
    }
    return  render_template('index.html', data=dataResult)

@app.route('/validarCadenas', methods=['GET', 'POST'])
def expRegEnteros():
    output = request.form.to_dict()
    numEnteros = output["numerosEnteros"]
    numReales = output["numerosReales"]
    numNotaciones = output["numeroNotacion"]
    cadEmail = output["cadenaEmail"]
    estado = controladorIndex.ValidarEnteros(numEnteros)
    estado2 = controladorIndex.ValidarReales(numReales)
    estado3 = controladorIndex.ValidarNotacionCientifica(numNotaciones)
    estado4 = controladorIndex.ValidarEmail(cadEmail)
    dataResult = {
        "estadoEntero":estado,
        "estadoReales":estado2,
        "estadoNotacion":estado3,
        "estadoEmail":estado4
    }
    return  render_template('index.html', data=dataResult)




@app.route('/validarReales', methods=['GET', 'POST'])
def expRegReales():
    output = request.form.to_dict()
    numReales = output["numerosReales"]
    estado = controladorIndex.ValidarReales(numReales)
    dataResult = {
        "estadoReales":estado
    }
    return  render_template('index.html', data=dataResult)

@app.route('/validarNotacion', methods=['GET', 'POST'])
def expRegNotacion():
    output = request.form.to_dict()
    numNotaciones = output["numeroNotacion"]
    estado = controladorIndex.ValidarNotacion(numNotaciones)
    dataResult = {
        "estadoNotacion":estado
    }
    return  render_template('index.html', data=dataResult)

@app.route('/validarEmail', methods=['GET', 'POST'])
def expRegEmail():
    output = request.form.to_dict()
    cadEmail = output["cadenaEmail"]
    estado = controladorIndex.ValidarEmail(cadEmail)
    dataResult = {
        "estadoEmail":estado
    }
    return  render_template('index.html', data=dataResult)

if __name__ == '__main__':
    app.run(debug=True, port=5000)