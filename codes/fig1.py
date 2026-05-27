import os
import numpy as np
import matplotlib.pyplot as plt
try:
    import ipywidgets as widgets
    from IPython.display import display
except ImportError:
    pass

# 1. GENERACIÓN DEL GRÁFICO CON MATPLOTLIB
def generar_grafico_matplotlib():
    """Genera la visualización analítica con estilos académicos."""
    fig, ax = plt.subplots(figsize=(10, 5))
    x = np.linspace(0, 10, 100)
    y = 1 / (1 + np.exp(-(x - 5))) * 5
    
    ax.plot(x, y, color='black', lw=2.5)
    ax.axhline(y=3.5, color='gray', linestyle='--', alpha=0.5)
    
    ax.set_ylabel("Quantum Capability Evolution", fontsize=11, fontweight='bold')
    ax.set_xlabel("lifecycle of a LEO satellite constellation", fontsize=11, fontweight='bold')
    ax.set_title("Quantum Threat Assessment in LEO Architectures", fontsize=13)
    plt.tight_layout()
    plt.show()

# 2. CÓDIGO TIKZ AUTÓNOMO
tikz_code = r"""
\documentclass[tikz,border=10pt]{standalone}
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}
    \draw[->, thick] (0,0) -- (12,0);
    \draw[very thick] (0,2) to[out=20, in=180] (10,5);
    \draw[fill=black] (0,0.2) rectangle (4,0.5);
    \draw[fill=gray!50] (4.2,0.2) rectangle (11,0.5);
    \node at (6, -0.7) {\textbf{lifecycle of a LEO satellite constellation}};
\end{tikzpicture}
\end{document}
"""

# 3. INTERFAZ Y LÓGICA DE GUARDADO
def guardar_archivo(b=None):
    nombre = text_input.value if 'text_input' in locals() else "analisis_quantum_leo.tex"
    ruta = "workflow/workflow/outputs/codes/"
    os.makedirs(ruta, exist_ok=True)
    if not nombre.endswith('.tex'): nombre += '.tex'
    
    with open(os.path.join(ruta, nombre), 'w') as f:
        f.write(tikz_code)
    print(f"Archivo guardado exitosamente en {ruta}{nombre}")

# Renderizado de interfaz (si ipywidgets está disponible)
if 'widgets' in globals():
    text_input = widgets.Text(value='quantum_threat_analysis.tex', description='Archivo:')
    save_button = widgets.Button(description='Guardar TikZ', button_style='primary')
    save_button.on_click(guardar_archivo)
    display(text_input, save_button)
else:
    guardar_archivo()

generar_grafico_matplotlib()