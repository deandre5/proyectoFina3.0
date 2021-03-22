from app.model.personas import Ingresosistema

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