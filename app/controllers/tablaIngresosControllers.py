from app.model.personas import Ingresosistema


import io
import xlwt


ingreso = Ingresosistema()


class tablaIngreso():
    def datosIngreso(self):
        result = ingreso.datosIngreso()
        return result

    def reporteIngreso(self):
        consulta = ingreso.datosIngresoReporte()

        output = io.BytesIO()

        worbook = xlwt.Workbook()
        sh = worbook.add_sheet("Reporte de Ingreso")

        sh.write(0, 0, "ID")
        sh.write(0, 1, "Nombres")
        sh.write(0, 2, "Apellidos")
        sh.write(0, 3, "Documento")
        sh.write(0, 4, "Edad")
        sh.write(0, 5, "Ficha")
        sh.write(0, 6, "Jornada")
        sh.write(0, 7, "Fecha")
        sh.write(0, 8, "Hora de entrada")
        sh.write(0, 9, "Hora de salida")

        idx = 0

        for item in consulta:
            sh.write(idx+1, 0, str(item.get('idpersona')))
            sh.write(idx+1, 1, str(item.get('nombres')))
            sh.write(idx+1, 2, str(item.get('apellidos')))
            sh.write(idx+1, 3, str(item.get('documento')))
            sh.write(idx+1, 4, str(item.get('edad')))
            sh.write(idx+1, 5, str(item.get('ficha')))
            sh.write(idx+1, 6, str(item.get('jornada')))
            sh.write(idx+1, 7, str(item.get('fecha')))
            sh.write(idx+1, 8, str(item.get('horaentrada')))
            sh.write(idx+1, 9, str(item.get('horasalida')))

            idx += 1
        worbook.save(output)
        output.seek(0)

        return output
