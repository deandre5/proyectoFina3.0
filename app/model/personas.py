from os import stat
import psycopg2


class Ingresosistema():

    def insert(self, nombres, apellidos, documento, ficha, idprograma, telefono, correo, edad, password, jornada, tipopersona, tipouser, fecha):
        try:
            conexion = psycopg2.connect(database="dd1o1liu6nsqob", user="gvjdpzhyjsvfxs", password="5ffbbd36b7bf7d3ff6e7edb572b8667da3b15d4396b445f4e705f13c25f8d075",
                                        host="ec2-52-23-190-126.compute-1.amazonaws.com", port="5432")

            cursor = conexion.cursor()

            sql = "INSERT INTO personas VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            datos = (nombres, apellidos, documento, ficha, idprograma, telefono,
                     correo, edad, password, jornada, tipopersona, tipouser, fecha)

            cursor.execute(sql, datos)

            conexion.commit()

            status = True

        except Exception as error:
            print("Error in the conexion with the database", error)

            status = False

        finally:
            cursor.close()
            conexion.close()
            return status

    def datosIngreso(self):
        try:
            conexion = psycopg2.connect(database="dd1o1liu6nsqob", user="gvjdpzhyjsvfxs", password="5ffbbd36b7bf7d3ff6e7edb572b8667da3b15d4396b445f4e705f13c25f8d075",
                                        host="ec2-52-23-190-126.compute-1.amazonaws.com", port="5432")
            cursor = conexion.cursor()

            sql = "select i.idingreso,per.nombres,per.apellidos,per.documento,per.edad,per.ficha,per.jornada,i.fecha,i.horaingreso,i.horasalida from personas per,ingreso i where per.idingreso=i.idingreso ORDER BY per.nombres, per.apellidos ASC"

            cursor.execute(sql)

            consulregistro = cursor.fetchall()
            Consultas = []
            for item in consulregistro:
                items = {"idpersona": item[0], "nombres": item[1], "apellidos": item[2], "documento": item[3],
                         "edad": item[4], "ficha": item[5], "jornada": item[6], "fecha": str(item[7]),
                         "horaentrada": str(item[8]), "horasalida": str(item[9])}
                Consultas.append(items)

            print(consulregistro)
            conexion.commit()

        except Exception as error:
            print("Error in the connection with the data base", error)

        finally:
            cursor.close()
            conexion.close()
            return Consultas

    def datosIngresoReporte(self):
        try:
            conexion = psycopg2.connect(database="dd1o1liu6nsqob", user="gvjdpzhyjsvfxs", password="5ffbbd36b7bf7d3ff6e7edb572b8667da3b15d4396b445f4e705f13c25f8d075",
                                        host="ec2-52-23-190-126.compute-1.amazonaws.com", port="5432")
            cursor = conexion.cursor()

            sql = "select i.idingreso,per.nombres,per.apellidos,per.documento,per.edad,per.ficha,per.jornada,i.fecha,i.horaingreso,i.horasalida from personas per,ingreso i where per.documento=i.documento ORDER BY per.nombres, per.apellidos ASC"

            cursor.execute(sql)

            consulregistro = cursor.fetchall()
            Consultas = []
            for item in consulregistro:
                items = {"idpersona": item[0], "nombres": item[1], "apellidos": item[2], "documento": item[3],
                         "edad": item[4], "ficha": item[5], "jornada": item[6], "fecha": str(item[7]),
                         "horaentrada": str(item[8]), "horasalida": str(item[9])}
                Consultas.append(items)

            print(consulregistro)
            conexion.commit()

        except Exception as error:
            print("Error in the connection with the data base", error)

        finally:
            cursor.close()
            conexion.close()
            return Consultas

    def consult(self, documento, correo):
        try:
            conexion = psycopg2.connect(database="dd1o1liu6nsqob", user="gvjdpzhyjsvfxs", password="5ffbbd36b7bf7d3ff6e7edb572b8667da3b15d4396b445f4e705f13c25f8d075",
                                        host="ec2-52-23-190-126.compute-1.amazonaws.com", port="5432")

            cursor = conexion.cursor()

            sql = "SELECT * FROM personas WHERE documento = %s or correo = %s"

            cursor.execute(sql, (documento, correo,))
            diccionario = cursor.fetchall()
            conexion.commit()

            print(diccionario)

            # se examina el len del diccionario despues de la consulta, si es mayor a cero se devuelve true ya que se encuentra repetido

            if len(diccionario) > 0:
                status = True
            # caso contrario false
            else:
                status = False

        except Exception as error:
            print("Error in the conetion with the database", error)

            status = False

        finally:

            cursor.close()
            conexion.close()
            return status

    def consultarDocumento(self, documento):
        try:
            conexion = psycopg2.connect(database="dd1o1liu6nsqob", user="gvjdpzhyjsvfxs", password="5ffbbd36b7bf7d3ff6e7edb572b8667da3b15d4396b445f4e705f13c25f8d075",
                                        host="ec2-52-23-190-126.compute-1.amazonaws.com", port="5432")

            cursor = conexion.cursor()

            sql = "SELECT * FROM personas WHERE documento = %s"

            cursor.execute(sql, (documento, ))
            diccionario = cursor.fetchall()
            conexion.commit()

            print(diccionario)

            # se examina el len del diccionario despues de la consulta, si es mayor a cero se devuelve true ya que se encuentra repetido

            if len(diccionario) > 0:
                status = True
            # caso contrario false
            else:
                status = False

        except Exception as error:
            print("Error in the conetion with the database", error)

            status = False

        finally:

            cursor.close()
            conexion.close()
            return status

    def consultaridpersona(self):
        try:
            conexion = psycopg2.connect(database="dd1o1liu6nsqob", user="gvjdpzhyjsvfxs", password="5ffbbd36b7bf7d3ff6e7edb572b8667da3b15d4396b445f4e705f13c25f8d075",
                                        host="ec2-52-23-190-126.compute-1.amazonaws.com", port="5432")

            cursor = conexion.cursor()
            sql = "SELECT * FROM ingreso ORDER BY idingreso ASC"

            cursor.execute(sql)

            consulregistro = cursor.fetchall()
            consulta = []
            for item in consulregistro:
                items = {"id": item[0]}
                consulta.append(items)

            conexion.commit()

        except Exception as error:
            print("Error in the connection with the data base", error)

        finally:
            cursor.close()
            conexion.close()
            return consulta

    def insertIngreso(self, id, documento, fecha, horaingreso):

        try:
            conexion = psycopg2.connect(database="dd1o1liu6nsqob", user="gvjdpzhyjsvfxs", password="5ffbbd36b7bf7d3ff6e7edb572b8667da3b15d4396b445f4e705f13c25f8d075",
                                        host="ec2-52-23-190-126.compute-1.amazonaws.com", port="5432")

            cursor = conexion.cursor()

            sql = "INSERT INTO ingreso VALUES(%s,%s,%s,%s)"

            datos = (id, fecha, horaingreso, documento)

            cursor.execute(sql, datos)

            sql = "UPDATE personas SET idingreso = %s WHERE documento = %s"

            idingreso = (id)
            documento = (documento)

            cursor.execute(sql, (idingreso, documento))

            conexion.commit()

            status = True
        except Exception as error:
            print("Error in the connection with the data base", error)

            status = False
        finally:
            cursor.close()
            conexion.close()
            return status

    def idIngreso(self, documento):
        try:
            conexion = psycopg2.connect(database="dd1o1liu6nsqob", user="gvjdpzhyjsvfxs", password="5ffbbd36b7bf7d3ff6e7edb572b8667da3b15d4396b445f4e705f13c25f8d075",
                                        host="ec2-52-23-190-126.compute-1.amazonaws.com", port="5432")

            cursor = conexion.cursor()

            sql = "SELECT idingreso FROM personas WHERE documento = %s"

            cursor.execute(sql, (documento,))

            diccionario = cursor.fetchall()

            diccionarios = []

            for item in diccionario:
                items = {"idingreso": item[0]}
                diccionarios.append(items)

            conexion.commit()

        except Exception as error:
            print(error)

        finally:
            cursor.close()
            conexion.close()
            return diccionarios

    def consultaIngreso(self, documento, fecha):

        try:
            conexion = psycopg2.connect(database="dd1o1liu6nsqob", user="gvjdpzhyjsvfxs", password="5ffbbd36b7bf7d3ff6e7edb572b8667da3b15d4396b445f4e705f13c25f8d075",
                                        host="ec2-52-23-190-126.compute-1.amazonaws.com", port="5432")

            cursor = conexion.cursor()

            sql = "SELECT * FROM ingreso WHERE fecha = %s AND documento =%s"

            cursor.execute(sql, (fecha, documento))

            diccionario = cursor.fetchall()

            if len(diccionario) > 0:
                status = True
            else:
                status = False

            conexion.commit()

            status = True
        except Exception as error:
            print("Error in the connection with the data base", error)

            status = False
        finally:
            cursor.close()
            conexion.close()
            return status

    def registrarSalida(self, idingreso, horasalida):

        try:
            conexion = psycopg2.connect(database="dd1o1liu6nsqob", user="gvjdpzhyjsvfxs", password="5ffbbd36b7bf7d3ff6e7edb572b8667da3b15d4396b445f4e705f13c25f8d075",
                                        host="ec2-52-23-190-126.compute-1.amazonaws.com", port="5432")

            cursor = conexion.cursor()

            sql = "UPDATE ingreso SET horasalida = %s WHERE idingreso =%s "

            idingreso = (idingreso,)

            horasalida = (horasalida)

            cursor.execute(sql, (horasalida, idingreso,))

            conexion.commit()

            status = True
        except Exception as error:
            print("Error in the connection with the data base", error)

            status = False
        finally:
            cursor.close()
            conexion.close()
            return status

    def consultaUsuarios(self):
        try:
            conexion = psycopg2.connect(database="dd1o1liu6nsqob", user="gvjdpzhyjsvfxs", password="5ffbbd36b7bf7d3ff6e7edb572b8667da3b15d4396b445f4e705f13c25f8d075",
                                        host="ec2-52-23-190-126.compute-1.amazonaws.com", port="5432")

            cursor = conexion.cursor()

            sql = "SELECT p.nombres, p.apellidos, p.documento, p.ficha, pr.nombreprograma, p.telefono, p.correo, p.edad, p.jornada, p.tipopersona, p.tipouser, p.fecha,  p.imagen FROM personas p, programas pr WHERE p.idprograma = pr.idprograma ORDER BY nombres, apellidos ASC"

            cursor.execute(sql,)

            consulregistro = cursor.fetchall()

            Consultas = []

            for item in consulregistro:
                items = {"nombres": item[0], "apellidos": item[1], "documento": item[2], "ficha": item[3], "programa": item[4],
                         "telefono": item[5], "correo": item[6], "edad": item[7], "jornada": item[8],
                         "tipopersona": item[9], "tipouser": item[10], "fecha": item[11], "imagen": item[12], }
                Consultas.append(items)

            conexion.commit()

            status = True
        except Exception as error:
            print("Error in the connection with the data base", error)

        finally:
            cursor.close()
            conexion.close()
            return Consultas

    def consultaUsuariosID(self, documento):
        try:
            conexion = psycopg2.connect(database="dd1o1liu6nsqob", user="gvjdpzhyjsvfxs", password="5ffbbd36b7bf7d3ff6e7edb572b8667da3b15d4396b445f4e705f13c25f8d075",
                                        host="ec2-52-23-190-126.compute-1.amazonaws.com", port="5432")

            cursor = conexion.cursor()

            sql = "SELECT p.nombres, p.apellidos, p.documento, p.ficha, pr.nombreprograma, p.telefono, p.correo, p.edad, p.jornada, p.tipopersona, p.tipouser, p.fecha,  p.imagen FROM personas p, programas pr WHERE p.idprograma = pr.idprograma AND p.documento = %s"

            cursor.execute(sql, (documento, ))

            consulregistro = cursor.fetchall()

            Consultas = []

            for item in consulregistro:
                items = {"nombres": item[0], "apellidos": item[1], "documento": item[2], "ficha": item[3], "programa": item[4],
                         "telefono": item[5], "correo": item[6], "edad": item[7], "jornada": item[8],
                         "tipopersona": item[9], "tipouser": item[10], "fecha": item[11], "imagen": item[12], }
                Consultas.append(items)

            conexion.commit()

            status = True
        except Exception as error:
            print("Error in the connection with the data base", error)

        finally:
            cursor.close()
            conexion.close()
            return Consultas

    def ConsultaId(self, documento):
        try:
            conexion = psycopg2.connect(database="dd1o1liu6nsqob", user="gvjdpzhyjsvfxs", password="5ffbbd36b7bf7d3ff6e7edb572b8667da3b15d4396b445f4e705f13c25f8d075",
                                        host="ec2-52-23-190-126.compute-1.amazonaws.com", port="5432")
            cursor = conexion.cursor()

            sql = "SELECT * FROM personas WHERE documento = %s"
            cursor.execute(sql, (documento, ))
            diccionario = cursor.fetchall()
            diccionarios = []
            # for que nos permite crear un objeto items para luego añadirlo a una lista y devolver su contenido
            for item in diccionario:
                items = {"nombres": item[0], "apellidos": item[1], "telefono": item[5],
                         "correo": item[6], "edad": item[7], "imagen": item[15]}

            diccionarios.append(items)

            conexion.commit()

        except Exception as error:
            print("Error in the conetion with the database", error)
        finally:
            print(diccionarios)
            cursor.close()
            conexion.close()
            return diccionarios

    def VerificarCorreo(self, correo):
        try:
            conexion = psycopg2.connect(database="dd1o1liu6nsqob", user="gvjdpzhyjsvfxs", password="5ffbbd36b7bf7d3ff6e7edb572b8667da3b15d4396b445f4e705f13c25f8d075",
                                        host="ec2-52-23-190-126.compute-1.amazonaws.com", port="5432")

            cursor = conexion.cursor()

            sql = "SELECT * FROM personas WHERE correo = %s"

            cursor.execute(sql, (correo,))
            diccionario = cursor.fetchall()
            conexion.commit()

            print(diccionario)

            # se examina el len del diccionario despues de la consulta, si es mayor a cero se devuelve true ya que se encuentra repetido

            if len(diccionario) > 1:
                status = True
            # caso contrario false
            else:
                status = False

        except Exception as error:
            print("Error in the conetion with the database", error)

            status = False

        finally:

            cursor.close()
            conexion.close()
            return status

    def actualizarPersona(self, documento, correo, nombres, apellidos, telefono, edad, url):
        try:
            conexion = psycopg2.connect(database="dd1o1liu6nsqob", user="gvjdpzhyjsvfxs", password="5ffbbd36b7bf7d3ff6e7edb572b8667da3b15d4396b445f4e705f13c25f8d075",
                                        host="ec2-52-23-190-126.compute-1.amazonaws.com", port="5432")

            cursor = conexion.cursor()

            sql = "UPDATE personas SET nombres = %s, apellidos = %s, correo = %s, telefono = %s, edad = %s, imagen = %s WHERE documento = %s "

            documento = (documento)
            nombres = (nombres)
            apellidos = (apellidos)
            correo = (correo)
            telefono = (telefono)
            edad = (edad)
            imagen = (url)

            cursor.execute(sql, (nombres, apellidos, correo,
                                 telefono, edad, imagen, documento))
            conexion.commit()
            status = True

        except Exception as error:
            print("Error in the conetion with the database", error)
            status = False
        finally:
            cursor.close()
            conexion.close()
            return status

    def programas(self):
        try:
            conexion = psycopg2.connect(database="dd1o1liu6nsqob", user="gvjdpzhyjsvfxs", password="5ffbbd36b7bf7d3ff6e7edb572b8667da3b15d4396b445f4e705f13c25f8d075",
                                        host="ec2-52-23-190-126.compute-1.amazonaws.com", port="5432")
            cursor = conexion.cursor()

            sql = "SELECT * FROM programas ORDER BY idprograma ASC"
            cursor.execute(sql)
            diccionario = cursor.fetchall()
            diccionarios = []
            # for que nos permite crear un objeto items para luego añadirlo a una lista y devolver su contenido
            for item in diccionario:
                items = {"id": item[0], "programa": item[1]}

                diccionarios.append(items)

            conexion.commit()

        except Exception as error:
            print("Error in the conetion with the database", error)
        finally:
            print(diccionarios)
            cursor.close()
            conexion.close()
            return diccionarios

    def actualizarPassword(self, correo, password):
        try:
            conexion = psycopg2.connect(database="dd1o1liu6nsqob", user="gvjdpzhyjsvfxs", password="5ffbbd36b7bf7d3ff6e7edb572b8667da3b15d4396b445f4e705f13c25f8d075",
                                        host="ec2-52-23-190-126.compute-1.amazonaws.com", port="5432")
            cursor = conexion.cursor()

            sql = "UPDATE personas SET contraseña = %s WHERE correo = %s"

            password = (password)
            correo = (correo)

            cursor.execute(sql, (password, correo,))

            conexion.commit()
            status = True

        except Exception as error:
            print("Error in the conetion with the database", error)
            status = False
        finally:
            cursor.close()
            conexion.close()
            return status

    def VerificarCorreoPassword(self, correo):
        try:
            conexion = psycopg2.connect(database="dd1o1liu6nsqob", user="gvjdpzhyjsvfxs", password="5ffbbd36b7bf7d3ff6e7edb572b8667da3b15d4396b445f4e705f13c25f8d075",
                                        host="ec2-52-23-190-126.compute-1.amazonaws.com", port="5432")

            cursor = conexion.cursor()

            sql = "SELECT * FROM personas WHERE correo = %s"

            cursor.execute(sql, (correo,))
            diccionario = cursor.fetchall()
            conexion.commit()

            print(diccionario)

            # se examina el len del diccionario despues de la consulta, si es mayor a cero se devuelve true ya que se encuentra repetido

            if len(diccionario) >= 1:
                status = True
            # caso contrario false
            else:
                status = False

        except Exception as error:
            print("Error in the conetion with the database", error)

            status = False

        finally:

            cursor.close()
            conexion.close()
            return status

    def remove(self, documento):
        try:
            conexion = psycopg2.connect(database="dd1o1liu6nsqob", user="gvjdpzhyjsvfxs", password="5ffbbd36b7bf7d3ff6e7edb572b8667da3b15d4396b445f4e705f13c25f8d075",
                                        host="ec2-52-23-190-126.compute-1.amazonaws.com", port="5432")

            cursor = conexion.cursor()

            sql = "DELETE FROM personas WHERE documento = %s"

            cursor.execute(sql, (documento,))
            conexion.commit()

            status = True
        except Exception as error:
            print("Error in the connection with the database", error)
            status = False

        finally:
            cursor.close()
            conexion.close()
            return status

    def consultarIDR(self, id):
        try:
            conexion = psycopg2.connect(database="dd1o1liu6nsqob", user="gvjdpzhyjsvfxs", password="5ffbbd36b7bf7d3ff6e7edb572b8667da3b15d4396b445f4e705f13c25f8d075",
                                        host="ec2-52-23-190-126.compute-1.amazonaws.com", port="5432")

            cursor = conexion.cursor()

            sql = "SELECT * FROM rutinas WHERE id = %s"

            cursor.execute(sql, (id,))
            diccionario = cursor.fetchall()
            diccionarios = []

            for item in diccionario:
                try:
                    sql = "SELECT * FROM rutinasejercicio re, ejercicios e where re.idrutinas=%s AND e.id = re.idejercicio"
                    cursor.execute(sql, (item[0],))
                    ejercicio = cursor.fetchall()

                    # se crea un objeto de tipo items que recoje la informacion de la rutina
                    items = {"id": item[0], "nombre": item[1], "descripcion": item[2],
                             "intensidad": item[3], "dificultad": item[4], "categoria": item[5]}
                    ejercicios = []

                    # si hay ejercicios vinculados a la rutina se agregan a la informacion y se envia
                    for i in ejercicio:

                        ejer = {"idejercicio": i[0], "repeticiones": i[1], "series": i[2],
                                "ejecucion": i[3], "dia": i[4], "idrutinas": i[5], "nombre": i[7], "descripcion": i[8], "imagen": i[9], "tipo": i[10]}

                        ejercicios.append(ejer)

                        items["ejercicios"] = ejercicios

                except Exception as error:
                    print("Error in the conetion with the database", error)
                    pass

                diccionarios.append(items)

            conexion.commit()

            status = diccionarios

        except Exception as error:
            print("Error in the conetion with the database", error)

            status = False

        finally:

            cursor.close()
            conexion.close()
            return status

    def Email(self, correo):
        try:
            conexion = psycopg2.connect(database="dd1o1liu6nsqob", user="gvjdpzhyjsvfxs", password="5ffbbd36b7bf7d3ff6e7edb572b8667da3b15d4396b445f4e705f13c25f8d075",
                                        host="ec2-52-23-190-126.compute-1.amazonaws.com", port="5432")

            cursor = conexion.cursor()

            sql = "SELECT nombres, apellidos FROM personas WHERE correo = %s"

            cursor.execute(sql, (correo, ))
            diccionario = cursor.fetchall()

            diccionarios = []

            for item in diccionario:
                items = {"nombre": item[0], "apellidos": item[1]}
                diccionarios.append(items)

            conexion.commit()

        except Exception as error:
            print("Error in the conetion with the database", error)

        finally:

            cursor.close()
            conexion.close()
            return diccionarios
