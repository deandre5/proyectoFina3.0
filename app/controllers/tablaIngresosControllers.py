from app.model.personas import Ingresosistema

ingreso = Ingresosistema()


class tablaIngreso():
    def datosIngreso(self):
        result = ingreso.datosIngreso()
        return result
