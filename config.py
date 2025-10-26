from dotenv import load_dotenv
import os

# Cargar variables de entorno
load_dotenv()

# Obtener configuración
my_directory_path = os.getenv("MY_DIRECTORY_PATH")
my_prefix = os.getenv("PREFIX", "archivo")  # valor por defecto

# Debugging - Elimina estas líneas después de que funcione
print("="*60)
print("DEBUG - config.py cargado")
print("="*60)
print(f"my_directory_path = {repr(my_directory_path)}")
print(f"my_prefix = {repr(my_prefix)}")
print("="*60 + "\n")

# Validación
if my_directory_path is None:
    print("⚠️ ADVERTENCIA: MY_DIRECTORY_PATH no encontrada en .env")
    print("Asegúrate de que el archivo .env existe y contiene:")
    print("MY_DIRECTORY_PATH=C:/tu/ruta/aqui\n")