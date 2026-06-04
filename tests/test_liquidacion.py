import unittest
import sys
sys.path.append("src")

import model.logica_liquidacion as logica_liquidacion
from model.logica_liquidacion import DatosLiquidacion, calcular_liquidacion
from controller.liquidacion_controller import LiquidacionController
import unittest


class LiquidacionTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Test Fixture: borra y recrea la tabla antes de correr las pruebas"""
        LiquidacionController.borrar_tabla()
        LiquidacionController.crear_tabla()

    # ── Tests de lógica ──────────────────────────────────────────────
    def test_normal_1(self):
        datos = logica_liquidacion.DatosLiquidacion(6000, 30)
        resultado = logica_liquidacion.calcular_liquidacion(datos)
        self.assertAlmostEqual(resultado, 1800000, places=2)

    def test_normal_2(self):
        datos = logica_liquidacion.DatosLiquidacion(8000, 15)
        resultado = logica_liquidacion.calcular_liquidacion(datos)
        self.assertAlmostEqual(resultado, 1200000, places=2)

    def test_con_vacaciones(self):
        datos = logica_liquidacion.DatosLiquidacion(7000, 20, 5)
        resultado = logica_liquidacion.calcular_liquidacion(datos)
        self.assertAlmostEqual(resultado, 1750000, places=2)

    def test_con_indemnizacion(self):
        datos = logica_liquidacion.DatosLiquidacion(6666.666667, 30, 0, True, 2000000)
        resultado = logica_liquidacion.calcular_liquidacion(datos)
        self.assertAlmostEqual(resultado, 4000000, places=2)

    def test_dias_minimos(self):
        datos = logica_liquidacion.DatosLiquidacion(5000, 5)
        resultado = logica_liquidacion.calcular_liquidacion(datos)
        self.assertAlmostEqual(resultado, 250000, places=2)

    def test_vacaciones_e_indemnizacion(self):
        datos = logica_liquidacion.DatosLiquidacion(10000, 25, 10, True, 3000000)
        resultado = logica_liquidacion.calcular_liquidacion(datos)
        self.assertAlmostEqual(resultado, 6500000, places=2)

    def test_salario_negativo(self):
        datos = logica_liquidacion.DatosLiquidacion(-6666.666667, 20)
        with self.assertRaises(logica_liquidacion.SalarioInvalido):
            logica_liquidacion.calcular_liquidacion(datos)

    def test_dias_fuera_de_rango(self):
        datos = logica_liquidacion.DatosLiquidacion(6666.666667, 35)
        with self.assertRaises(logica_liquidacion.DiasInvalidos):
            logica_liquidacion.calcular_liquidacion(datos)

    def test_vacaciones_negativas(self):
        datos = logica_liquidacion.DatosLiquidacion(6666.666667, 20, -3)
        with self.assertRaises(logica_liquidacion.VacacionesInvalidas):
            logica_liquidacion.calcular_liquidacion(datos)

    def test_indemnizacion_negativa(self):
        datos = logica_liquidacion.DatosLiquidacion(6666.666667, 20, 0, True, -1000000)
        with self.assertRaises(logica_liquidacion.IndemnizacionInvalida):
            logica_liquidacion.calcular_liquidacion(datos)

    # ── Tests de insertar en BD ──────────────────────────────────────────────

    def test_insertar_1(self):
        """Caso normal: inserta liquidación básica, la busca y verifica que los datos coinciden"""
        datos = logica_liquidacion.DatosLiquidacion(6000, 30)
        total = logica_liquidacion.calcular_liquidacion(datos)
        LiquidacionController.insertar(datos, total)

        id_insertado = LiquidacionController.obtener_ultimo_id()
        datos_buscados = LiquidacionController.buscar_por_id(id_insertado)

        self.assertEqual(datos.salario_hora, datos_buscados.salario_hora)
        self.assertEqual(datos.dias_trabajados, datos_buscados.dias_trabajados)
        self.assertEqual(datos.vacaciones_pendientes, datos_buscados.vacaciones_pendientes)

    def test_insertar_2(self):
        """Caso normal: inserta liquidación con vacaciones, la busca y verifica que los datos coinciden"""
        datos = logica_liquidacion.DatosLiquidacion(7000, 20, 5)
        total = logica_liquidacion.calcular_liquidacion(datos)
        LiquidacionController.insertar(datos, total)

        id_insertado = LiquidacionController.obtener_ultimo_id()
        datos_buscados = LiquidacionController.buscar_por_id(id_insertado)

        self.assertEqual(datos.salario_hora, datos_buscados.salario_hora)
        self.assertEqual(datos.vacaciones_pendientes, datos_buscados.vacaciones_pendientes)

    def test_insertar_3(self):
        """Caso normal: inserta liquidación con indemnización, la busca y verifica que los datos coinciden"""
        datos = logica_liquidacion.DatosLiquidacion(6666.666667, 30, 0, True, 2000000)
        total = logica_liquidacion.calcular_liquidacion(datos)
        LiquidacionController.insertar(datos, total)

        id_insertado = LiquidacionController.obtener_ultimo_id()
        datos_buscados = LiquidacionController.buscar_por_id(id_insertado)

        self.assertEqual(datos.aplica_indemnizacion, datos_buscados.aplica_indemnizacion)
        self.assertAlmostEqual(datos.valor_indemnizacion, datos_buscados.valor_indemnizacion, places=2)

    def test_insertar_error_campo_nulo(self):
        """Caso error: insertar None en campo obligatorio lanza excepción de la base de datos"""
        datos_invalidos = logica_liquidacion.DatosLiquidacion(None, 10)
        self.assertRaises(Exception, LiquidacionController.insertar, datos_invalidos, 0)

    # ── Tests de buscar en BD ────────────────────────────────────────────────

    def test_buscar_1(self):
        """Caso normal: obtener_todas retorna una lista no vacía luego de insertar"""
        datos = logica_liquidacion.DatosLiquidacion(5000, 10)
        total = logica_liquidacion.calcular_liquidacion(datos)
        LiquidacionController.insertar(datos, total)

        registros = LiquidacionController.obtener_todas()
        self.assertIsInstance(registros, list)
        self.assertGreater(len(registros), 0)

    def test_buscar_2(self):
        """Caso normal: buscar_por_id retorna el registro correcto comparando campo a campo"""
        datos = logica_liquidacion.DatosLiquidacion(9000, 15)
        total = logica_liquidacion.calcular_liquidacion(datos)
        LiquidacionController.insertar(datos, total)

        id_insertado = LiquidacionController.obtener_ultimo_id()
        datos_buscados = LiquidacionController.buscar_por_id(id_insertado)

        self.assertIsNotNone(datos_buscados)
        self.assertEqual(datos.salario_hora, datos_buscados.salario_hora)
        self.assertEqual(datos.dias_trabajados, datos_buscados.dias_trabajados)

    def test_buscar_3(self):
        """Caso normal: cada fila de obtener_todas tiene 7 columnas (id + 6 campos)"""
        registros = LiquidacionController.obtener_todas()
        self.assertGreater(len(registros), 0)
        for fila in registros:
            self.assertEqual(len(fila), 7)

    def test_buscar_error_id_inexistente(self):
        """Caso error: buscar un id que no existe retorna None"""
        resultado = LiquidacionController.buscar_por_id(999999)
        self.assertIsNone(resultado)


if __name__ == "__main__":
    unittest.main()