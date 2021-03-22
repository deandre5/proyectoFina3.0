from flask import Flask, jsonify, request, Response
from flask_cors import CORS
import jwt



from app.controllers.tablaIngresosControllers import tablaIngreso
from app.controllers.registroPersonasControllers import RegistroPersonas
from app.controllers.ingresoSitemaControllers import Ingresosistema

from app.validators.ingresoValidator import CreateUserSchema, CreateUserFuncionarioSchema


userSchema = CreateUserSchema()
funcionarioSchema = CreateUserFuncionarioSchema()
ingresoSistema = Ingresosistema()

from app.config.config import KEY_TOKEN_AUTH


registroPersonas = RegistroPersonas()
tablaIngresos = tablaIngreso()


app = Flask(__name__)

CORS(app)

def validarToken(headers):
    token = headers.split(' ')

    try:
        # se devulve la informacion util del usuario
        data = jwt.decode(token[1], KEY_TOKEN_AUTH, algorithms=['HS256'])
        status = True
        print(data)
        return data
    except:
        status = False
        return status

@app.route('/tablaingresos', methods=['GET'])
def tablaingresos():
    if (request.headers.get('Authorization')):
        token = request.headers.get('Authorization')

        validate = validarToken(token)

        if validate:
            if validate.get('user') == "admin":
                result = tablaIngresos.datosIngreso()

                if result:
                    return jsonify({"status": "registrado", "consultaUser": result}), 200

                else:
                    return jsonify({"status": "no hay usuarios registrados"}),400

            else:
                return jsonify({'status': 'error', "message": "No tiene permisos para entrar a esta pagina"}), 406
        else:
            return jsonify({'status': 'error', "message": "Token invalido"})
    else:
        return jsonify({'status': 'No ha envido ningun token'})



@app.route('/registrarusuario', methods=['POST'])
def registrar():
    if (request.headers.get('Authorization')):
        token = request.headers.get('Authorization')

        validar = validarToken(token)

        if (validar):
            if (validar.get('user') == 'admin'):

                try:

                    content = request.get_json()
                    tipopersona = content.get("tipopersona")
                    if tipopersona == "Aprendiz":
                        userSchema.load(content)
                    elif tipopersona == "Funcionario":
                        funcionarioSchema.load(content)

                    consulta = registroPersonas.consultar(content)

                    if (consulta):
                        return jsonify({"status": "BAD", "message": 'El correo o el documento ya estan registrados'}), 200

                    else:

                        registro = registroPersonas.registrar(content)

                        if (registro):

                            return jsonify({"status": "OK"}), 200
                        else:
                            return jsonify({"status": str(registro)}), 500

                except Exception as error:
                    Errorjson = str(error)
                    return jsonify({"error": Errorjson})

            else:
                return jsonify({'status': 'error', "message": "No tiene permisos para entrar a esta pagina"}), 406
        else:
            return jsonify({'status': 'error', "message": "Token invalido"}),400
    else:
        return jsonify({'status': 'No ha envido ningun token'}),400


        
@app.route('/ingresosistema/<int:documento>', methods=['POST'])
def ingresosistema(documento):
    if (request.headers.get('Authorization')):
        token = request.headers.get('Authorization')

        validar = validarToken(token)

        if (validar):

            documento = str(documento)

            result = ingresoSistema.ingresarSitemas(documento)

            if (result == 0):
                return jsonify({"status": "No existe el usuario"}),400
            
            if (result):
                return jsonify({"status": "OK"})
            
            else:
                return jsonify({"status": "Error"})

        else:
            return jsonify({'status': 'error', "message": "Token invalido"}),400
    else:
        return jsonify({'status': 'No ha envido ningun token'}),400



@app.route('/salidaGym/<int:documento>', methods=['POST'])
def salidaGym(documento):
    if (request.headers.get('Authorization')):
        token = request.headers.get('Authorization')

        validar = validarToken(token)

        if (validar):

            documento = str(documento)
            result = ingresoSistema.salir(documento)

            if (result == 0):
                return jsonify({"status": "No ha ingresado al sistema hoy"}),400

            if (result):
                return jsonify({"status": "OK"}),200
            else:
                return jsonify({"status": "Error"}),400

        else:
            return jsonify({'status': 'error', "message": "Token invalido"}),400
    else:
        return jsonify({'status': 'No ha envido ningun token'}),400


