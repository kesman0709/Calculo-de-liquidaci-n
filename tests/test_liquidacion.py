from src.model import logica_liquidacion
import unittest


class LiquidacionTest(unittest.TestCase):

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


if __name__ == "_main_":
    unittest.main()