from app.model.personas import Ingresosistema
from werkzeug.utils import secure_filename
import cloudinary
import cloudinary.uploader
import cloudinary.api
import datetime
import bcrypt
from app.helpers.helpers import allowed_file

personas = Ingresosistema()


cloudinary.config(
    cloud_name='hdjsownnk',
    api_key='926599253344788',
    api_secret='I8rBOy-rnozmrxhNL_Lg7hqtj7s'
)


class ActualizacionPersona():
    def actualizarFoto(self, documento, content, file):

        consulta = personas.ConsultaId(documento)

        if (len(consulta) < 1):
            return False

        correo = content['correo']

        verificarCorreo = personas.VerificarCorreo(correo)

        if (verificarCorreo):
            status = int(1)
            return status

        if allowed_file(file.filename):

            nombres = content['nombres']
            apellidos = content['apellidos']
            telefono = content['telefono']
            edad = content['edad']

            filename = secure_filename(file.filename)

            dia = datetime.datetime.utcnow()
            salt = bcrypt.gensalt()
            hash = bcrypt.hashpw(bytes(str(dia), encoding='utf-8'), salt)

            h = str(hash).split('/')

            if (len(h) > 2):
                t = h[1]+h[2]
            else:
                t = h[0]

            filename = h[0]

            filename = str(t)

            cloudinary.uploader.upload(file, public_id=filename)
            url = cloudinary.utils.cloudinary_url(filename)

            actualizar = personas.actualizarPersona(
                documento, correo, nombres, apellidos, telefono, edad, url[0])

            if (actualizar):
                return url[0]

        else:
            status = int(0)
            return status

    def actualizar(self, documento, content):
        consulta = personas.ConsultaId(documento)

        if (len(consulta) < 1):
            return False

        correo = content['correo']

        verificarCorreo = personas.VerificarCorreo(correo)

        if (verificarCorreo):
            status = int(0)
            return status

        nombres = content['nombres']
        apellidos = content['apellidos']
        telefono = content['telefono']
        edad = content['edad']
        imagen = content['url']

        actualizar = personas.actualizarPersona(
            documento, correo, nombres, apellidos, telefono, edad, imagen)

        return imagen

    def actualizarPassword(self, correo, content):

        verificarCorreo = personas.VerificarCorreoPassword(correo)

        if (verificarCorreo):
            password = content.get('password')

            try:
                salt = bcrypt.gensalt()
                hash_password = bcrypt.hashpw(
                    bytes(str(password), encoding='utf-8'), salt)
                final_password = hash_password.decode()

                actualizar = personas.actualizarPassword(
                    correo, final_password)

                if (actualizar):
                    return True

            except Exception as Error:
                return Error
