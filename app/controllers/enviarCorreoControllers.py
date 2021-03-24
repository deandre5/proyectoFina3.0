from app.model.personas import Ingresosistema
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

personas = Ingresosistema()


class EnvioCorreos():
    def enviarCorreos(self, content, correo):

        try:

            mensaje = content.get('mensaje')
            asunto = content.get('asunto')

            consulta = personas.Email(correo)

            for i in consulta:
                nombre = i.get('nombre')
                apellidos = i.get('apellidos')

            # credenciales
            proveedor_correo = 'smtp.live.com: 587'
            remitente = 'gymsena@hotmail.com'
            password = 'Adsi2021'
            # conexion a servidor
            servidor = smtplib.SMTP(proveedor_correo)
            servidor.starttls()
            servidor.ehlo()
            # autenticacion
            servidor.login(remitente, password)
            # mensaje

            msg = MIMEMultipart()
            msg.attach(MIMEText(mensaje+" Enviado por "+nombre +
                                " "+apellidos+" correo: "+correo, 'html'))
            msg['From'] = remitente
            msg['To'] = remitente
            msg['Subject'] = asunto
            servidor.sendmail(msg['From'], msg['To'], msg.as_string())

            return True

        except Exception as error:
            print(error)
            return str(error)
