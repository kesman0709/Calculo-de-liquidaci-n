import unittest
import logica_liquidacion


class LiquidacionTest(unittest.TestCase):

    # CASOS NORMALES

    def test_normal_1(self):
        resultado = logica_liquidacion.calcular_liquidacion(6000, 30)
        self.assertEqual(round(resultado, 2), 1800000)

    def test_normal_2(self):
        resultado = logica_liquidacion.calcular_liquidacion(8000, 15)
        self.assertEqual(round(resultado, 2), 1200000)

    def test_con_vacaciones(self):
        resultado = logica_liquidacion.calcular_liquidacion(7000, 20, 5)
        self.assertEqual(round(resultado, 1750000)

    # CASOS EXTRAORDINARIOS

    def test_con_indemnizacion(self):
        resultado = logica_liquidacion.calcular_liquidacion(6666.666667, 30, 0, True, 2000000)
        self.assertEqual(round(resultado, 2), 4000000)

    def test_dias_minimos(self):
        resultado = logica_liquidacion.calcular_liquidacion(5000, 5)
        self.assertEqual(round(resultado, 2), 250000)

    def test_vacaciones_e_indemnizacion(self):
        resultado = logica_liquidacion.calcular_liquidacion(10000, 25, 10, True, 3000000)
        self.assertEqual(round(resultado, 2), 6500000)

    # CASOS DE ERROR

    def test_salario_negativo(self):
        with self.assertRaises(logica_liquidacion.SalarioInvalido):
            logica_liquidacion.calcular_liquidacion(-6666.666667, 20)

    def test_dias_fuera_de_rango(self):
        with self.assertRaises(logica_liquidacion.DiasInvalidos):
            logica_liquidacion.calcular_liquidacion(6666.666667, 35)

    def test_vacaciones_negativas(self):
        with self.assertRaises(logica_liquidacion.VacacionesInvalidas):
            logica_liquidacion.calcular_liquidacion(6666.666667, 20, -3)

    def test_indemnizacion_negativa(self):
        with self.assertRaises(logica_liquidacion.IndemnizacionInvalida):
            logica_liquidacion.calcular_liquidacion(6666.666667, 20, 0, True, -1000000)


if __name__ == "__main__":

    unittest.main()
