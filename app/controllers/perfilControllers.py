from app.model.personas import Ingresosistema

personas = Ingresosistema()


class Perfil():
    def consultarPerfil(self, documento):

        consulta = personas.ConsultaId(documento)

        if (consulta):
            return consulta

        else:
            return False
