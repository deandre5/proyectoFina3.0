from app.model.personas import Ingresosistema
import datetime

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
            fecha = datetime.datetime.utcnow()
            horaingreso = str(fecha.hour)+":"+str(fecha.minute)

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

        fecha = datetime.datetime.utcnow()
        dia = fecha.day
        mes = fecha.month
        anio = fecha.year

        consultaIngreso = personas.consultaIngreso(documento,fecha)

        if (consultaIngreso):

            horasalida = str(fecha.hour)+":"+str(fecha.minute)

            fecha = str(anio)+"-"+str(mes)+"-"+str(dia)

            registrarSalida = personas.registrarSalida(documento, fecha, horasalida)

            if (registrarSalida):
                return registrarSalida

            else:
                return False

        else:
            status = int(0)
            return status


