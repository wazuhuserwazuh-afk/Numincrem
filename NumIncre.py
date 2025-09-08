import sys
import os
import argparse

def crear_secuencia(inicio, fin):
    """
    Crea un diccionario con una secuencia de números en un rango.
    """
    if inicio > fin:
        print("\n[!] El número inicial no puede ser mayor que el final. Intente de nuevo.\n")
        return None
        
    mi_diccionario = {}
    print(f"\n--- Creando una secuencia de números de {inicio} a {fin} ---")
    
    for i in range(inicio, fin + 1):
        try:
            mi_diccionario[i] = i
        except Exception as e:
            print(f"\n[!] Ocurrió un error inesperado al crear la secuencia: {e}")
            return None
    
    return mi_diccionario

def guardar_diccionario(diccionario, nombre_archivo):
    """
    Guarda el diccionario en un archivo de texto simple en la ubicación actual.
    """
    if not diccionario:
        print("\n[!] No hay un diccionario para guardar. Saliendo.")
        return

    # Asegura que el nombre de archivo tenga la extensión .txt
    if not nombre_archivo.endswith('.txt'):
        nombre_archivo += '.txt'
        
    ruta_completa = os.path.join(os.getcwd(), nombre_archivo)
    
    # Verificar si el archivo ya existe y pedir confirmación para sobreescribir
    if os.path.exists(ruta_completa):
        confirmacion = input(f"[!] El archivo '{nombre_archivo}' ya existe. ¿Desea sobreescribirlo? (s/n): ").lower()
        if confirmacion != 's':
            print("\n[!] Operación cancelada. El archivo no fue modificado.")
            return
            
    try:
        with open(ruta_completa, 'w') as f:
            for valor in diccionario.values():
                f.write(f"{valor}\n")
        
        print(f"\n[+] Diccionario guardado exitosamente en: {ruta_completa}")
    except PermissionError:
        print(f"[!] Error de permisos: No se puede escribir en el archivo en la ruta: {ruta_completa}")
    except Exception as e:
        print(f"[!] Error inesperado al guardar el archivo: {e}")

def main():
    """
    Función principal que maneja los argumentos de la línea de comandos.
    """
    parser = argparse.ArgumentParser(description="Crea un diccionario de números y lo guarda en un archivo de texto.")
    parser.add_argument("--inicio", type=int, required=True, help="Número inicial del rango (inclusive).")
    parser.add_argument("--fin", type=int, required=True, help="Número final del rango (inclusive).")
    parser.add_argument("--nombre", type=str, required=True, help="Nombre del archivo a guardar (sin extensión).")
    
    args = parser.parse_args()

    if args.inicio > args.fin:
        print("\n[!] El número inicial no puede ser mayor que el final.")
        sys.exit(1)
    
    diccionario = crear_secuencia(args.inicio, args.fin)
    if diccionario:
        guardar_diccionario(diccionario, args.nombre)

if __name__ == "__main__":
    main()
