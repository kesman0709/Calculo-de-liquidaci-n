# 💼 Calculadora de Liquidación Laboral - Web

Una aplicación web para calcular el total a pagar a un empleado al momento de su liquidación, teniendo en cuenta el salario por hora, días trabajados, vacaciones pendientes e indemnización.

---

## 👥 Desarrolladores

**Backend & Lógica:**
- Santiago Gonzalez Orrego
- Kesman Posso Parra

**Interfaz Web:**
- Maria Paula Ospina
- Manolo Restrepo

**Documentación:** [Audio de explicación del proyecto](https://github.com/kesman0709/Calculo-de-liquidaci-n/blob/main/explicaci%C3%B3n%20del%20proyecto.m4a)

---

## 📋 Descripción del Proyecto

La **Calculadora de Liquidación Laboral** es una aplicación web diseñada para automatizar el cálculo preciso de liquidaciones laborales. El sistema permite:

- ✅ Ingresar el salario por hora y días trabajados
- ✅ Incluir vacaciones pendientes no disfrutadas
- ✅ Aplicar indemnización adicional cuando corresponda
- ✅ Obtener el total a pagar de forma inmediata
- ✅ Persistencia de datos en base de datos PostgreSQL

---

## 🚀 Instalación y Ejecución

### Prerrequisitos

Antes de comenzar, asegúrese de tener lo siguiente instalado:

1. **Python 3.8 o superior** - Descargue desde https://www.python.org/downloads/
   - En Windows, marque la casilla **"Add Python to PATH"** durante la instalación

2. **Git** - Descargue desde https://git-scm.com/downloads

3. **PostgreSQL** (opcional, para persistencia de datos)
   - Local: https://www.postgresql.org/download/
   - Cloud gratuito: https://render.com o https://neon.tech

---

## 📦 Opción 1: Ejecución Local sin Base de Datos

Ideal para pruebas rápidas sin persistencia.

### Paso 1 — Clonar o descargar el proyecto

```bash
git clone https://github.com/kesman0709/Calculo-de-liquidaci-n.git
cd Calculo-de-liquidaci-n
```

### Paso 2 — Crear un entorno virtual

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Mac / Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### Paso 3 — Instalar dependencias

```bash
pip install flask
```

### Paso 4 — Ejecutar la aplicación

```bash
python app.py
```

**Resultado esperado:**
```
 * Serving Flask app 'app'
 * Debug mode: on
 * Running on http://127.0.0.1:5000
```

### Paso 5 — Acceder a la aplicación

Abra su navegador web e ingrese:
```
http://localhost:5000
```

---

## 🗄️ Opción 2: Ejecución con Base de Datos PostgreSQL

Para persistencia y gestión de datos históricos.

### Paso 1 — Completar los pasos 1-3 de la Opción 1

```bash
git clone https://github.com/kesman0709/Calculo-de-liquidaci-n.git
cd Calculo-de-liquidaci-n
python -m venv venv
# Activar venv (ver Opción 1, Paso 2)
```

### Paso 2 — Instalar dependencias con PostgreSQL

```bash
pip install flask psycopg2-binary
```

### Paso 3 — Configurar la conexión a la base de datos

1. Copie el archivo de configuración de ejemplo:

**Windows:**
```bash
copy secret_config_sample.py secret_config.py
```

**Mac / Linux:**
```bash
cp secret_config_sample.py secret_config.py
```

2. Abra `secret_config.py` y complete con sus credenciales:

```python
PGHOST='su-host.render.com'      # Host de PostgreSQL
PGDATABASE='nombre_de_su_bd'     # Nombre de la base de datos
PGUSER='su_usuario'              # Usuario de PostgreSQL
PGPASSWORD='su_contrasena'       # Contraseña
PGPORT=5432                      # Puerto (por defecto 5432)
```

> ⚠️ **Importante:** `secret_config.py` está en `.gitignore` y **nunca debe subirse al repositorio**.

### Paso 4 — Crear la tabla de liquidaciones

Ejecute el script SQL para crear la tabla:

**Windows:**
```bash
# Acceder a PostgreSQL
psql -h <PGHOST> -U <PGUSER> -d <PGDATABASE>
# Luego ejecutar el contenido de sql/crear-liquidaciones.sql
```

**Mac / Linux:**
```bash
psql -h <PGHOST> -U <PGUSER> -d <PGDATABASE> < sql/crear-liquidaciones.sql
```

O ejecute las pruebas unitarias (crean la tabla automáticamente):

```bash
python -m pytest tests/ -v
```

### Paso 5 — Ejecutar la aplicación

```bash
python app.py
```

Acceda a la aplicación en: http://localhost:5000

---

## 🧪 Ejecución de Pruebas Unitarias

Las pruebas validan toda la lógica de cálculo:

```bash
# Con unittest
python -m unittest discover -s tests

# Con pytest (recomendado)
pip install pytest
python -m pytest tests/ -v
```

**Resultado esperado:** Todos los tests en verde ✅

---

## 📊 Estructura del Proyecto

```
Calculo-de-liquidaci-n/
├── app.py                          # Aplicación principal Flask
├── requirements.txt                # Dependencias del proyecto
├── secret_config_sample.py         # Plantilla de configuración DB (sin datos privados)
│
├── src/
│   ├── model/
│   │   └── logica_liquidacion.py   # Lógica de cálculo y validaciones
│   ├── controller/
│   │   └── liquidacion_controller.py # Operaciones con la base de datos
│   └── view/
│       ├── Web/
│       │   ├── liquidacion_routes.py # Rutas de la aplicación web
│       │   └── (templates HTML)
│       └── templates/
│           └── (archivos HTML)
│
├── sql/
│   ├── crear-liquidaciones.sql     # Script para crear tabla
│   └── borrar-liquidaciones.sql    # Script para eliminar tabla
│
├── tests/
│   └── test_liquidacion.py         # Pruebas unitarias
│
└── README.md                       # Este archivo
```

---

## 📥 Entradas del Sistema

El usuario debe ingresar en la interfaz web:

| Campo | Descripción | Validación |
|-------|-------------|-----------|
| **Salario por hora** | Valor monetario por hora trabajada | Mayor que 0 |
| **Días trabajados** | Cantidad de días laborados | Entre 1 y 30 |
| **Vacaciones pendientes** | Días de vacaciones no disfrutados | ≥ 0 (opcional) |
| **¿Aplica indemnización?** | ¿Tiene derecho a indemnización? | Sí/No |
| **Valor indemnización** | Monto adicional a sumar | ≥ 0 (si aplica) |

---

## 🧮 Proceso de Cálculo

El sistema asume una **jornada laboral de 10 horas por día**.

```
Salario base   = salario_hora × 10 × días_trabajados
Vacaciones     = salario_hora × 10 × vacaciones_pendientes
Indemnización  = valor_indemnización (si aplica)

TOTAL A PAGAR  = Salario base + Vacaciones + Indemnización
```

### Ejemplo:
```
Salario por hora:      $15.000
Días trabajados:       15
Vacaciones pendientes: 3
Indemnización:         $50.000

Salario base   = $15.000 × 10 × 15 = $2.250.000
Vacaciones     = $15.000 × 10 × 3  = $450.000
Indemnización  = $50.000

TOTAL          = $2.750.000
```

---

## ⚠️ Validaciones y Mensajes de Error

El sistema valida los datos y muestra errores específicos:

| Error | Mensaje | Solución |
|-------|---------|----------|
| `SalarioInvalido` | "salario_hora inválido: {valor}" | Ingrese un valor mayor a 0 |
| `DiasInvalidos` | "dias_trabajados inválidos: {valor}" | Ingrese entre 1 y 30 días |
| `VacacionesInvalidas` | "vacaciones_pendientes inválidas: {valor}" | Ingrese un valor ≥ 0 |
| `IndemnizacionInvalida` | "valor_indemnizacion inválido: {valor}" | Ingrese un valor ≥ 0 |

---

## 📤 Salidas del Sistema

La aplicación muestra:

- **Total a pagar:** Suma final del salario base, vacaciones e indemnización
- **Desglose:** Valores parciales de cada concepto
- **Validaciones:** Mensajes de error si los datos son inválidos

---

## 🌐 Variables de Entorno (Avanzado)

Si prefiere usar variables de entorno en lugar de `secret_config.py`:

**Windows (CMD):**
```bash
set PGHOST=su-host.render.com
set PGDATABASE=nombre_de_su_bd
set PGUSER=su_usuario
set PGPASSWORD=su_contrasena
set PGPORT=5432
python app.py
```

**Mac / Linux (Bash):**
```bash
export PGHOST=su-host.render.com
export PGDATABASE=nombre_de_su_bd
export PGUSER=su_usuario
export PGPASSWORD=su_contrasena
export PGPORT=5432
python app.py
```

---

## 🐛 Solución de Problemas

### "ModuleNotFoundError: No module named 'flask'"
```bash
pip install flask
```

### "psycopg2: Connection refused"
- Verifique que PostgreSQL esté ejecutándose
- Verifique credenciales en `secret_config.py`
- Revise que PGHOST y PGPORT sean correctos

### Puerto 5000 ya está en uso
```bash
# Encontrar el proceso usando el puerto y terminarlo
# O ejecutar en otro puerto:
python app.py --port 5001
```

### "Template not found"
- Verifique que la carpeta `src/templates/` exista
- Asegúrese de estar en el directorio raíz del proyecto

---

## 📚 Archivos de Referencia

- **Casos de prueba:** `Casos de prueba - liquidación.xlsx`
- **Especificación de empaquetado:** `app.spec`
- **Audio explicativo:** `explicación del proyecto.m4a`

---

## 📝 Notas Importantes

- 🔐 **Nunca** suba `secret_config.py` al repositorio
- ✅ Ejecute siempre las pruebas antes de hacer cambios
- 🌍 Para acceso remoto, configure Flask con un host público:
  ```python
  app.run(host='0.0.0.0', debug=True)
  ```
- 📱 Asegúrese de que el firewall permita conexiones al puerto 5000

---

## 🤝 Contribuciones

Para contribuir al proyecto:

1. Cree una rama con sus cambios: `git checkout -b feature/mi-funcionalidad`
2. Commit de cambios: `git commit -m 'Agregar nueva funcionalidad'`
3. Push a la rama: `git push origin feature/mi-funcionalidad`
4. Abra un Pull Request

---

## 📄 Licencia

Este proyecto es un trabajo académico desarrollado como proyecto de clase.

---

## 📧 Contacto

Para preguntas o sugerencias, abra un issue en el repositorio:
https://github.com/kesman0709/Calculo-de-liquidaci-n/issues

---

**Última actualización:** Junio 2026
