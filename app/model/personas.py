import psycopg2

class Ingresosistema():

    def insert(self, nombres, apellidos, documento, ficha, idprograma, telefono, correo, edad, password, jornada, tipopersona, tipouser, fecha):
        try:
            conexion = psycopg2.connect(database="dd1o1liu6nsqob", user="gvjdpzhyjsvfxs", password="5ffbbd36b7bf7d3ff6e7edb572b8667da3b15d4396b445f4e705f13c25f8d075",
                                        host="ec2-52-23-190-126.compute-1.amazonaws.com", port="5432")

            cursor = conexion.cursor()

            sql = "INSERT INTO personas VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            datos = (nombres, apellidos, documento, ficha, idprograma, telefono, correo, edad, password, jornada, tipopersona, tipouser, fecha)

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
            Consultas=[]
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