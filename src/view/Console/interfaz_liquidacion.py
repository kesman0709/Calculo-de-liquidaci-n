import sys
sys.path.append("src")

from model.logica_liquidacion import DatosLiquidacion, calcular_liquidacion
from model.logica_liquidacion import SalarioInvalido, DiasInvalidos, VacacionesInvalidas, IndemnizacionInvalida
from controller.liquidacion_controller import LiquidacionController

try:
    print("=== Calculo de Liquidacion ===")

    salario = float(input("Salario por hora: "))
    dias = int(input("Dias trabajados: "))
    vacaciones = int(input("Vacaciones pendientes (dias): "))

    aplica = input("Aplica indemnizacion? (s/n): ").lower()
    if aplica == "s":
        valor_indemnizacion = float(input("Valor indemnizacion: "))
        aplica_bool = True
    else:
        valor_indemnizacion = 0
        aplica_bool = False

    datos = DatosLiquidacion(
        salario_hora=salario,
        dias_trabajados=dias,
        vacaciones_pendientes=vacaciones,
        aplica_indemnizacion=aplica_bool,
        valor_indemnizacion=valor_indemnizacion
    )

    total = calcular_liquidacion(datos)
    LiquidacionController.insertar(datos, total)

    print(f"Total liquidacion: {total}")
    print("Liquidacion guardada en la base de datos.")

except SalarioInvalido as e:
    print("Error:", e)
except DiasInvalidos as e:
    print("Error:", e)
except VacacionesInvalidas as e:
    print("Error:", e)
except IndemnizacionInvalida as e:
    print("Error:", e)
except Exception as e:
    print("Error:", e)
