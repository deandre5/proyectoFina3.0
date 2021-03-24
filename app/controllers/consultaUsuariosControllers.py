from app.model.personas import Ingresosistema

import io
import xlwt


personas = Ingresosistema()


class ConsultaUsuarios():
    def consultarGeneral(self):

        consulta = personas.consultaUsuarios()

        if (consulta):
            return consulta

        else:
            return False

    def consultarID(self, documento):

        consulta = personas.consultaUsuariosID(documento)

        if (consulta):
            return consulta

        else:
            return False

    def programas(self):
        consulta = personas.programas()

        if (consulta):
            return consulta

        else:
            return False

    def reporteUsuarios(self):
        consulta = personas.consultaUsuarios()

        output = io.BytesIO()

        worbook = xlwt.Workbook()
        sh = worbook.add_sheet("Reporte de usuarios")

        sh.write(0, 0, "Nombres")
        sh.write(0, 1, "Apellidos")
        sh.write(0, 2, "documento")
        sh.write(0, 3, "ficha")
        sh.write(0, 4, "programa")
        sh.write(0, 5, "telefono")
        sh.write(0, 6, "correo")
        sh.write(0, 7, "edad")
        sh.write(0, 8, "jornada")
        sh.write(0, 9, "tipo persona")
        sh.write(0, 10, "tipo user")
        sh.write(0, 11, "fecha")

        idx = 0

        for item in consulta:
            sh.write(idx+1, 0, str(item.get('nombres')))
            sh.write(idx+1, 1, str(item.get('apellidos')))
            sh.write(idx+1, 2, str(item.get('documento')))
            sh.write(idx+1, 3, str(item.get('ficha')))
            sh.write(idx+1, 4, str(item.get('programa')))
            sh.write(idx+1, 5, str(item.get('telefono')))
            sh.write(idx+1, 6, str(item.get('correo')))
            sh.write(idx+1, 7, str(item.get('edad')))
            sh.write(idx+1, 8, str(item.get('jornada')))
            sh.write(idx+1, 9, str(item.get('tipopersona')))
            sh.write(idx+1, 10, str(item.get('tipouser')))
            sh.write(idx+1, 11, str(item.get('fecha')))

            idx += 1
        worbook.save(output)
        output.seek(0)

        return output
