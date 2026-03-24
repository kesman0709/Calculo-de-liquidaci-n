from dataclasses import dataclass

# Constante
HORAS_POR_DIA = 10


class SalarioInvalido(Exception):
    """Se lanza cuando el salario es menor o igual a cero"""


class DiasInvalidos(Exception):
    """Se lanza cuando los días no están entre 1 y 30"""


class VacacionesInvalidas(Exception):
    """Se lanza cuando las vacaciones son negativas"""


class IndemnizacionInvalida(Exception):
    """Se lanza cuando la indemnización es negativa"""


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
        raise SalarioInvalido(f"salario_hora inválido: {salario_hora}")


def validar_dias(dias_trabajados):
    if dias_trabajados <= 0 or dias_trabajados > 30:
        raise DiasInvalidos(f"dias_trabajados inválidos: {dias_trabajados}")


def validar_vacaciones(vacaciones_pendientes):
    if vacaciones_pendientes < 0:
        raise VacacionesInvalidas(
            f"vacaciones_pendientes inválidas: {vacaciones_pendientes}"
        )


def validar_indemnizacion(aplica, valor):
    if aplica and valor < 0:
        raise IndemnizacionInvalida(f"valor_indemnizacion inválido: {valor}")


# CÁLCULOS
def calcular_salario_base(salario_hora, dias_trabajados):
    return salario_hora * HORAS_POR_DIA * dias_trabajados


def calcular_vacaciones(salario_hora, vacaciones_pendientes):
    return salario_hora * HORAS_POR_DIA * vacaciones_pendientes


def aplicar_indemnizacion(total, valor_indemnizacion):
    return total + valor_indemnizacion


# FUNCIÓN PRINCIPAL
def calcular_liquidacion(datos: DatosLiquidacion) -> float:
    """
    Calcula el total de la liquidación de un empleado.

    Args:
        datos (DatosLiquidacion): Información necesaria para el cálculo.

    Returns:
        float: Total de la liquidación.

    Raises:
        SalarioInvalido: Si el salario es <= 0
        DiasInvalidos: Si los días no están entre 1 y 30
        VacacionesInvalidas: Si las vacaciones son negativas
        IndemnizacionInvalida: Si la indemnización es negativa
    """

    # Validaciones
    validar_salario(datos.salario_hora)
    validar_dias(datos.dias_trabajados)
    validar_vacaciones(datos.vacaciones_pendientes)
    validar_indemnizacion(
        datos.aplica_indemnizacion, datos.valor_indemnizacion
    )

    # Cálculos
    total_base = calcular_salario_base(
        datos.salario_hora, datos.dias_trabajados
    )
    total_vacaciones = calcular_vacaciones(
        datos.salario_hora, datos.vacaciones_pendientes
    )

    total = total_base + total_vacaciones

    # Indemnización
    if datos.aplica_indemnizacion:
        total = aplicar_indemnizacion(total, datos.valor_indemnizacion)

    return total