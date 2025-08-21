import numpy as np
from src.utils import grapher

def my_dft(x):
    """
    Calcula la Transformada de Fourier Discreta (DFT) de una señal 1D.
    
    Args:
        x (np.array): La señal de entrada (muestras).
        
    Returns:
        np.array: Los coeficientes complejos de la DFT.
    """
    N = len(x)
    X = np.zeros(N, dtype=np.complex128)
    # Itera sobre cada coeficiente de frecuencia k
    for k in range(N):
        sum_val = 0.0
        # Sumatoria sobre cada muestra n
        for n in range(N):
            angle = -2j * np.pi * k * n / N
            sum_val += x[n] * np.exp(angle)
        X[k] = sum_val
    return X

def find_spectral_peaks(magnitudes, freqs, num_peaks=3):
    """
    Encuentra los picos más significativos en el espectro de magnitud.
    
    Args:
        magnitudes (np.array): El espectro de magnitud de la señal.
        freqs (np.array): El eje de frecuencias correspondiente.
        num_peaks (int): El número de picos a encontrar.
        
    Returns:
        list of tuples: Una lista con (frecuencia, magnitud) para cada pico.
    """
    # Ordena los índices por magnitud de forma descendente
    peak_indices_sorted = np.argsort(magnitudes)[::-1]
    
    peaks = []
    found_freqs = []
    
    # Frecuencia de resolución para determinar la cercanía de los picos
    freq_resolution = freqs[1] - freqs[0]

    for index in peak_indices_sorted:
        if len(peaks) == num_peaks:
            break
        
        current_freq = freqs[index]
        
        # Comprueba si el pico actual está muy cerca de uno ya encontrado
        is_close = any(abs(current_freq - f) < 2 * freq_resolution for f in found_freqs)
        
        if not is_close:
            peaks.append((current_freq, magnitudes[index]))
            found_freqs.append(current_freq)
            
    # Ordena los picos encontrados por frecuencia para un reporte más claro
    return sorted(peaks, key=lambda p: p[0])


def run_analysis():
    """
    Función principal para generar la señal, muestrearla, calcular la DFT
    y visualizar los resultados.
    """
    # 1. PARÁMETROS DE LA SEÑAL Y MUESTREO
    fm = 0.5   # Frecuencia moduladora (Hz)
    fc = 8.0   # Frecuencia portadora (Hz)
    m = 0.5    # Índice de modulación
    
    # La frecuencia máxima en la señal es fc + fm = 8.5 Hz.
    # Por el Teorema de Nyquist, fs debe ser > 2 * 8.5 = 17 Hz.
    fs = 100.0  # Frecuencia de muestreo (Hz), elegimos un valor seguro.
    T_total = 4.0 # Duración de la señal (s) para capturar varios ciclos.
    N = int(fs * T_total) # Número total de muestras.

    # 2. CÁLCULO DE LA RESOLUCIÓN EN FRECUENCIA (Δf)
    delta_f = fs / N
    print("--- PARÁMETROS DE ANÁLISIS ---")
    print(f"Frecuencia de muestreo (fₛ): {fs} Hz")
    print(f"Número de muestras (N): {N}")
    print(f"Resolución en frecuencia (Δf = fₛ/N): {delta_f:.4f} Hz\n")
    
    # 3. GENERACIÓN Y MUESTREO DE LA SEÑAL
    # Vector de tiempo discreto (para las muestras)
    t_discrete = np.arange(N) / fs
    # Señal muestreada x[n]
    x_discrete = (1 + m * np.cos(2 * np.pi * fm * t_discrete)) * np.sin(2 * np.pi * fc * t_discrete)

    # (Opcional) Generar señal continua para una mejor visualización
    t_continuous = np.linspace(0, T_total, 2000)
    x_continuous = (1 + m * np.cos(2 * np.pi * fm * t_continuous)) * np.sin(2 * np.pi * fc * t_continuous)
    
    # 4. VISUALIZACIÓN DE LAS SEÑALES
    grapher.continuous_plotter(t_continuous, x_continuous, "Señal Continua Original: x(t)", "Tiempo (s)", "Amplitud")
    grapher.discrete_plotter(t_discrete, x_discrete, "Señal Muestreada: x[n]", "Tiempo (s)", "Amplitud")
    
    # 5. CÁLCULO DE LA DFT
    print("--- ANÁLISIS DFT ---")
    print("Calculando la DFT con la implementación propia...")
    X = my_dft(x_discrete)
    print("Cálculo de DFT completado.\n")
    
    # 6. ANÁLISIS DEL ESPECTRO
    # Magnitud de la DFT (se normaliza por N para que sea independiente del número de muestras)
    magnitudes = np.abs(X) / N
    # Eje de frecuencias
    freqs = np.arange(N) * delta_f
    
    # Visualización del espectro
    grapher.spectrum_plotter(freqs, magnitudes, "Espectro de Frecuencia (DFT)", N, fs)
    
    # 7. IDENTIFICACIÓN DE PICOS
    # Buscamos en la primera mitad del espectro (frecuencias positivas)
    positive_magnitudes = magnitudes[:N // 2]
    positive_freqs = freqs[:N // 2]
    
    # La señal tiene 3 componentes de frecuencia, por lo que buscamos 3 picos
    peaks = find_spectral_peaks(positive_magnitudes, positive_freqs, num_peaks=3)
    
    print("--- RESULTADOS ---")
    print("Picos espectrales identificados:")
    print("-" * 65)
    print("Frec. Teórica (Hz) | Frec. Estimada (Hz) | Amplitud Relativa Estimada")
    print("-" * 65)
    
    # Frecuencias teóricas: fc-fm, fc, fc+fm
    # Amplitudes teóricas: Para un seno de amplitud A, el pico en la DFT normalizada es A/2.
    # x(t) = sin(2π*fc*t) + (m/2)*sin(2π*(fc+fm)*t) - (m/2)*sin(2π*(fc-fm)*t)
    # Amplitudes teóricas: 0.5, m/4, m/4
    theoretical_freqs = sorted([fc - fm, fc, fc + fm])
    theoretical_amps = [m / 4, 0.5, m / 4] # Corresponden a [fc-fm, fc, fc+fm]

    for i, (freq, mag) in enumerate(peaks):
        # La magnitud en la DFT es A/2, así que la amplitud relativa es 2 * mag
        amplitude = mag * 2
        print(f"{theoretical_freqs[i]:<18.2f} | {freq:<21.4f} | {amplitude:.4f} (Teórica: {theoretical_amps[i]*2:.4f})")
    print("-" * 65)
