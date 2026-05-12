## Ejecución del programa en Visual Studio Code

Siga estos pasos para ejecutar la aplicación:

### 1. Abrir el proyecto en VS Code
- Abra Visual Studio Code.
- Seleccione **File > Open Folder**.
- Elija la carpeta raíz del proyecto (donde se encuentra `app.py`, `src`, `build`, etc.).

### 2. Ubicar el archivo principal
El archivo que ejecuta la interfaz es:

src/view/payment_gui.py

### 3. Abrir una terminal en VS Code
- Menú: **Terminal > New Terminal**
- Verifique que esté ubicado en la raíz del proyecto.

### 4. Ejecutar el programa
Ejecute el siguiente comando en la terminal:

```bash
python src/view/payment_gui.py
Si su sistema usa python3, utilice:
python3 src/view/payment_gui.py
```
---
## Opción 1 — Interfaz de consola (sin Kivy)
 
**Paso 1 — Abrir la terminal**
 
- **Windows:** Presione `Windows + R`, escriba `cmd` y presione Enter.
- **Mac:** Presione `Cmd + Espacio`, busque Terminal y ábrala.
- **Linux:** Busque Terminal en el menú de aplicaciones.
**Paso 2 — Ir a la carpeta del proyecto**
 
Windows:
```
cd C:\Users\TuUsuario\Desktop\Calculo-de-liquidacion
```
Mac / Linux:
```
cd /Users/TuUsuario/Desktop/Calculo-de-liquidacion
```
 
**Paso 3 — Ejecutar el programa**
 
Windows:
```
python src\view\interfaz_liquidacion.py
```
Mac / Linux:
```
python3 src/view/interfaz_liquidacion.py
```
 
**Ejecutar las pruebas unitarias**
 
Windows:
```
python -m unittest discover -s tests
```
Mac / Linux:
```
python3 -m unittest discover -s tests
```
 
---
 
## Opción 2 — Interfaz gráfica (con Kivy)
 
**Paso 1 — Crear el entorno virtual**
 
Windows:
```
python -m venv kivy_venv
```
Mac / Linux:
```
python3 -m venv kivy_venv
```
 
**Paso 2 — Activar el entorno virtual**
 
Windows:
```
kivy_venv\Scripts\activate
```
Mac / Linux:
```
source kivy_venv/bin/activate
```
 
**Paso 3 — Instalar Kivy**
```
pip install kivy
```
 
**Paso 4 — Ejecutar la interfaz gráfica**
```
python app.py
```
 
---
 
## Opción 3 — APK para Android
 
El archivo `liquidacion-0.1-arm64-v8a_armeabi-v7a-debug.apk` se encuentra en la carpeta `bin/`.
 
1. Transfiera el archivo `.apk` a su dispositivo Android.
2. En su dispositivo, vaya a **Ajustes > Seguridad** y habilite **"Instalar desde fuentes desconocidas"**.
3. Abra el archivo `.apk` desde su dispositivo y siga los pasos de instalación.
