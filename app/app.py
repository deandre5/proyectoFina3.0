from app.config.config import KEY_TOKEN_AUTH
from flask import Flask, jsonify, request, Response
from flask_cors import CORS
import jwt


from app.controllers.tablaIngresosControllers import tablaIngreso
from app.controllers.registroPersonasControllers import RegistroPersonas
from app.controllers.ingresoSitemaControllers import Ingresosistema
from app.controllers.consultaUsuariosControllers import ConsultaUsuarios
from app.controllers.actualizarPersonaControllers import ActualizacionPersona
from app.controllers.perfilControllers import Perfil
from app.controllers.eliminarUsuarioControllers import eliminarUsuario
from app.controllers.consultarRutinasControllers import ConsultarRutinas
from app.controllers.enviarCorreoControllers import EnvioCorreos

from app.validators.ingresoValidator import CreateUserSchema, CreateUserFuncionarioSchema, ChangePasswordSchema
from app.validators.actualizarValidator import actualizarUserSchema, actualizarUserSinFotoSchema


userSchema = CreateUserSchema()
funcionarioSchema = CreateUserFuncionarioSchema()
actualizarUser = actualizarUserSchema()
actualizarSinFoto = actualizarUserSinFotoSchema()
changePassword = ChangePasswordSchema()


ingresoSistema = Ingresosistema()
actualizarPersona = ActualizacionPersona()
consultaPerfil = Perfil()
eliminacionUsuario = eliminarUsuario()
consultaRutina = ConsultarRutinas()
envioCorreos = EnvioCorreos()


registroPersonas = RegistroPersonas()
tablaIngresos = tablaIngreso()
consultarUsuarios = ConsultaUsuarios()


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
                    return jsonify({"status": "no hay usuarios registrados"}), 400

            else:
                return jsonify({'status': 'error', "message": "No tiene permisos para entrar a esta pagina"}), 406
        else:
            return jsonify({'status': 'error', "message": "Token invalido"}), 406
    else:
        return jsonify({'status': 'No ha envido ningun token'}), 406


@app.route('/registrarusuario', methods=['POST'])
def registrar():
    if (request.headers.get('Authorization')):
        token = request.headers.get('Authorization')

        validar = validarToken(token)

        if (validar):
            if (validar.get('user') == 'admin'):

                try:

                    content = request.get_json()
                    tipouser = content.get("tipouser")
                    if tipouser == "Aprendiz":
                        userSchema.load(content)
                    elif tipouser == "Funcionario":
                        funcionarioSchema.load(content)

                    consulta = registroPersonas.consultar(content)

                    if (consulta):
                        return jsonify({"status": "BAD", "message": 'El correo o el documento ya estan registrados'}), 400

                    else:

                        registro = registroPersonas.registrar(content)

                        if (registro):

                            return jsonify({"status": "OK"}), 200
                        else:
                            return jsonify({"status": str(registro)}), 500

                except Exception as error:
                    Errorjson = str(error)
                    return jsonify({"error": Errorjson}), 500

            else:
                return jsonify({'status': 'error', "message": "No tiene permisos para entrar a esta pagina"}), 406
        else:
            return jsonify({'status': 'error', "message": "Token invalido"}), 400
    else:
        return jsonify({'status': 'No ha envido ningun token'}), 400


@app.route('/ingresosistema/<int:documento>', methods=['POST'])
def ingresosistema(documento):
    if (request.headers.get('Authorization')):
        token = request.headers.get('Authorization')

        validar = validarToken(token)

        if (validar):
            if (validar.get('user') == 'admin'):

                documento = str(documento)

                result = ingresoSistema.ingresarSitemas(documento)

                if (result == 0):
                    return jsonify({"status": "No existe el usuario"}), 400

                if (result):
                    return jsonify({"status": "OK"}), 200

                else:
                    return jsonify({"status": "Error"}), 500
            else:
                return jsonify({'status': 'error', "message": "No tiene permisos para entrar a esta pagina"}), 406

        else:
            return jsonify({'status': 'error', "message": "Token invalido"}), 400
    else:
        return jsonify({'status': 'No ha envido ningun token'}), 400


@app.route('/salidaGym/<int:documento>', methods=['PUT'])
def salidaGym(documento):
    if (request.headers.get('Authorization')):
        token = request.headers.get('Authorization')

        validar = validarToken(token)

        if (validar):
            if (validar.get('user') == 'admin'):

                documento = str(documento)
                result = ingresoSistema.salir(documento)

                if (result == 0):
                    return jsonify({"status": "No ha ingresado al sistema hoy"}), 400

                if (result):
                    return jsonify({"status": "OK"}), 200
                else:
                    return jsonify({"status": "Error"}), 400

            else:
                return jsonify({'status': 'error', "message": "No tiene permisos para entrar a esta pagina"}), 406

        else:
            return jsonify({'status': 'error', "message": "Token invalido"}), 400
    else:
        return jsonify({'status': 'No ha envido ningun token'}), 400


@app.route('/consultaUsuarios', methods=['GET'])
def consultaUsuarios():
    if (request.headers.get('Authorization')):
        token = request.headers.get('Authorization')

        validar = validarToken(token)

        if (validar):
            if (validar.get('user') == 'admin'):

                consulta = consultarUsuarios.consultarGeneral()

                if (consulta):
                    return jsonify({"status": "OK", "consulta": consulta}), 200

                else:
                    return jsonify({"status": "No hay usuarios registrados"}), 400

            else:
                return jsonify({'status': 'error', "message": "No tiene permisos para entrar a esta pagina"}), 406

        else:
            return jsonify({'status': 'error', "message": "Token invalido"}), 400
    else:
        return jsonify({'status': 'No ha envido ningun token'}), 400


@app.route('/consultaUsuarios/<int:documento>', methods=['GET'])
def consultaUsuariosID(documento):
    if (request.headers.get('Authorization')):
        token = request.headers.get('Authorization')

        validar = validarToken(token)

        if (validar):
            if (validar.get('user') == 'admin'):

                documento = str(documento)

                consulta = consultarUsuarios.consultarID(documento)

                if (consulta):
                    return jsonify({"status": "OK", "consulta": consulta}), 200

                else:
                    return jsonify({"status": "No hay usuarios registrados"}), 400

            else:
                return jsonify({'status': 'error', "message": "No tiene permisos para entrar a esta pagina"}), 406

        else:
            return jsonify({'status': 'error', "message": "Token invalido"}), 400
    else:
        return jsonify({'status': 'No ha envido ningun token'}), 400


@app.route('/actualizar', methods=['PUT'])
def actualizar():
    if (request.headers.get('Authorization')):
        token = request.headers.get('Authorization')

        validar = validarToken(token)

        if (validar):

            try:
                content = request.form

                documento = validar.get('documento')

                if len(request.files) > 0:
                    validacion = actualizarUser.load(content)
                    file = request.files['imagen']

                    actualizar = actualizarPersona.actualizarFoto(
                        documento, content, file)

                    if actualizar == 0:

                        return jsonify({"status": "error, ingrese un archivo valido"}), 400

                    if actualizar == 1:

                        return jsonify({"status": "error, el correo ya esta registrado"}), 400

                    if actualizar:
                        return jsonify({"status": "OK", "imagen": actualizar}), 200
                    else:
                        return jsonify({"status": "Error, no existe la persona a actualizar"}), 400

                else:
                    validacion = actualizarSinFoto.load(content)
                    actualizar = actualizarPersona.actualizar(
                        documento, content)

                    if isinstance(actualizar, str):
                        return jsonify({"status": "error, el correo ya esta registrado"}), 400

                    if (actualizar):
                        return jsonify({"status": "OK", "imagen": actualizar}), 200
                    else:
                        return jsonify({"status": "Error, no existe la persona a actualizar", }), 400
            except Exception as error:
                tojson = str(error)
                print(tojson)
                return jsonify({"status": "no es posible validar", "error": tojson}), 406

        else:
            return jsonify({'status': 'error', "message": "Token invalido"}), 400
    else:
        return jsonify({'status': 'No ha envido ningun token'}), 400


@app.route('/actualizar/<int:documento>', methods=['PUT'])
def actualizarID(documento):
    if (request.headers.get('Authorization')):
        token = request.headers.get('Authorization')

        validar = validarToken(token)

        if (validar):

            try:
                content = request.form

                documento = str(documento)

                if len(request.files) > 0:
                    validacion = actualizarUser.load(content)
                    file = request.files['imagen']

                    actualizar = actualizarPersona.actualizarFoto(
                        documento, content, file)

                    if actualizar == 0:

                        return jsonify({"status": "error, ingrese un archivo valido"}), 400

                    if actualizar == 1:

                        return jsonify({"status": "error, el correo ya esta registrado"}), 400

                    if actualizar:
                        return jsonify({"status": "OK"}), 200
                    else:
                        return jsonify({"status": "Error, no existe la persona a actualizar"}), 400

                else:
                    validacion = actualizarSinFoto.load(content)
                    actualizar = actualizarPersona.actualizar(
                        documento, content)

                    if isinstance(actualizar, str):
                        return jsonify({"status": "error, el correo ya esta registrado"}), 400

                    if (actualizar):
                        return jsonify({"status": "OK"}), 200
                    else:
                        return jsonify({"status": "Error, no existe la persona a actualizar", }), 400
            except Exception as error:
                tojson = str(error)
                print(tojson)
                return jsonify({"status": "no es posible validar", "error": tojson}), 406

        else:
            return jsonify({'status': 'error', "message": "Token invalido"}), 400
    else:
        return jsonify({'status': 'No ha envido ningun token'}), 400


@app.route('/perfil', methods=['GET'])
def perfil():
    if (request.headers.get('Authorization')):
        token = request.headers.get('Authorization')

        validar = validarToken(token)

        if (validar):

            try:

                documento = validar.get('documento')

                consulta = consultaPerfil.consultarPerfil(documento)

                if(consulta):
                    return jsonify({"status": "OK", "consulta": consulta}), 200

            except Exception as error:
                tojson = str(error)
                print(tojson)
                return jsonify({"status": "no es posible validar", "error": tojson}), 406

        else:
            return jsonify({'status': 'error', "message": "Token invalido"}), 400
    else:
        return jsonify({'status': 'No ha envido ningun token'}), 400


@app.route('/programas', methods=['GET'])
def programas():
    if (request.headers.get('Authorization')):
        token = request.headers.get('Authorization')

        validar = validarToken(token)

        if (validar):
            if (validar.get('user') == 'admin'):

                consulta = consultarUsuarios.programas()

                if (consulta):
                    return jsonify({"status": "OK", "consulta": consulta}), 200

                else:
                    return jsonify({"status": "No hay programas registrados"}), 400

            else:
                return jsonify({'status': 'error', "message": "No tiene permisos para entrar a esta pagina"}), 406
        else:
            return jsonify({'status': 'error', "message": "Token invalido"}), 400
    else:
        return jsonify({'status': 'No ha envido ningun token'}), 400


@app.route('/cambiarPassword', methods=['PUT'])
def cambiarPassword():
    if (request.headers.get('Authorization')):
        token = request.headers.get('Authorization')

        validar = validarToken(token)

        if (validar):

            try:

                correo = validar.get('correo')
                content = request.get_json()

                validator = changePassword.load(content)




                actualizarPassword = actualizarPersona.actualizarPassword(
                    correo, content)

                if (actualizarPassword):
                    print(actualizarPassword)

                    return jsonify({"status": "OK"}), 200
                else:
                    return jsonify({"status": str(actualizarPassword)}), 500
            
            except Exception as error:
                toString = str(error)
                return jsonify({"status": "No es posible validar", "Error": toString})

        else:
            return jsonify({'status': 'error', "message": "Token invalido"}), 400
    else:
        return jsonify({'status': 'No ha envido ningun token'}), 400


@app.route('/elimnarUsuario/<int:documento>', methods=['DELETE'])
def elimnarUsuario(documento):
    if (request.headers.get('Authorization')):
        token = request.headers.get('Authorization')

        validar = validarToken(token)

        if (validar):
            if (validar.get('user') == 'admin'):

                documento = str(documento)

                eliminar = eliminarUsuario.eliminar(documento)

                if (eliminar):
                    return jsonify({"status": "OK"}), 200

                else:
                    return jsonify({"status": "No existe el usuario"}), 400

            else:
                return jsonify({'status': 'error', "message": "No tiene permisos para entrar a esta pagina"}), 406
        else:
            return jsonify({'status': 'error', "message": "Token invalido"}), 400
    else:
        return jsonify({'status': 'No ha envido ningun token'}), 400


@app.route('/consultarRutina', methods=['GET'])
def consultarRutinaAsignada():
    if (request.headers.get('Authorization')):
        token = request.headers.get('Authorization')

        validar = validarToken(token)

        if (validar):

            id = validar.get('rutina')

            retorno = consultaRutina.consultar(id)

            if retorno:
                return jsonify({'status': 'ok', 'ejercicios': retorno}), 200
            else:
                return jsonify({'status': 'error'}), 400

        else:
            return jsonify({'status': 'error', "message": "Token invalido"}), 400
    else:
        return jsonify({'status': 'No ha envido ningun token'}), 400


@app.route('/reporteUsuarios', methods=['GET'])
def reporteUsuarios():
    if (request.headers.get('Authorization')):
        token = request.headers.get('Authorization')

        validar = validarToken(token)

        if (validar):
            if (validar.get('user') == 'admin'):

                try:
                    reporte = consultarUsuarios.reporteUsuarios()
                    return Response(reporte, mimetype="application/ms-excel", headers={"content-Disposition": "attachment; filename=reporteUsuarios.csv"}), 200

                except Exception as error:
                    Errorjson = str(error)
                    print(error)
                    return jsonify({"error": Errorjson}), 500

            else:
                return jsonify({'status': 'error', "message": "No tiene permisos para entrar a esta pagina"}), 406
        else:
            return jsonify({'status': 'error', "message": "Token invalido"}), 400
    else:
        return jsonify({'status': 'No ha envido ningun token'}), 400


@app.route('/reporteIngreso', methods=['GET'])
def reporteIngreso():
    if (request.headers.get('Authorization')):
        token = request.headers.get('Authorization')

        validar = validarToken(token)

        if (validar):
            if (validar.get('user') == 'admin'):

                try:
                    reporte = tablaIngresos.reporteIngreso()
                    return Response(reporte, mimetype="application/ms-excel", headers={"content-Disposition": "attachment; filename=reporteUsuarios.csv"}), 200

                except Exception as error:
                    Errorjson = str(error)
                    print(error)
                    return jsonify({"error": Errorjson}), 500

            else:
                return jsonify({'status': 'error', "message": "No tiene permisos para entrar a esta pagina"}), 406
        else:
            return jsonify({'status': 'error', "message": "Token invalido"}), 400
    else:
        return jsonify({'status': 'No ha envido ningun token'}), 400


@app.route('/enviarCorreo', methods=['POST'])
def enviarCorreo():
    if (request.headers.get('Authorization')):
        token = request.headers.get('Authorization')

        validar = validarToken(token)

        if (validar):

            try:

                content = request.get_json()

                correo = validar.get('correo')

                correo = envioCorreos.enviarCorreos(content, correo)

                if (correo):
                    return jsonify({'status': "ok"}), 200

                else:
                    return jsonify({'status': "bad", "error": correo}), 400
            except Exception as error:
                error = str(error)
                return jsonify({'error', error}), 500

        else:
            return jsonify({'status': 'error', "message": "Token invalido"}), 400
    else:
        return jsonify({'status': 'No ha envido ningun token'}), 400
