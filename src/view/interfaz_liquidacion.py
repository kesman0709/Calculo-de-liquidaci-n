import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

import src.model.logica_liquidacion as logica_liquidacion
from src.controller.liquidacion_controller import LiquidacionController


def insertar_liquidacion():
    print("\n=== Calcular e Insertar Liquidación ===")

    salario = float(input("Salario por hora: "))
    dias = int(input("Días trabajados: "))
    vacaciones = int(input("Vacaciones pendientes: "))

    aplica = input("¿Aplica indemnización? (s/n): ").lower() == "s"

    valor_indemnizacion = (
        float(input("Valor indemnización: "))
        if aplica else 0
    )

    datos = logica_liquidacion.DatosLiquidacion(
        salario_hora=salario,
        dias_trabajados=dias,
        vacaciones_pendientes=vacaciones,
        aplica_indemnizacion=aplica,
        valor_indemnizacion=valor_indemnizacion
    )

    total = logica_liquidacion.calcular_liquidacion(datos)

    LiquidacionController.insertar(datos, total)

    print(f"\nTotal liquidación: {total}")
    print("Liquidación guardada correctamente.")


def mostrar_liquidaciones():
    print("\n=== Liquidaciones Guardadas ===")

    registros = LiquidacionController.obtener_todas()

    if not registros:
        print("No hay registros.")
        return

    encabezado = (
        f"{'ID':<5} {'Salario':<10} {'Días':<6} "
        f"{'Vac':<5} {'Indemn':<8} {'Valor':<10} {'Total'}"
    )

    print(encabezado)
    print("-" * len(encabezado))

    for r in registros:
        print(
            f"{r[0]:<5} "
            f"{float(r[1]):<10.0f} "
            f"{r[2]:<6} "
            f"{r[3]:<5} "
            f"{'Sí' if r[4] else 'No':<8} "
            f"{float(r[5]):<10.0f} "
            f"{float(r[6]):.0f}"
        )


def manejar_errores(funcion):
    try:
        funcion()

    except (
        logica_liquidacion.SalarioInvalido,
        logica_liquidacion.DiasInvalidos,
        logica_liquidacion.VacacionesInvalidas,
        logica_liquidacion.IndemnizacionInvalida
    ) as e:
        print("Error:", e)

    except Exception as e:
        print("Error inesperado:", e)


def menu():
    opciones = {
        "1": insertar_liquidacion,
        "2": mostrar_liquidaciones
    }

    while True:
        print("\n=== Calculadora de Liquidación ===")
        print("1. Calcular e insertar liquidación")
        print("2. Ver liquidaciones guardadas")
        print("3. Salir")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "3":
            print("Hasta luego.")
            break

        funcion = opciones.get(opcion)

        if funcion:
            manejar_errores(funcion)
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    menu()