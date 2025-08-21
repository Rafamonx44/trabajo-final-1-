# Pr�ctica: Transformada de Fourier Discreta (DFT)

Este repositorio contiene la implementaci�n en Python desde cero de la Transformada de Fourier Discreta (DFT), aplicada a una se�al sinusoidal modulada en amplitud para analizar su contenido frecuencial.

## Objetivo

El objetivo de esta pr�ctica es aplicar la DFT a una se�al muestreada para:
- Implementar el algoritmo de la DFT sin usar librer�as como `scipy.fft`.
- Muestrear correctamente una se�al continua bas�ndose en el Teorema de Nyquist.
- Identificar los picos espectrales en la se�al transformada.
- Estimar las frecuencias y amplitudes relativas de los componentes de la se�al.
- Calcular y utilizar la resoluci�n en frecuencia ($?f = f?/N$).

## ?? Estructura del Repositorio
+-- .gitignore
+-- README.md
+-- main.py
+-- requirements.txt
+-- src
+-- examen_p1.py
+-- utils
+-- grapher.py


- **`main.py`**: Punto de entrada del programa. Gestiona la ejecuci�n.
- **`src/examen_p1.py`**: Contiene la l�gica principal: generaci�n de la se�al, muestreo, implementaci�n de la DFT y an�lisis de picos.
- **`src/utils/grapher.py`**: M�dulo con funciones para graficar las se�ales y el espectro.
- **`requirements.txt`**: Lista de dependencias del proyecto.

## ??? Dependencias

Las librer�as necesarias para ejecutar este proyecto son:
- **numpy**: Para c�lculos num�ricos y manejo de arreglos.
- **matplotlib**: Para la visualizaci�n de las se�ales y sus espectros.

## ?? C�mo Ejecutar

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
    El script se ejecuta desde la consola a trav�s de `main.py`, especificando el nombre de la tarea (`examen_p1`).

    ```bash
    python main.py examen_p1
    ```

    Al ejecutarlo, el programa imprimir� en la consola los par�metros de an�lisis y los resultados de los picos encontrados. Adem�s, se abrir�n tres ventanas con las siguientes gr�ficas:
    1.  La se�al continua original.
    2.  La se�al despu�s del muestreo.
    3.  El espectro de magnitud en frecuencia de la se�al.
"# final-1" 
