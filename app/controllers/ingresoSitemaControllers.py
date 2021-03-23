from app.model.personas import Ingresosistema
from datetime import datetime
from dateutil import tz

from_zone = tz.gettz('UTC')
to_zone = tz.gettz('America/Atikokan')

now = datetime.utcfromtimestamp(to_zone)

personas = Ingresosistema()


class Ingresosistema():
    def ingresarSitemas(self, documento):

        consulta = personas.consultarDocumento(documento)

        if (consulta):

            consulta = personas.consultaridpersona()
            print(consulta)
            # si hay ejercicios registrados se toma el ultimo y se le suma 1 al id, luego se toma este id y se envia para el registro del ejercicio
            if consulta:
                for i in consulta:
                    id_bd = i.get('id')+1
            # si no hay ejercicios registrados, este toma el valor de 1
            else:
                id_bd = 1
            fecha = str(now.year)+"-"+str(now.month)+"-"+str(now.day)
            horaingreso = str(now.hour)+":"+str(now.minute)


            insert = personas.insertIngreso(
                id_bd, documento, fecha, horaingreso)

            if (insert):
                return True

            else:
                return False
        else:
            status = int(0)
            return status


    def salir(self, documento):

        fecha = str(now.year)+"-"+str(now.month)+"-"+str(now.day)

        consultaIngreso = personas.consultaIngreso(documento,fecha)

        if (consultaIngreso):

            horasalida =  str(now.hour)+":"+str(now.minute)

            

            registrarSalida = personas.registrarSalida(documento, fecha, horasalida)

            if (registrarSalida):
                return registrarSalida

            else:
                return False

        else:
            status = int(0)
            return status


