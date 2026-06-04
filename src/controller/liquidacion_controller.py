import sys
sys.path.append(".")
sys.path.append("src")

import psycopg2
from model.logica_liquidacion import DatosLiquidacion
import secret_config


class LiquidacionController:

    def crear_tabla():
        cursor = LiquidacionController.obtener_cursor()
        with open("sql/crear-liquidaciones.sql", "r") as archivo:
            consulta = archivo.read()
        cursor.execute(consulta)
        cursor.connection.commit()
        cursor.connection.close()

    def borrar_tabla():
        cursor = LiquidacionController.obtener_cursor()
        with open("sql/borrar-liquidaciones.sql", "r") as archivo:
            consulta = archivo.read()
        cursor.execute(consulta)
        cursor.connection.commit()
        cursor.connection.close()

    def insertar(datos: DatosLiquidacion, total: float):
        """Guarda una liquidacion calculada en la base de datos"""
        cursor = LiquidacionController.obtener_cursor()
        consulta = """insert into liquidaciones
            (salario_hora, dias_trabajados, vacaciones_pendientes,
             aplica_indemnizacion, valor_indemnizacion, total)
            values (%s, %s, %s, %s, %s, %s)"""
        cursor.execute(consulta, (
            datos.salario_hora,
            datos.dias_trabajados,
            datos.vacaciones_pendientes,
            datos.aplica_indemnizacion,
            datos.valor_indemnizacion,
            total
        ))
        cursor.connection.commit()
        cursor.connection.close()

    def buscar_por_id(id: int):
        """Trae una liquidacion dado su id"""
        cursor = LiquidacionController.obtener_cursor()
        consulta = "select * from liquidaciones where id = %s"
        cursor.execute(consulta, (id,))
        resultado = cursor.fetchone()
        cursor.connection.close()
        return resultado

    def obtener_todas():
        """Trae todas las liquidaciones guardadas"""
        cursor = LiquidacionController.obtener_cursor()
        consulta = "select * from liquidaciones order by id"
        cursor.execute(consulta)
        resultado = cursor.fetchall()
        cursor.connection.close()
        return resultado

    def obtener_cursor():
        """Crea la conexion a la base de datos y retorna un cursor"""
        connection = psycopg2.connect(
            database=secret_config.PGDATABASE,
            user=secret_config.PGUSER,
            password=secret_config.PGPASSWORD,
            host=secret_config.PGHOST,
            port=secret_config.PGPORT
        )
        cursor = connection.cursor()
        return cursor


