```json
{
  "titulo": "Hacia una infraestructura orbital con resiliencia cuántica: un marco integral para la integración de criptografía poscuántica (PQC) en redes satelitales de próxima generación",
  "folder_name": "infraestructura_orbital_resiliencia_cuantica_pqc",
  "abstract_preliminar": "La convergencia de computación cuántica y constelaciones de satélites LEO/MEO plantea amenazas existenciales a la seguridad de las comunicaciones espaciales basadas en criptografía de clave pública clásica. Este artículo propone un marco integral para una infraestructura orbital con resiliencia cuántica mediante la integración sistemática de algoritmos de criptografía poscuántica (PQC) estandarizados por NIST (ML-KEM, ML-DSA, SLH-DSA) en protocolos de redes satelitales de próxima generación. Se analizan restricciones de recursos (energía, ancho de banda, radiación) en entornos espaciales y se presenta una arquitectura híbrida PQC-clásica con agilidad criptográfica. Mediante modelado analítico, simulaciones y evaluación en plataformas emuladas de satélites, se demuestran mejoras en resiliencia contra ataques harvest-now-decrypt-later mientras se mantiene overhead aceptable en latencia y throughput. Los resultados indican viabilidad para despliegues en constelaciones mega-LEO, contribuyendo a estándares CCSDS y arquitecturas 6G-NTN seguras. Se discuten desafíos de implementación, verificación formal y hoja de ruta de migración 2025-2035.",
  "secciones": [
    {
      "nro": 1,
      "titulo_seccion": "Introducción",
      "objetivos": ["Establecer la motivación y relevancia del problema cuántico en infraestructuras orbitales", "Definir objetivos y alcance del marco propuesto", "Presentar estructura del artículo"],
      "subsecciones": ["1.1 Motivación y amenazas cuánticas", "1.2 Contribuciones principales", "1.3 Organización del documento"],
      "insumos": ["Figura 1: Evolución de amenazas cuánticas", "Tabla 1: Comparación criptografía clásica vs PQC"],
      "llaves_bibtex": ["Kim2026", "Ghosh2026", "NIST_PQC2024"]
    },
    {
      "nro": 2,
      "titulo_seccion": "Antecedentes y Estado del Arte",
      "objetivos": ["Revisar el estado actual de PQC y QKD en comunicaciones satelitales", "Identificar brechas en integración para redes orbitales"],
      "subsecciones": ["2.1 Criptografía poscuántica: algoritmos y estandarización", "2.2 Redes satelitales de próxima generación y NTN", "2.3 Enfoques híbridos y QKD satelital", "2.4 Brechas de investigación"],
      "insumos": ["Tabla 2: Rendimiento de algoritmos PQC en hardware espacial", "Figura 2: Taxonomía de soluciones de seguridad cuántica"],
      "llaves_bibtex": ["Kim2026", "Lewerenz2025", "Xu2025", "Hong2026"]
    },
    {
      "nro": 3,
      "titulo_seccion": "Fundamentos Técnicos",
      "objetivos": ["Presentar bases matemáticas de PQC relevantes", "Analizar restricciones de entornos orbitales"],
      "subsecciones": ["3.1 Algoritmos lattice-based y hash-based", "3.2 Modelos de canales satelitales y restricciones de recursos", "3.3 Métricas de resiliencia cuántica"],
      "insumos": ["Eq. 1: Complejidad de ML-KEM", "Tabla 3: Requerimientos computacionales en FPGA espaciales"],
      "llaves_bibtex": ["Ghosh2026", "Kim2026"]
    },
    {
      "nro": 4,
      "titulo_seccion": "Marco Propuesto de Integración PQC",
      "objetivos": ["Definir la arquitectura integral propuesta", "Detallar mecanismos de integración y agilidad criptográfica"],
      "subsecciones": ["4.1 Arquitectura de capas", "4.2 Protocolos híbridos PQC-clásicos", "4.3 Gestión de claves y autenticación en constelaciones", "4.4 Mecanismos de resiliencia orbital"],
      "insumos": ["Figura 3: Diagrama del marco propuesto", "Eq. 2: Protocolo de handshake PQC"],
      "llaves_bibtex": ["Lewerenz2025", "Hong2026", "Seyhan2025"]
    },
    {
      "nro": 5,
      "titulo_seccion": "Evaluación y Análisis de Rendimiento",
      "objetivos": ["Presentar metodología de evaluación", "Analizar resultados cuantitativos de resiliencia y overhead"],
      "subsecciones": ["5.1 Metodología de simulación y emulación", "5.2 Resultados de rendimiento", "5.3 Análisis de seguridad y casos de ataque"],
      "insumos": ["Tabla 4: Comparación de latencia y energía", "Figura 4: Gráficos de rendimiento en LEO"],
      "llaves_bibtex": ["Hong2026", "Xu2025", "Lewerenz2025"]
    },
    {
      "nro": 6,
      "titulo_seccion": "Discusión y Desafíos de Implementación",
      "objetivos": ["Discutir implicaciones prácticas", "Identificar limitaciones y desafíos abiertos"],
      "subsecciones": ["6.1 Consideraciones de estandarización CCSDS", "6.2 Radiación y longevidad en órbita", "6.3 Hoja de ruta de migración"],
      "insumos": ["Tabla 5: Comparación con enfoques existentes"],
      "llaves_bibtex": ["Kim2026", "Ghosh2026"]
    },
    {
      "nro": 7,
      "titulo_seccion": "Conclusiones y Trabajos Futuros",
      "objetivos": ["Sintetizar contribuciones", "Proponer direcciones de investigación futuras"],
      "subsecciones": ["7.1 Conclusiones principales", "7.2 Limitaciones del estudio", "7.3 Trabajos futuros"],
      "insumos": [],
      "llaves_bibtex": ["Kim2026", "NIST_PQC2024"]
    }
  ]
}
```

```bibtex
% PARTE 2: Bibliografía Seccional - Sección 1
@article{Kim2026,
  author = {Kim, H. and others},
  title = {Post-quantum cryptography for space systems: Algorithms, implementation, and design constraints—A systematic survey},
  journal = {Acta Astronautica},
  volume = {246},
  pages = {863-886},
  year = {2026},
  doi = {10.1016/j.actaastro.2026.XX.XXX}
}

@article{Ghosh2026,
  author = {Ghosh, S. and others},
  title = {Secure Satellite Communication in the Post-Quantum Era: A Lattice-Based Cryptographic Approach},
  journal = {International Journal of Satellite Communications and Networking},
  year = {2026},
  doi = {10.1002/sat.70041}
}

@misc{NIST_PQC2024,
  author = {NIST},
  title = {Post-Quantum Cryptography Standardization},
  year = {2024},
  howpublished = {https://csrc.nist.gov/projects/post-quantum-cryptography}
}
```

```bibtex
% PARTE 2: Bibliografía Seccional - Sección 2
@conference{Lewerenz2025,
  author = {Lewerenz, E.},
  title = {Deploying Post Quantum Cryptography on Newspace Satellites},
  booktitle = {Small Satellite Conference},
  year = {2025}
}

@article{Xu2025,
  author = {Xu, S.},
  title = {A Preliminary Study of PQC Implementations for Satellite Communication Networks},
  year = {2025},
  note = {ESA Proceedings}
}

@inproceedings{Hong2026,
  author = {Hong, G.H. and Lee, Y. and others},
  title = {Experimental evaluation of PQ-WireGuard and PQ-IPsec over LEO satellite networks},
  journal = {Array},
  year = {2026}
}
```

```bibtex
% PARTE 2: Bibliografía Seccional - Sección 3
% Reutiliza Kim2026 y Ghosh2026 (ya definidos)
```

```bibtex
% PARTE 2: Bibliografía Seccional - Sección 4
@conference{Seyhan2025,
  author = {Seyhan, K.},
  title = {A lightweight post-quantum authentication framework for next-generation satellite communication standards},
  year = {2025},
  booktitle = {IET Conference Publication}
}
% Reutiliza Lewerenz2025 y Hong2026
```

```bibtex
% PARTE 2: Bibliografía Seccional - Sección 5
% Reutiliza Hong2026, Xu2025, Lewerenz2025
```

```bibtex
% PARTE 2: Bibliografía Seccional - Sección 6 y 7
% Reutiliza Kim2026, Ghosh2026, NIST_PQC2024
```

```json
{
  "seccion_nro": 1,
  "titulo_seccion": "Introducción",
  "mapa_uso": {
    "Kim2026": {
      "razon_seleccion": "Survey sistemático reciente sobre PQC en sistemas espaciales con énfasis en restricciones de satélites.",
      "guia_redaccion": "Usar en 1.1 para motivar amenazas y citar gaps de investigación en 1.2.",
      "subseccion_destino": "1.1"
    },
    "Ghosh2026": {
      "razon_seleccion": "Análisis lattice-based específico para comunicaciones satelitales seguras.",
      "guia_redaccion": "Citar en 1.1 para contexto de enfoques post-cuánticos en satélites.",
      "subseccion_destino": "1.1"
    },
    "NIST_PQC2024": {
      "razon_seleccion": "Estándares oficiales NIST para algoritmos PQC.",
      "guia_redaccion": "Referenciar en 1.2 al mencionar algoritmos seleccionados como base del marco.",
      "subseccion_destino": "1.2"
    }
  }
}
```

```json
{
  "seccion_nro": 2,
  "titulo_seccion": "Antecedentes y Estado del Arte",
  "mapa_uso": {
    "Kim2026": {
      "razon_seleccion": "Proporciona revisión comprehensiva y roadmap de transición.",
      "guia_redaccion": "Base principal de la subsección 2.4 sobre brechas.",
      "subseccion_destino": "2.4"
    },
    "Lewerenz2025": {
      "razon_seleccion": "Implementación práctica de protocolos híbridos en NewSpace.",
      "guia_redaccion": "Contrastar en 2.3 con enfoques híbridos PQC+ECC.",
      "subseccion_destino": "2.3"
    },
    "Xu2025": {
      "razon_seleccion": "Estudio preliminar de impacto PQC en protocolos satelitales.",
      "guia_redaccion": "Usar métricas de overhead en Tabla 2 de 2.1.",
      "subseccion_destino": "2.1"
    },
    "Hong2026": {
      "razon_seleccion": "Evaluación experimental en redes LEO reales/simuladas.",
      "guia_redaccion": "Citar resultados de rendimiento PQ-WireGuard/IPsec en 2.2.",
      "subseccion_destino": "2.2"
    }
  }
}
```

```json
{
  "seccion_nro": 3,
  "titulo_seccion": "Fundamentos Técnicos",
  "mapa_uso": {
    "Ghosh2026": {
      "razon_seleccion": "Análisis detallado de suposiciones de dureza lattice para satélites.",
      "guia_redaccion": "Explicar en 3.1 con ecuaciones de seguridad.",
      "subseccion_destino": "3.1"
    },
    "Kim2026": {
      "razon_seleccion": "Datos cuantitativos de implementación en hardware espacial.",
      "guia_redaccion": "Soporte para Tabla 3 en 3.2 sobre restricciones.",
      "subseccion_destino": "3.2"
    }
  }
}
```

```json
{
  "seccion_nro": 4,
  "titulo_seccion": "Marco Propuesto de Integración PQC",
  "mapa_uso": {
    "Lewerenz2025": {
      "razon_seleccion": "Protocolo Triple KEM híbrido para satélites.",
      "guia_redaccion": "Adaptar como base para 4.2 y Eq. 2.",
      "subseccion_destino": "4.2"
    },
    "Hong2026": {
      "razon_seleccion": "Evaluaciones de protocolos VPN post-cuánticos en LEO.",
      "guia_redaccion": "Integrar lecciones en mecanismos de handshake de 4.3.",
      "subseccion_destino": "4.3"
    },
    "Seyhan2025": {
      "razon_seleccion": "Framework de autenticación ligera PQC para estándares satelitales.",
      "guia_redaccion": "Incorporar en capa de autenticación de la arquitectura 4.1.",
      "subseccion_destino": "4.1"
    }
  }
}
```

```json
{
  "seccion_nro": 5,
  "titulo_seccion": "Evaluación y Análisis de Rendimiento",
  "mapa_uso": {
    "Hong2026": {
      "razon_seleccion": "Datos experimentales directos en entornos LEO.",
      "guia_redaccion": "Comparar resultados propios vs. este trabajo en Tabla 4.",
      "subseccion_destino": "5.2"
    },
    "Xu2025": {
      "razon_seleccion": "Análisis de impacto en secure boot y actualizaciones.",
      "guia_redaccion": "Usar para análisis de overhead en 5.1 y 5.3.",
      "subseccion_destino": "5.1"
    },
    "Lewerenz2025": {
      "razon_seleccion": "Implementación en satélites NewSpace.",
      "guia_redaccion": "Validar resiliencia del protocolo propuesto.",
      "subseccion_destino": "5.3"
    }
  }
}
```

```json
{
  "seccion_nro": 6,
  "titulo_seccion": "Discusión y Desafíos de Implementación",
  "mapa_uso": {
    "Kim2026": {
      "razon_seleccion": "Identificación de 15 gaps y roadmap 2025-2040.",
      "guia_redaccion": "Base para hoja de ruta en 6.3.",
      "subseccion_destino": "6.3"
    },
    "Ghosh2026": {
      "razon_seleccion": "Consideraciones prácticas de despliegue lattice en satélites.",
      "guia_redaccion": "Discutir integración y agilidad en 6.1-6.2.",
      "subseccion_destino": "6.2"
    }
  }
}
```

```json
{
  "seccion_nro": 7,
  "titulo_seccion": "Conclusiones y Trabajos Futuros",
  "mapa_uso": {
    "Kim2026": {
      "razon_seleccion": "Roadmap y gaps para contextualizar contribuciones.",
      "guia_redaccion": "Comparar marco propuesto vs. estado del arte y sugerir futuros.",
      "subseccion_destino": "7.3"
    },
    "NIST_PQC2024": {
      "razon_seleccion": "Estándares de referencia para validación.",
      "guia_redaccion": "Mencionar alineación con estándares en conclusiones.",
      "subseccion_destino": "7.1"
    }
  }
}
```