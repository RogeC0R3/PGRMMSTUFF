def buscar_y_reemplazar(cosa1_buscar, cosa2_buscar, cosa3_buscar, nuevo_plant=None):


    try:
        with open(cosa1_buscar, 'r', encoding='utf-8') as archivo:
            contenido = archivo.read()
        
        contenido_modificado = contenido.replace(cosa2_buscar, cosa3_buscar)
        
        archivo_salida = nuevo_plant if nuevo_plant else cosa1_buscar
        
        with open(archivo_salida, 'w', encoding='utf-8') as archivo:
            archivo.write(contenido_modificado)
            
        print(f" **Se reemplazó** '{cosa2_buscar}' por '{cosa3_buscar}' en '{archivo_salida}'.")
    except FileNotFoundError:
        print(f" Error: El archivo '{cosa1_buscar}' no existe.")
    except Exception as e:
        print(f" Ocurrió un error: {e}")

# Ejemplo de uso:
if __name__ == "__main__":
    print("////Buscar y Destruir en Archivo seleccionado////// ")
    archivo = input("Donde esta el archivo seleccionado a buscar y destruir: ")
    buscar = input("Palabra a DESTRUIR: ")
    reemplazar = input("Palabra a PLANTAR: ")
    opcion = input("¿Guardar en nuevo archivo? (s/n): ").strip().upper()
    
    nuevo_plant = None
    if opcion == 's':
        nuevo_plant = input("Introduce donde ira el archivo anteriormente seleccionado, ya corregido txt. ")
    
    buscar_y_reemplazar(archivo, buscar, reemplazar, nuevo_plant)