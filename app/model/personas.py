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

            sql = "select i.idpersona,per.nombres,per.apellidos,per.documento,per.edad,per.ficha,per.jornada,i.fecha,i.horaingreso,i.horasalida from personas per,ingreso i where per.documento=i.documento"

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
            sql = "SELECT * FROM ingreso "

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

            conexion.commit()

            status = True
        except Exception as error:
            print("Error in the connection with the data base", error)

            status = False
        finally:
            cursor.close()
            conexion.close()
            return status

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

    def registrarSalida(self, documento, fecha, horasalida):

        try:
            conexion = psycopg2.connect(database="dd1o1liu6nsqob", user="gvjdpzhyjsvfxs", password="5ffbbd36b7bf7d3ff6e7edb572b8667da3b15d4396b445f4e705f13c25f8d075",
                                        host="ec2-52-23-190-126.compute-1.amazonaws.com", port="5432")

            cursor = conexion.cursor()

            sql = "UPDATE ingreso SET horasalida = %s WHERE fecha =%s AND documento = %s"

            documento = (documento)
            fecha = (fecha)
            horasalida = (horasalida)

            cursor.execute(sql, (horasalida, fecha, documento,))

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
                         "correo": item[6], "edad": item[7], "imagen": item[15] }

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

            cursor.execute(sql, (nombres, apellidos, correo, telefono, edad, imagen, documento))
            conexion.commit()
            status = True

        except Exception as error:
            print("Error in the conetion with the database", error)
            status = False
        finally:
            cursor.close()
            conexion.close()
            return status  
