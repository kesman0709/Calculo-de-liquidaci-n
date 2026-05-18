import sys
sys.path.append(".")
sys.path.append("src")

import psycopg2

from model.logica_liquidacion import DatosLiquidacion
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
        consulta = """select id, salario_hora, dias_trabajados, vacaciones_pendientes,
                      aplica_indemnizacion, valor_indemnizacion, total
                      from liquidaciones where id = %s"""
        cursor.execute(consulta, (id,))
        fila = cursor.fetchone()
        if fila is None:
            return None
        resultado = DatosLiquidacion(
            salario_hora=float(fila[1]),
            dias_trabajados=int(fila[2]),
            vacaciones_pendientes=int(fila[3]),
            aplica_indemnizacion=bool(fila[4]),
            valor_indemnizacion=float(fila[5])
        )
        return resultado

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
        fila = cursor.fetchone()
        return fila[0]

    def modificar(id: int, datos: DatosLiquidacion, total: float):
        """Actualiza un registro existente por su id"""
        cursor = LiquidacionController.obtener_cursor()
        consulta = """update liquidaciones set
            salario_hora = %s,
            dias_trabajados = %s,
            vacaciones_pendientes = %s,
            aplica_indemnizacion = %s,
            valor_indemnizacion = %s,
            total = %s
            where id = %s"""
        cursor.execute(consulta, (
            datos.salario_hora,
            datos.dias_trabajados,
            datos.vacaciones_pendientes,
            datos.aplica_indemnizacion,
            datos.valor_indemnizacion,
            total,
            id
        ))
        cursor.connection.commit()

    def obtener_cursor():
        """Crea la conexion a la base de datos y retorna un cursor para hacer consultas"""
        connection = psycopg2.connect(
            database=secret_config.PGDATABASE,
            user=secret_config.PGUSER,
            password=secret_config.PGPASSWORD,
            host=secret_config.PGHOST,
            port=secret_config.PGPORT
        )
        cursor = connection.cursor()
        return cursor
