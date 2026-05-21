Procedo a redactar el prompt de ingeniería de imágenes completamente optimizado para **`fig4.png`**.

Este prompt traduce la matriz de evaluación empírica en un layout multi-panel 1x3 exacto, incorporando de forma rigurosa las bandas de dispersión estadística, los perfiles continuos de área para los pases orbitales y el punto de quiebre crítico por desvanecimiento en ángulos menores a 10°, eliminando todo texto incrustado para permitir una rotulación limpia con `overpic`.

### PROMPT DE IMAGEN OPTIMIZADO (Gráficos de Rendimiento Estándar IEEE):

```json
A 2D technical vector diagram, multi-panel scientific performance plot, flat design, minimalist, background in pure white, utilizing a strict color palette of cobalt blue #0047AB, technical grey #4A4A4A, and deep black for axes and vector curves. The image contains NO embedded text, numbers, or alphabetic labels.

The diagram is organized in a perfectly balanced horizontal 1x3 grid layout containing three independent, identically sized square plots, each marked only with small subfigure indicators (a), (b), and (c) in the upper-left corners.

Plot (a) (Handshake Latency vs. Density): A Cartesian coordinate system with fine grey tick marks along the axes. Three mathematical curves ascend from left to right:
- Top curve (Technical Grey #4A4A4A) rises steeply, marked with discrete empty square data points.
- Middle curve (Cobalt Blue #0047AB) rises with a highly optimized, much lower slope, marked with discrete solid circular data points. This blue line is perfectly centered within a very faint, narrow, translucent blue shaded envelope block (representing the 95% statistical confidence interval).
- Bottom reference line (Deep Black) is a thin, flat dashed horizontal line running near the bottom axis.

Plot (b) (Normalized Energy Profile During Passes): A time-series profile plot representing continuous orbital pass windows. Instead of static bars, it features overlapping, smooth continuous area curves that peak near the center (bell-shaped distribution):
- The tallest curve is an outline in Technical Grey #4A4A4A filled with a very light, semi-transparent grey tint, showing a sharp high peak.
- The efficient curve is an outline in Cobalt Blue #0047AB filled with a very light, semi-transparent blue tint, showing a significantly lower, flattened, and optimized energy curve.

Plot (c) (Effective Throughput vs. Elevation Angle): A performance curve plot mapping channel degradation. A fine vertical dashed grey line runs perpendicular to the horizontal axis near the origin (marking the critical 10-degree elevation threshold). Three lines flow from right to left:
- Reference line (Thin Black Dashed) stays consistently high across the entire plot.
- Proposed architecture line (Cobalt Blue #0047AB, solid circle markers) stays high and stable on the right side, but upon crossing the vertical dashed threshold line towards the left, it shows a controlled, distinct downward step-like inflection curve.
- Comparison line (Technical Grey #4A4A4A, empty square markers) runs lower and exhibits a much sharper, severe drop towards the origin after passing the threshold.

Technical details: Absolute geometric alignment, crisp vector lines (1.5pt for data curves, 1pt for axes and grids), no ambient shadows, no decorative gradients, matching IEEE journal publication guidelines perfectly. All text labels are omitted for LaTeX overpic integration.

```