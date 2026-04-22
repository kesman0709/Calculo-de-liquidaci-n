# Calculo-de-liquidaci-n
### Desarrollado por:

Santiago Gonzalez Orrego

Kesman Posso Parra

Audio donde se explica acerca del proyecto: https://github.com/kesman0709/Calculo-de-liquidaci-n/blob/main/explicaci%C3%B3n%20del%20proyecto.m4a

### Interfaz gráfica desarrollada por:

Maria Paula Ospina

Manolo Restrepo

---
 
##  Descripción del Proyecto
 
La Calculadora de Liquidación Laboral es una aplicación diseñada para calcular el total a pagar a un empleado al momento de su liquidación. El sistema tiene en cuenta el salario por hora, los días trabajados, las vacaciones pendientes y, si aplica, una indemnización adicional. Los casos de prueba fueron definidos previamente en un archivo Excel y la implementación se realizó con base en esos escenarios.
 
---

 
##  Objetivo
 
Esta herramienta busca facilitar el cálculo preciso y automatizado de una liquidación laboral, permitiendo:
 
- Ingresar el salario por hora y los días trabajados.
- Incluir vacaciones pendientes no disfrutadas.
- Aplicar una indemnización adicional cuando corresponda.
- Obtener el total a pagar de forma inmediata y confiable.
---
 
## ▶️ Funcionamiento
 
### Prerrequisitos
 
Antes de comenzar, asegúrese de tener lo siguiente:
 
- **Python 3** instalado en su computador. Si no lo tiene, descárguelo desde https://www.python.org/downloads/
  >  En Windows, durante la instalación marque la casilla **"Add Python to PATH"**
- La carpeta del proyecto descargada en su computador (`Calculo-de-liquidacion`)
---
 
###  Opción 1 — Desde la terminal (CMD / Bash)
 
**Paso 1 — Abrir la terminal**
 
- **Windows:** Presione `Windows + R`, escriba `cmd` y presione Enter.
- **Mac:** Presione `Cmd + Espacio`, busque Terminal y ábrala.
- **Linux:** Busque Terminal en el menú de aplicaciones.
**Paso 2 — Ir a la carpeta del proyecto**
 
Escriba `cd` seguido de la ruta donde guardó el proyecto. Por ejemplo:
 
Windows:
```
cd C:\Users\TuUsuario\Desktop\Calculo-de-liquidacion
```
 
Mac / Linux:
```
cd /Users/TuUsuario/Desktop/Calculo-de-liquidacion
```
 
>  **Tip:** Puede arrastrar la carpeta del proyecto hacia la ventana de la terminal y la ruta aparecerá automáticamente.
 
**Paso 3 — Ejecutar el programa**
 
Windows:
```
python src\view\interfaz_liquidacion.py
```
 
Mac / Linux:
```
python3 src/view/interfaz_liquidacion.py
```
 
Si todo está bien, verá la interfaz del programa en pantalla.
 
**Ejecutar las pruebas unitarias**
 
Windows:
```
python -m unittest discover -s tests
```
 
Mac / Linux:
```
python3 -m unittest discover -s tests
```
 
Si las pruebas pasaron correctamente, verá un mensaje con `passed` en verde. Si alguna falló, verá `FAILED` en rojo con una descripción del error.
 
---
 
###  Opción 2 — Desde un entorno de desarrollo (VS Code, PyCharm, etc.)
 
**Paso 1 — Abrir el proyecto**
 
Abra su entorno de desarrollo y seleccione la opción "Abrir carpeta" (o *Open Folder*). Busque y seleccione la carpeta `Calculo-de-liquidacion`.
 
**Paso 2 — Seleccionar el intérprete de Python**
 
Asegúrese de que su entorno tenga configurado Python 3 como intérprete.
 
- **VS Code:** Presione `Ctrl + Shift + P`, busque *"Python: Select Interpreter"* y elija la versión de Python 3 instalada en su equipo.
- **PyCharm:** Vaya a *File > Settings > Project > Python Interpreter* y seleccione Python 3.
**Paso 3 — Ejecutar el programa**
 
Abra el archivo `src/view/interfaz_liquidacion.py` y ejecútelo:
 
- **VS Code:** Presione el botón ▶️ en la esquina superior derecha, o haga clic derecho sobre el archivo y seleccione *"Run Python File"*.
- **PyCharm:** Presione el botón ▶️ en la esquina superior derecha, o haga clic derecho y seleccione *"Run"*.
**Ejecutar las pruebas unitarias**
 
Abra el archivo `tests/test_liquidacion.py` y ejecútelo de la misma forma que el paso anterior.
 
>  También puede ejecutar las pruebas desde la terminal integrada del entorno (*View > Terminal*) usando el mismo comando de la Opción 1.
 
---

##  Entradas del Sistema
 
El usuario debe ingresar:
 
- **Salario por hora** (`salario_hora`): Valor monetario pagado por cada hora trabajada. Debe ser mayor que cero.
- **Días trabajados** (`dias_trabajados`): Cantidad de días laborados. Debe estar entre 1 y 30.
- **Vacaciones pendientes** (`vacaciones_pendientes`): Días de vacaciones no disfrutados a pagar. No puede ser negativo. Por defecto es 0.
- **Aplica indemnización** (`aplica_indemnizacion`): Valor booleano que indica si el empleado tiene derecho a indemnización adicional.
- **Valor indemnización** (`valor_indemnizacion`): Monto adicional a sumar si aplica indemnización. No puede ser negativo. Por defecto es 0.
---
 
##  Proceso del Sistema
 
El sistema asume una jornada laboral de **10 horas por día**, de acuerdo con los valores definidos en los casos de prueba.
 
El total se calcula de la siguiente manera:
 
```
Salario base   = salario_hora × 10 × días_trabajados
Vacaciones     = salario_hora × 10 × vacaciones_pendientes
Total          = salario base + vacaciones + indemnización (si aplica)
```
 
---
 
##  Validaciones
 
El sistema valida que:
 
- El salario por hora sea mayor que cero.
- Los días trabajados estén entre 1 y 30.
- Las vacaciones pendientes no sean negativas.
- El valor de la indemnización no sea negativo si aplica.
---

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
