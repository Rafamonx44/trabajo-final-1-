import matplotlib.pyplot as plt
import numpy as np

def continuous_plotter(t, signal, title, xlabel, ylabel):
    """
    Grafica una señal de tipo continuo.
    """
    plt.figure(figsize=(12, 6))
    plt.plot(t, signal)
    plt.title(title, fontsize=16)
    plt.xlabel(xlabel, fontsize=12)
    plt.ylabel(ylabel, fontsize=12)
    plt.grid(True)
    plt.show()

def discrete_plotter(n, signal, title, xlabel, ylabel):
    """
    Grafica una señal discreta usando un diagrama de tallo y hojas (stem plot).
    """
    plt.figure(figsize=(12, 6))
    # Usamos markerfmt y linefmt para controlar el estilo del gráfico de tallo
    (markerline, stemlines, baseline) = plt.stem(n, signal, linefmt='b-', markerfmt='bo', basefmt='r-')
    plt.setp(markerline, markersize=4)
    plt.title(title, fontsize=16)
    plt.xlabel(xlabel, fontsize=12)
    plt.ylabel(ylabel, fontsize=12)
    plt.grid(True)
    plt.show()

def spectrum_plotter(freq, magnitude, title, N, fs):
    """
    Grafica el espectro de frecuencia de una señal.
    """
    delta_f = fs / N
    plt.figure(figsize=(12, 6))
    # Graficamos solo la primera mitad del espectro (frecuencias positivas)
    plt.plot(freq[:N // 2], magnitude[:N // 2])
    plt.title(f"{title} (Δf = {delta_f:.4f} Hz)", fontsize=16)
    plt.xlabel("Frecuencia (Hz)", fontsize=12)
    plt.ylabel("Magnitud |X(f)|", fontsize=12)
    plt.grid(True)
    # Ajustar los límites para una mejor visualización de los picos
    max_magnitude = np.max(magnitude[:N // 2])
    plt.ylim(0, max_magnitude * 1.1)
    plt.show()
