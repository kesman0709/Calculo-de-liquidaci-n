# Calculo-de-liquidaci-n
Desarrollado por:
Santiago Gonzalez Orrego

Kesman Posso Parra

Audio donde se explica acerca del proyecto: https://github.com/kesman0709/Calculo-de-liquidaci-n/blob/main/explicaci%C3%B3n%20del%20proyecto.m4a

Descripción: 

El sistema calcula el total a pagar a un empleado teniendo en cuenta: Salario por hora, Días trabajados, Vacaciones pendientes e Indemnización (si aplica).

Los casos de prueba fueron definidos previamente en un archivo Excel y la implementación se realizó con base en esos escenarios.

Variables de entrada:
El sistema recibe los siguientes parámetros:

salario_hora

Representa el valor monetario que se paga por cada hora trabajada.

Debe ser un número mayor que cero.

dias_trabajados

Indica la cantidad de días laborados por el empleado.

Debe estar en el rango de 1 a 30 días.

vacaciones_pendientes

Corresponde a los días de vacaciones no disfrutados que deben ser pagados al momento de la liquidación.

No puede ser un valor negativo.

Por defecto es 0.

aplica_indemnizacion

Es un valor booleano (True o False) que indica si el empleado tiene derecho a una indemnización adicional.

valor_indemnizacion

Representa el monto adicional que se suma al total si aplica indemnización.

No puede ser negativo.

Por defecto es 0.


Formula usada:

El sistema asume una jornada laboral de 10 horas por día, de acuerdo con los valores definidos en los casos de prueba.

El total se calcula de la siguiente manera:

Salario base = salario_hora × 10 × días_trabajados

Vacaciones = salario_hora × 10 × vacaciones_pendientes

Total = salario base + vacaciones + indemnización (si aplica)

Validaciones:

El sistema valida que:

El salario por hora sea mayor que cero.

Los días trabajados estén entre 1 y 30.

Las vacaciones pendientes no sean negativas.

La indemnización no sea negativa si aplica

Pruebas:

Se implementaron pruebas unitarias utilizando la librería unittest.

Las pruebas cubren: Casos normales ,Casos extraordinarios, Casos de error

Los valores esperados utilizados en las pruebas son valores fijos definidos en el archivo Excel de casos de pruebas.
