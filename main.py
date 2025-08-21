import sys
import os

# Añade el directorio 'src' al path de Python para permitir importaciones directas
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

def main():
    """
    Punto de entrada principal del programa.
    Verifica los argumentos de la línea de comandos y ejecuta la tarea correspondiente.
    """
    print("Iniciando ejecución de la práctica...")
    
    # El primer argumento es el nombre del script, el segundo es la tarea.
    if len(sys.argv) < 2:
        print("\nError: Argumento no especificado.")
        print("Uso: python main.py <nombre_de_la_tarea>")
        print("Ejemplo: python main.py examen_p1")
        return

    task_name = sys.argv[1]

    if task_name == "examen_p1":
        try:
            # Importa la función de análisis desde el módulo correspondiente
            from examen_p1 import run_analysis
            print(f"Tarea encontrada: '{task_name}'. Ejecutando análisis...\n")
            run_analysis()
        except ImportError:
            print(f"\nError: No se pudo encontrar el módulo '{task_name}.py' en el directorio 'src'.")
        except Exception as e:
            print(f"\nOcurrió un error inesperado al ejecutar la tarea: {e}")
    else:
        print(f"\nError: Tarea desconocida -> '{task_name}'.")
        print("La única tarea disponible es 'examen_p1'.")

if __name__ == "__main__":
    main()
