from dataclasses import dataclass

# Constante
HORAS_POR_DIA = 10


class SalarioInvalido(Exception):
    """Se lanza cuando el salario es menor o igual a cero"""


class DiasInvalidos(Exception):
    """Se lanza cuando los dias no estan entre 1 y 30"""


class VacacionesInvalidas(Exception):
    """Se lanza cuando las vacaciones son negativas"""


class IndemnizacionInvalida(Exception):
    """Se lanza cuando la indemnizacion es negativa"""


@dataclass
class DatosLiquidacion:
    salario_hora: float
    dias_trabajados: int
    vacaciones_pendientes: int = 0
    aplica_indemnizacion: bool = False
    valor_indemnizacion: float = 0


# VALIDACIONES
def validar_salario(salario_hora):
    if salario_hora <= 0:
        raise SalarioInvalido(f"salario_hora invalido: {salario_hora}")


def validar_dias(dias_trabajados):
    if dias_trabajados <= 0 or dias_trabajados > 30:
        raise DiasInvalidos(f"dias_trabajados invalidos: {dias_trabajados}")


def validar_vacaciones(vacaciones_pendientes):
    if vacaciones_pendientes < 0:
        raise VacacionesInvalidas(
            f"vacaciones_pendientes invalidas: {vacaciones_pendientes}"
        )


def validar_indemnizacion(aplica, valor):
    if aplica and valor < 0:
        raise IndemnizacionInvalida(f"valor_indemnizacion invalido: {valor}")


# CALCULOS
def calcular_salario_base(salario_hora, dias_trabajados):
    return salario_hora * HORAS_POR_DIA * dias_trabajados


def calcular_vacaciones(salario_hora, vacaciones_pendientes):
    return salario_hora * HORAS_POR_DIA * vacaciones_pendientes


def aplicar_indemnizacion(total, valor_indemnizacion):
    return total + valor_indemnizacion


# FUNCION PRINCIPAL
def calcular_liquidacion(datos: DatosLiquidacion) -> float:
    """
    Calcula el total de la liquidacion de un empleado.

    Args:
        datos (DatosLiquidacion): Informacion necesaria para el calculo.

    Returns:
        float: Total de la liquidacion.

    Raises:
        SalarioInvalido: Si el salario es <= 0
        DiasInvalidos: Si los dias no estan entre 1 y 30
        VacacionesInvalidas: Si las vacaciones son negativas
        IndemnizacionInvalida: Si la indemnizacion es negativa
    """

    validar_salario(datos.salario_hora)
    validar_dias(datos.dias_trabajados)
    validar_vacaciones(datos.vacaciones_pendientes)
    validar_indemnizacion(datos.aplica_indemnizacion, datos.valor_indemnizacion)

    total_base = calcular_salario_base(datos.salario_hora, datos.dias_trabajados)
    total_vacaciones = calcular_vacaciones(datos.salario_hora, datos.vacaciones_pendientes)

    total = total_base + total_vacaciones

    if datos.aplica_indemnizacion:
        total = aplicar_indemnizacion(total, datos.valor_indemnizacion)

    return total
