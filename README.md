# 🔄 Renombrador de Archivos

Script en Python para renombrar archivos en un directorio de forma masiva, añadiendo un prefijo personalizado y un número secuencial a cada archivo.

## 📋 Tabla de Contenidos

- [Características](#-características)
- [Requisitos](#-requisitos)
- [Instalación](#-instalación)
- [Configuración](#-configuración)
- [Uso](#-uso)
- [Estructura del Proyecto](#-estructura-del-proyecto)
- [Ejemplos](#-ejemplos)
- [Solución de Problemas](#-solución-de-problemas)
- [Buenas Prácticas](#-buenas-prácticas)

## ✨ Características

- ✅ Renombrado masivo de archivos con prefijo personalizado
- ✅ Numeración secuencial automática
- ✅ Preservación de extensiones de archivo
- ✅ Validaciones exhaustivas antes de renombrar
- ✅ Manejo de errores robusto
- ✅ Configuración mediante variables de entorno (.env)
- ✅ Mensajes claros y descriptivos con emojis
- ✅ Filtrado automático de subdirectorios
- ✅ Detección de nombres duplicados
- ✅ Resumen detallado del proceso

## 🔧 Requisitos

- Python 3.9 o superior
- pip (gestor de paquetes de Python)
- Pipenv (opcional, pero recomendado)

## 📦 Instalación

### Opción 1: Usando Pipenv (Recomendado)

```bash
# 1. Clonar o descargar el proyecto
cd ruta/al/proyecto

# 2. Instalar Pipenv si no lo tienes
pip install pipenv

# 3. Instalar dependencias
pipenv install

# 4. Activar el entorno virtual
pipenv shell
```

### Opción 2: Usando pip tradicional

```bash
# 1. Clonar o descargar el proyecto
cd ruta/al/proyecto

# 2. Instalar dependencias
pip install -r requirements.txt
```

### Dependencias

El proyecto utiliza las siguientes librerías:

```txt
python-dotenv==1.2.1
```

**Importante:** Solo debes usar `python-dotenv`. El paquete `dotenv` (sin "python-") es diferente y obsoleto.

## ⚙️ Configuración

### 1. Crear el archivo .env

Crea un archivo llamado `.env` en el directorio raíz del proyecto con el siguiente contenido:

```env
MY_DIRECTORY_PATH=C:/Users/tu_usuario/ruta/a/la/carpeta
PREFIX=mi_prefijo
```

**Reglas importantes para el archivo .env:**

- ❌ **NO** uses espacios alrededor del signo `=`
- ✅ Usa barras normales `/` o dobles barras invertidas `\\`
- ✅ No uses comillas a menos que sean parte del valor
- ✅ No dejes líneas vacías al inicio del archivo

**Ejemplos válidos:**

```env
# ✅ CORRECTO - Barras normales
MY_DIRECTORY_PATH=C:/Users/vic_s/Desktop/mis_archivos
PREFIX=video

# ✅ CORRECTO - Barras invertidas dobles
MY_DIRECTORY_PATH=C:\\Users\\vic_s\\Desktop\\mis_archivos
PREFIX=documento

# ✅ CORRECTO - Ruta con espacios
MY_DIRECTORY_PATH=C:/Users/vic_s/Desktop/carpeta con espacios
PREFIX=archivo_renombrado
```

**Ejemplos incorrectos:**

```env
# ❌ INCORRECTO - Espacios alrededor del =
MY_DIRECTORY_PATH = C:/Users/vic_s/Desktop/mis_archivos

# ❌ INCORRECTO - Barras simples sin escapar
MY_DIRECTORY_PATH=C:\Users\vic_s\Desktop\mis_archivos

# ❌ INCORRECTO - Comillas innecesarias
MY_DIRECTORY_PATH='C:/Users/vic_s/Desktop/mis_archivos'
```

### 2. Crear el archivo .gitignore

Para proteger tu información sensible, crea un archivo `.gitignore`:

```gitignore
# Variables de entorno
.env

# Cache de Python
__pycache__/
*.pyc
*.pyo
*.pyd
.Python

# Entornos virtuales
venv/
env/
ENV/
.venv

# IDEs
.vscode/
.idea/
*.swp
*.swo

# Pipenv
Pipfile.lock
```

## 🚀 Uso

### Método 1: Con Pipenv

```bash
# Activar el entorno virtual
pipenv shell

# Ejecutar el script
python cambiarNombre.py

# O ejecutar directamente sin activar el entorno
pipenv run python cambiarNombre.py
```

### Método 2: Con Python tradicional

```bash
python cambiarNombre.py
```

### Flujo del Programa

1. **Carga de configuración**: Lee las variables del archivo `.env`
2. **Validaciones**: Verifica que el directorio existe y contiene archivos
3. **Listado**: Muestra cuántos archivos se encontraron
4. **Renombrado**: Procesa cada archivo y muestra el progreso
5. **Resumen**: Presenta estadísticas del proceso (éxitos y errores)

## 📁 Estructura del Proyecto

```
cambioNombre/
│
├── .env                    # Variables de entorno (NO subir a git)
├── .env.example           # Plantilla de ejemplo para .env
├── .gitignore             # Archivos a ignorar en git
├── Pipfile                # Configuración de Pipenv
├── Pipfile.lock          # Dependencias bloqueadas
├── requirements.txt       # Dependencias (para pip tradicional)
├── README.md              # Este archivo
│
├── config.py              # Carga de variables de entorno
├── cambiarNombre.py       # Script principal
│
└── carpeta_de_pruebas/    # Carpeta de ejemplo con archivos
    ├── archivo1.txt
    ├── archivo2.jpg
    └── archivo3.pdf
```

## 💡 Ejemplos

### Ejemplo 1: Renombrar videos

**Configuración (.env):**
```env
MY_DIRECTORY_PATH=C:/Users/vic_s/Videos/vacaciones
PREFIX=vacaciones_2024
```

**Antes:**
```
vacaciones/
├── IMG_001.mp4
├── IMG_002.mp4
└── IMG_003.mp4
```

**Después:**
```
vacaciones/
├── vacaciones_2024_0.mp4
├── vacaciones_2024_1.mp4
└── vacaciones_2024_2.mp4
```

### Ejemplo 2: Renombrar documentos

**Configuración (.env):**
```env
MY_DIRECTORY_PATH=C:/Users/vic_s/Documents/facturas
PREFIX=factura
```

**Antes:**
```
facturas/
├── scan001.pdf
├── scan002.pdf
├── documento.pdf
└── archivo.xlsx
```

**Después:**
```
facturas/
├── factura_0.pdf
├── factura_1.pdf
├── factura_2.pdf
└── factura_3.xlsx
```

### Ejemplo 3: Salida del programa

```
============================================================
DEBUG - config.py cargado
============================================================
my_directory_path = 'C:/Users/vic_s/Desktop/carpeta_de_pruebas'
my_prefix = 'megustaelbrocoli'
============================================================

============================================================
🔄 RENOMBRADOR DE ARCHIVOS
============================================================

📋 Configuración:
   Directorio: C:/Users/vic_s/Desktop/carpeta_de_pruebas
   Prefijo: megustaelbrocoli

🚀 Iniciando proceso de renombrado...

📁 Se encontraron 3 archivo(s) para renombrar.

✅ Renombrado: 'sddxsd.txt' → 'megustaelbrocoli_0.txt'
✅ Renombrado: 'sdfsd.txt' → 'megustaelbrocoli_1.txt'
✅ Renombrado: 'sdvsdf.txt' → 'megustaelbrocoli_2.txt'

==================================================
✨ Proceso completado:
   • Archivos renombrados: 3
   • Errores: 0
==================================================

🎉 ¡Operación finalizada con éxito!

Presiona Enter para salir...
```

## 🔍 Solución de Problemas

### Error: "MY_DIRECTORY_PATH es None"

**Causa:** El archivo `.env` no existe o tiene errores de sintaxis.

**Solución:**
1. Verifica que existe el archivo `.env` en el directorio raíz
2. Abre `.env` y verifica que contenga:
   ```env
   MY_DIRECTORY_PATH=C:/tu/ruta/aqui
   PREFIX=tu_prefijo
   ```
3. Asegúrate de que no hay espacios alrededor del `=`
4. Usa barras `/` o dobles barras `\\`

### Error: "No se encontraron archivos en el directorio"

**Causa:** El directorio está vacío o solo contiene subdirectorios.

**Solución:**
1. Verifica que la ruta en `.env` es correcta
2. Asegúrate de que el directorio contiene archivos (no solo carpetas)
3. El script solo renombra archivos, no subdirectorios

### Error: "ModuleNotFoundError: No module named 'dotenv'"

**Causa:** El paquete `python-dotenv` no está instalado.

**Solución:**
```bash
# Con Pipenv
pipenv install python-dotenv

# Con pip tradicional
pip install python-dotenv
```

### Error: "El archivo 'X' ya existe"

**Causa:** Ya existe un archivo con el nombre que se intenta asignar.

**Solución:**
1. El script automáticamente salta estos archivos para evitar sobrescrituras
2. Puedes eliminar o renombrar manualmente los archivos duplicados
3. O cambiar el prefijo en el archivo `.env`

### Error: "Sin permisos para renombrar"

**Causa:** El archivo está siendo usado por otro programa o no tienes permisos.

**Solución:**
1. Cierra cualquier programa que esté usando los archivos
2. Ejecuta el script como administrador (click derecho → "Ejecutar como administrador")
3. Verifica los permisos de la carpeta

### Conflicto con paquete 'dotenv'

**Problema:** Tienes instalado `dotenv` y `python-dotenv` simultáneamente.

**Solución:**
```bash
# Desinstalar el paquete incorrecto
pip uninstall dotenv -y

# Asegurar que solo está python-dotenv
pip install python-dotenv
```

## 🛡️ Buenas Prácticas

### 1. Hacer copias de seguridad

**Antes de renombrar archivos importantes, haz una copia de seguridad:**

```bash
# En Windows (PowerShell)
Copy-Item -Path "C:\ruta\original" -Destination "C:\ruta\backup" -Recurse

# En Linux/Mac
cp -r /ruta/original /ruta/backup
```

### 2. Probar primero con archivos de prueba

Crea una carpeta de prueba con archivos de ejemplo antes de usar el script en archivos importantes:

```bash
mkdir carpeta_de_pruebas
cd carpeta_de_pruebas
# Crear archivos de prueba
echo . > test1.txt
echo . > test2.jpg
echo . > test3.pdf
```

### 3. Usar control de versiones

Si trabajas con código, usa Git para rastrear cambios:

```bash
git init
git add .
git commit -m "Initial commit"
```

**Importante:** Nunca subas el archivo `.env` a repositorios públicos.

### 4. Variables de entorno por proyecto

Si trabajas con múltiples proyectos, cada uno debe tener su propio archivo `.env`:

```
proyecto1/
├── .env          # Configuración específica del proyecto 1
└── ...

proyecto2/
├── .env          # Configuración específica del proyecto 2
└── ...
```

### 5. Documentar cambios importantes

Si modificas el script, documenta los cambios:

```python
# Versión 1.1 - 2025-10-26
# - Agregada validación de nombres duplicados
# - Mejorados mensajes de error
```

## 🔧 Personalización

### Cambiar el formato de numeración

Si quieres cambiar el formato del número (por ejemplo, añadir ceros a la izquierda):

```python
# En cambiarNombre.py, línea ~60
# Formato original:
new_name = f'{prefix}_{counter}{extension}'

# Con ceros a la izquierda (3 dígitos):
new_name = f'{prefix}_{counter:03d}{extension}'
# Resultado: archivo_001.txt, archivo_002.txt, archivo_003.txt

# Con ceros a la izquierda (4 dígitos):
new_name = f'{prefix}_{counter:04d}{extension}'
# Resultado: archivo_0001.txt, archivo_0002.txt, archivo_0003.txt
```

### Cambiar el separador

Si quieres usar un separador diferente al guion bajo:

```python
# Guion: archivo-0.txt
new_name = f'{prefix}-{counter}{extension}'

# Espacio: archivo 0.txt
new_name = f'{prefix} {counter}{extension}'

# Sin separador: archivo0.txt
new_name = f'{prefix}{counter}{extension}'
```

### Ordenar archivos antes de renombrar

Si quieres que los archivos se renombren en un orden específico:

```python
# Ordenar alfabéticamente
files.sort()

# Ordenar por fecha de modificación (más antiguos primero)
files.sort(key=lambda x: os.path.getmtime(os.path.join(directory_path, x)))

# Ordenar por fecha de modificación (más recientes primero)
files.sort(key=lambda x: os.path.getmtime(os.path.join(directory_path, x)), reverse=True)

# Ordenar por tamaño
files.sort(key=lambda x: os.path.getsize(os.path.join(directory_path, x)))
```

## 📝 Licencia

Este proyecto es de código abierto y está disponible para uso personal y educativo.

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Si encuentras un error o tienes una sugerencia:

1. Crea un issue describiendo el problema o la mejora
2. Haz un fork del proyecto
3. Crea una rama para tu feature (`git checkout -b feature/nueva-funcionalidad`)
4. Commit tus cambios (`git commit -am 'Agrega nueva funcionalidad'`)
5. Push a la rama (`git push origin feature/nueva-funcionalidad`)
6. Crea un Pull Request

## 📞 Soporte

Si tienes problemas o preguntas:

1. Revisa la sección de [Solución de Problemas](#-solución-de-problemas)
2. Verifica que tu configuración sea correcta
3. Ejecuta el script de diagnóstico (si está disponible)

## 🎓 Aprendizaje

Este proyecto es ideal para aprender sobre:

- Manipulación de archivos y directorios en Python
- Uso de variables de entorno con `python-dotenv`
- Manejo de errores y excepciones
- Validación de datos
- Buenas prácticas de programación en Python
- Gestión de dependencias con Pipenv
- Documentación de código

## 🔮 Futuras Mejoras

Posibles funcionalidades a agregar:

- [ ] Modo interactivo para seleccionar archivos específicos
- [ ] Opción de vista previa antes de renombrar
- [ ] Deshacer cambios (restaurar nombres originales)
- [ ] Soporte para expresiones regulares en patrones
- [ ] Interfaz gráfica (GUI)
- [ ] Renombrado basado en metadatos (fecha de creación, EXIF, etc.)
- [ ] Modo batch para múltiples directorios
- [ ] Exportar log de cambios a archivo

---


<img src="https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExeXByYTViN2FhZTN3OWg5N2N0cTJmYWQ1cjhzcHFjZXFyOHJldnVuYSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/TY6lSlGuTVNdK/giphy.gif" alt="Perrito divertido" width="300"/>


**Desarrollado con ❤️ usando Python**

*Última actualización: Octubre 2025*