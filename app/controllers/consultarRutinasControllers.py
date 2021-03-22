from app.model.personas import Ingresosistema


personas = Ingresosistema()

class ConsultarRutinas():
    def consultar(self, id):
        diccionario = personas.consultarIDR(id)
        return diccionario