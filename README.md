# Práctica: Transformada de Fourier Discreta (DFT)

Este repositorio contiene la implementación en Python desde cero de la Transformada de Fourier Discreta (DFT), aplicada a una señal sinusoidal modulada en amplitud para analizar su contenido frecuencial.

## Objetivo

El objetivo de esta práctica es aplicar la DFT a una señal muestreada para:
- Implementar el algoritmo de la DFT sin usar librerías como `scipy.fft`.
- Muestrear correctamente una señal continua basándose en el Teorema de Nyquist.
- Identificar los picos espectrales en la señal transformada.
- Estimar las frecuencias y amplitudes relativas de los componentes de la señal.
- Calcular y utilizar la resolución en frecuencia ($?f = f?/N$).

## ?? Estructura del Repositorio
+-- .gitignore
+-- README.md
+-- main.py
+-- requirements.txt
+-- src
+-- examen_p1.py
+-- utils
+-- grapher.py


- **`main.py`**: Punto de entrada del programa. Gestiona la ejecución.
- **`src/examen_p1.py`**: Contiene la lógica principal: generación de la señal, muestreo, implementación de la DFT y análisis de picos.
- **`src/utils/grapher.py`**: Módulo con funciones para graficar las señales y el espectro.
- **`requirements.txt`**: Lista de dependencias del proyecto.

## ??? Dependencias

Las librerías necesarias para ejecutar este proyecto son:
- **numpy**: Para cálculos numéricos y manejo de arreglos.
- **matplotlib**: Para la visualización de las señales y sus espectros.

## ?? Cómo Ejecutar

1.  **Clonar el repositorio:**
    ```bash
    git clone <URL_DE_TU_REPOSITORIO>
    cd <NOMBRE_DEL_DIRECTORIO>
    ```

2.  **Crear un entorno virtual (recomendado):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # En Windows: venv\Scripts\activate
    ```

3.  **Instalar las dependencias:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Ejecutar el programa:**
    El script se ejecuta desde la consola a través de `main.py`, especificando el nombre de la tarea (`examen_p1`).

    ```bash
    python main.py examen_p1
    ```

    Al ejecutarlo, el programa imprimirá en la consola los parámetros de análisis y los resultados de los picos encontrados. Además, se abrirán tres ventanas con las siguientes gráficas:
    1.  La señal continua original.
    2.  La señal después del muestreo.
    3.  El espectro de magnitud en frecuencia de la señal.
"# final-1" 
