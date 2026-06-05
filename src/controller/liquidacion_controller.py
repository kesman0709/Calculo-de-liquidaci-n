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

    def buscar_por_id(id: int) -> DatosLiquidacion:
        """Trae una liquidacion dado su id, retorna DatosLiquidacion o None.
        Usado por los tests."""
        cursor = LiquidacionController.obtener_cursor()
        consulta = """select salario_hora, dias_trabajados, vacaciones_pendientes,
                      aplica_indemnizacion, valor_indemnizacion
                      from liquidaciones where id = %s"""
        cursor.execute(consulta, (id,))
        fila = cursor.fetchone()
        cursor.connection.close()
        if fila is None:
            return None
        return DatosLiquidacion(
            salario_hora=float(fila[0]),
            dias_trabajados=int(fila[1]),
            vacaciones_pendientes=int(fila[2]),
            aplica_indemnizacion=bool(fila[3]),
            valor_indemnizacion=float(fila[4])
        )

    def buscar_por_id_web(id: int) -> tuple:
        """Trae una liquidacion dado su id como tupla de 7 campos.
        Usado por la vista web."""
        cursor = LiquidacionController.obtener_cursor()
        consulta = """select id, salario_hora, dias_trabajados, vacaciones_pendientes,
                      aplica_indemnizacion, valor_indemnizacion, total
                      from liquidaciones where id = %s"""
        cursor.execute(consulta, (int(id),))
        fila = cursor.fetchone()
        cursor.connection.close()
        return fila

    def obtener_todas() -> list:
        """Trae todas las liquidaciones guardadas"""
        cursor = LiquidacionController.obtener_cursor()
        consulta = """select id, salario_hora, dias_trabajados, vacaciones_pendientes,
                      aplica_indemnizacion, valor_indemnizacion, total
                      from liquidaciones order by id"""
        cursor.execute(consulta)
        resultado = cursor.fetchall()
        cursor.connection.close()
        return resultado

    def obtener_ultimo_id() -> int:
        """Retorna el id del ultimo registro insertado"""
        cursor = LiquidacionController.obtener_cursor()
        cursor.execute("select max(id) from liquidaciones")
        resultado = cursor.fetchone()[0]
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
        return connection.cursor()