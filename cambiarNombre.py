from config import my_directory_path, my_prefix
import os

def change_names(directory_path, prefix):
    """
    Renombra todos los archivos de un directorio añadiendo un prefijo y número secuencial.
    
    Args:
        directory_path (str): Ruta del directorio con los archivos a renombrar
        prefix (str): Prefijo que se añadirá al inicio de cada nombre
    
    Returns:
        bool: True si se completó exitosamente, False si hubo errores
    """
    
    # Validación 0: Verificar que los parámetros no sean None
    if directory_path is None:
        print("❌ ERROR CRÍTICO: directory_path es None")
        print("\n📋 Esto significa que MY_DIRECTORY_PATH no se cargó del archivo .env")
        print("\nPasos para solucionar:")
        print("1. Verifica que existe el archivo .env en el directorio del proyecto")
        print("2. Abre .env y verifica que contiene:")
        print("   MY_DIRECTORY_PATH=C:/tu/ruta/aqui")
        print("   (sin espacios alrededor del =)")
        print("3. Asegúrate de que el nombre es exactamente MY_DIRECTORY_PATH")
        print("4. Usa barras / o dobles barras \\\\")
        return False
    
    if prefix is None or prefix.strip() == '':
        print("⚠️ Advertencia: prefix está vacío. Usando 'archivo' por defecto.")
        prefix = "archivo"
    
    # Validación 1: Verificar que el directorio existe
    if not os.path.exists(directory_path):
        print(f"❌ Error: El directorio '{directory_path}' no existe.")
        print(f"\nVerifica que la ruta es correcta:")
        print(f"   Ruta actual: {directory_path}")
        return False
    
    # Validación 2: Verificar que es un directorio y no un archivo
    if not os.path.isdir(directory_path):
        print(f"❌ Error: '{directory_path}' no es un directorio válido.")
        return False
    
    try:
        # Obtener todos los elementos del directorio
        all_items = os.listdir(directory_path)
        
        # Filtrar solo archivos (excluir subdirectorios)
        files = [item for item in all_items 
                 if os.path.isfile(os.path.join(directory_path, item))]
        
        # Validación 3: Verificar que hay archivos para renombrar
        if not files:
            print("⚠️ Advertencia: No se encontraron archivos en el directorio.")
            print(f"   Directorio: {directory_path}")
            print(f"   Contenido encontrado: {all_items if all_items else 'vacío'}")
            return False
        
        print(f"📁 Se encontraron {len(files)} archivo(s) para renombrar.\n")
        
        # Contador de archivos procesados exitosamente
        renamed_count = 0
        errors = []
        
        # Procesar cada archivo
        for counter, file_name in enumerate(files):
            try:
                # Separar nombre y extensión
                name, extension = os.path.splitext(file_name)
                
                # Crear el nuevo nombre
                new_name = f'{prefix}_{counter}{extension}'
                
                # Crear rutas completas
                old_path = os.path.join(directory_path, file_name)
                new_path = os.path.join(directory_path, new_name)
                
                # Validación 4: Verificar que el nuevo nombre no existe ya
                if os.path.exists(new_path):
                    print(f"⚠️ Saltando '{file_name}': el archivo '{new_name}' ya existe.")
                    errors.append(f"{file_name} -> nombre duplicado")
                    continue
                
                # Renombrar el archivo
                os.rename(old_path, new_path)
                
                # Mensaje de confirmación para cada archivo
                print(f"✅ Renombrado: '{file_name}' → '{new_name}'")
                renamed_count += 1
                
            except PermissionError:
                error_msg = f"Sin permisos para renombrar '{file_name}'"
                print(f"❌ {error_msg}")
                errors.append(error_msg)
                
            except Exception as e:
                error_msg = f"Error al renombrar '{file_name}': {str(e)}"
                print(f"❌ {error_msg}")
                errors.append(error_msg)
        
        # Resumen final
        print(f"\n{'='*50}")
        print(f"✨ Proceso completado:")
        print(f"   • Archivos renombrados: {renamed_count}")
        print(f"   • Errores: {len(errors)}")
        
        if errors:
            print(f"\n⚠️ Detalles de errores:")
            for error in errors:
                print(f"   - {error}")
        
        print(f"{'='*50}")
        
        return True
        
    except PermissionError:
        print(f"❌ Error: No tienes permisos para acceder al directorio '{directory_path}'.")
        return False
        
    except Exception as e:
        print(f"❌ Error inesperado: {str(e)}")
        return False


if __name__ == "__main__":
    print("\n" + "="*60)
    print("🔄 RENOMBRADOR DE ARCHIVOS")
    print("="*60 + "\n")
    
    # Usar configuración desde config.py
    directory_path = my_directory_path
    prefix = my_prefix
    
    print(f"📋 Configuración:")
    print(f"   Directorio: {directory_path}")
    print(f"   Prefijo: {prefix}\n")
    
    # Validación antes de ejecutar
    if directory_path is None:
        print("\n" + "="*60)
        print("❌ ERROR DE CONFIGURACIÓN")
        print("="*60)
        print("\nNO se pudo cargar MY_DIRECTORY_PATH del archivo .env")
        print("\nRevisa el output de config.py arriba ⬆️")
        print("="*60)
        input("\nPresiona Enter para salir...")
        exit(1)
    
    # Ejecutar el renombrado
    print("🚀 Iniciando proceso de renombrado...\n")
    success = change_names(directory_path, prefix)
    
    if success:
        print("\n🎉 ¡Operación finalizada con éxito!")
    else:
        print("\n⚠️ La operación se completó con advertencias o errores.")
    
    input("\nPresiona Enter para salir...")