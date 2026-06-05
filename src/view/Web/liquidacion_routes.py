# Vista Web - Capa View del patron MVC
# Usa Blueprint de Flask para registrar las rutas de la aplicacion
from flask import Blueprint, render_template, request

import sys
sys.path.append("src")

from model.logica_liquidacion import (
    DatosLiquidacion,
    calcular_liquidacion,
    SalarioInvalido,
    DiasInvalidos,
    VacacionesInvalidas,
    IndemnizacionInvalida,
)
from controller.liquidacion_controller import LiquidacionController

# Se crea el blueprint indicando:
# - Nombre del Blueprint (informativo)
# - Nombre del modulo con la variable reservada __name__
# - Carpeta donde se almacenan los templates
blueprint = Blueprint("vista_liquidacion", __name__, template_folder="templates")


@blueprint.route("/")
def inicio():
    return render_template("inicio.html")


@blueprint.route("/crear_tablas")
def crear_tablas():
    LiquidacionController.crear_tabla()
    return "Tablas creadas exitosamente. Ya puede usar la aplicacion."


@blueprint.route("/liquidaciones")
def liquidaciones():
    return render_template("liquidaciones.html", total=None, datos=None, error=None)


@blueprint.route("/calcular")
def calcular():
    try:
        datos = DatosLiquidacion(
            salario_hora=float(request.args["salario_hora"]),
            dias_trabajados=int(request.args["dias_trabajados"]),
            vacaciones_pendientes=int(request.args["vacaciones_pendientes"]),
            aplica_indemnizacion=bool(int(request.args["aplica_indemnizacion"])),
            valor_indemnizacion=float(request.args["valor_indemnizacion"]),
        )
        total = calcular_liquidacion(datos)
        LiquidacionController.insertar(datos, total)
        return render_template("liquidaciones.html", total=total, datos=datos, error=None)

    except SalarioInvalido as e:
        return render_template("liquidaciones.html", total=None, datos=None, error=str(e))
    except DiasInvalidos as e:
        return render_template("liquidaciones.html", total=None, datos=None, error=str(e))
    except VacacionesInvalidas as e:
        return render_template("liquidaciones.html", total=None, datos=None, error=str(e))
    except IndemnizacionInvalida as e:
        return render_template("liquidaciones.html", total=None, datos=None, error=str(e))
    except Exception as e:
        return render_template("liquidaciones.html", total=None, datos=None, error=str(e))


@blueprint.route("/buscar_liquidacion")
def buscar_liquidacion():
    liquidacion = LiquidacionController.buscar_por_id_web(request.args["id_buscado"])
    return render_template("liquidacion_buscada.html", liquidacion=liquidacion)


@blueprint.route("/lista_liquidaciones")
def lista_liquidaciones():
    liquidaciones = LiquidacionController.obtener_todas()
    return render_template("lista_liquidaciones.html", liquidaciones=liquidaciones)
