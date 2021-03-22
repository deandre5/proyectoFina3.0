from app.model.personas import Ingresosistema


personas = Ingresosistema()


class eliminarUsuario():
    def eliminar(documento):

        consulta = personas.ConsultaId(documento)

        if (len(consulta) > 0):
            remover = personas.remove(documento)
            return remover

        else:
            return False

