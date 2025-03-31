def buscar_y_reemplazar(nombre_archivo, palabra_buscar, palabra_reemplazar, nuevo_archivo=None):
    """
    Busca una palabra en un archivo de texto y la reemplaza por otra.
    
    :param nombre_archivo: Nombre del archivo .txt a modificar.
    :param palabra_buscar: Palabra o frase a buscar.
    :param palabra_reemplazar: Palabra o frase de reemplazo.
    :param nuevo_archivo: Si se especifica, guarda los cambios en un nuevo archivo.
                          Si es None, modifica el archivo original.
    """
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            contenido = archivo.read()
        
        contenido_modificado = contenido.replace(palabra_buscar, palabra_reemplazar)
        
        archivo_salida = nuevo_archivo if nuevo_archivo else nombre_archivo
        
        with open(archivo_salida, 'w', encoding='utf-8') as archivo:
            archivo.write(contenido_modificado)
            
        print(f" **Se reemplazó** '{palabra_buscar}' por '{palabra_reemplazar}' en '{archivo_salida}'.")
    except FileNotFoundError:
        print(f" Error: El archivo '{nombre_archivo}' no existe.")
    except Exception as e:
        print(f" Ocurrió un error: {e}")

# Ejemplo de uso:
if __name__ == "__main__":
    print("////Buscar y Reemplazar en Archivo TXT////// ")
    archivo = input("Ingresa la ruta donde tengas el archivo seguido por \su nombre.txt(ej: 'datos.txt'): ")
    buscar = input("Palabra a buscar: ")
    reemplazar = input("Palabra de reemplazo: ")
    opcion = input("¿Guardar en nuevo archivo? (s/n): ").strip().lower()
    
    nuevo_archivo = None
    if opcion == 's':
        nuevo_archivo = input("ingresa la ruta donde quieres que se guarde el archivo seguido por \su nuevo nombre.txt (ej: 'modificado.txt'): ")
    
    buscar_y_reemplazar(archivo, buscar, reemplazar, nuevo_archivo)