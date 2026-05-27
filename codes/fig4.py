import matplotlib.pyplot as plt
import numpy as np

# Configuración de estilo académico
plt.rcParams.update({'font.family': 'serif', 'font.size': 10})

fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# --- Gráfico (a): Handshake Latency vs. Density ---
x = np.linspace(0, 5, 6)
y1 = 1.2 * x + 0.5  # Línea azul
y2 = 0.25 * x**2 + 1 # Línea gris con curva
axes[0].plot(x, y1, 'o-', color='#0056b3', label='Latencia A')
axes[0].plot(x, y2, 's-', color='#6c757d', label='Latencia B')
axes[0].fill_between(x, y1-0.3, y1+0.3, color='#0056b3', alpha=0.2)
axes[0].axhline(y=0.2, color='black', linestyle='--')
axes[0].set_title('(a) Handshake Latency vs. Density')

# --- Gráfico (b): Normalized Energy Profile ---
t = np.linspace(-3, 3, 100)
e1 = np.exp(-t**2 / 0.5)        # Perfil azul (más ancho)
e2 = 1.5 * np.exp(-t**2 / 0.15) # Perfil gris (más estrecho)
axes[1].plot(t, e1, color='#0056b3', lw=2)
axes[1].fill_between(t, 0, e1, color='#0056b3', alpha=0.2)
axes[1].plot(t, e2, color='#6c757d', lw=2)
axes[1].fill_between(t, 0, e2, color='#6c757d', alpha=0.2)
axes[1].set_title('(b) Normalized Energy Profile')
axes[1].set_yticks([]) # Remover ejes para coincidir con la imagen

# --- Gráfico (c): Effective Throughput vs. Elevation Angle ---
angle = np.linspace(0, 8, 15)
th1 = 7 - 3 / (1 + np.exp(-(angle - 4))) # Curva azul
th2 = 6.5 - 6.5 / (1 + np.exp(-(angle - 3))) # Curva gris
axes[2].plot(angle, th1, 'o-', color='#0056b3')
axes[2].plot(angle, th2, 's-', color='#6c757d')
axes[2].axhline(y=7, color='black', linestyle='--')
axes[2].axvline(x=2, color='gray', linestyle='-.')
axes[2].set_title('(c) Effective Throughput vs. Elevation Angle')

for ax in axes:
    ax.set_xticks([])
    ax.set_yticks([])
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

plt.tight_layout()
plt.show()