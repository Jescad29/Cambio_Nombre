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
    
    # Validación 1: Verificar que el directorio existe
    if not os.path.exists(directory_path):
        print(f"❌ Error: El directorio '{directory_path}' no existe.")
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


# Ejemplo de uso con validación de entrada
if __name__ == "__main__":
    # Configuración
    directory_path = 'C:/Users/user/Desktop/videosYT/cambionombre'
    prefix = 'megustaelbrocoli'
    
    # Ejecutar el renombrado
    success = change_names(directory_path, prefix)
    
    if success:
        print("\n🎉 ¡Operación finalizada con éxito!")
    else:
        print("\n⚠️ La operación se completó con advertencias o errores.")