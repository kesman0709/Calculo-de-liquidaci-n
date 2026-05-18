import sys
sys.path.append(".")
sys.path.append("src")

import psycopg2

from src.model.logica_liquidacion import DatosLiquidacion
import secret_config


class LiquidacionController:

    def crear_tabla():
        """Crea la tabla liquidaciones en la base de datos"""
        cursor = LiquidacionController.obtener_cursor()
        with open("sql/crear-liquidaciones.sql", "r") as archivo:
            consulta = archivo.read()
        cursor.execute(consulta)
        cursor.connection.commit()

    def borrar_tabla():
        """Borra la tabla liquidaciones de la base de datos"""
        cursor = LiquidacionController.obtener_cursor()
        with open("sql/borrar-liquidaciones.sql", "r") as archivo:
            consulta = archivo.read()
        cursor.execute(consulta)
        cursor.connection.commit()

    def insertar(datos: DatosLiquidacion, total: float):
        """Recibe una instancia de DatosLiquidacion y el total, y los inserta en la tabla"""
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

    def buscar_por_id(id: int) -> DatosLiquidacion:
        """Busca una liquidacion por su id y retorna una instancia de DatosLiquidacion"""
        cursor = LiquidacionController.obtener_cursor()
        consulta = """select salario_hora, dias_trabajados, vacaciones_pendientes,
                      aplica_indemnizacion, valor_indemnizacion
                      from liquidaciones where id = %s"""
        cursor.execute(consulta, (id,))
        fila = cursor.fetchone()
        if fila is None:
            return None
        return DatosLiquidacion(
            salario_hora=float(fila[0]),
            dias_trabajados=int(fila[1]),
            vacaciones_pendientes=int(fila[2]),
            aplica_indemnizacion=bool(fila[3]),
            valor_indemnizacion=float(fila[4])
        )

    def obtener_todas() -> list:
        """Retorna todas las liquidaciones guardadas como lista de filas"""
        cursor = LiquidacionController.obtener_cursor()
        consulta = """select id, salario_hora, dias_trabajados, vacaciones_pendientes,
                      aplica_indemnizacion, valor_indemnizacion, total
                      from liquidaciones order by id"""
        cursor.execute(consulta)
        return cursor.fetchall()

    def obtener_ultimo_id() -> int:
        """Retorna el id del ultimo registro insertado"""
        cursor = LiquidacionController.obtener_cursor()
        cursor.execute("select max(id) from liquidaciones")
        return cursor.fetchone()[0]

    def obtener_cursor():
        """Crea la conexion a la base de datos y retorna un cursor para hacer consultas"""
        connection = psycopg2.connect(
            database=secret_config.PGDATABASE,
            user=secret_config.PGUSER,
            password=secret_config.PGPASSWORD,
            host=secret_config.PGHOST,
            port=secret_config.PGPORT
        )
        return connection.cursor()