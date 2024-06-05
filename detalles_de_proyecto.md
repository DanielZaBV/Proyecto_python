Proyecto: Analisis_coloriespaciales

Descripción:
Este proyecto consiste en un paquete de Python para realizar análisis de colores en imágenes espaciales. Proporciona herramientas para generar imágenes de muestra, analizar colores en imágenes mediante valores del 0 al 1 en un archivo y generar informes sobre la distribución de colores en diferentes áreas de una imagen.

Componentes:
- `data`: Carpeta donde se guardan los archivos con los que se trabajará
- `scripts`: Módulo para realizar análisis de colores en imágenes.
- `utils`: Módulo con funciones de utilidad para el paquete.
- `tests`: Carpeta con pruebas unitarias para el paquete.
- `docs`: Carpeta para documentación del proyecto.

Dependencias:
- Pillow>=8.4.0

Uso:
- Instalar el paquete: `pip install Analisis_coloriespaciales`
- Generar una imagen de muestra: `python -m Analisis_coloriespaciales.generate_image`
- Realizar análisis de colores: `python -m Analisis_coloriespaciales.analyze data/selected_colors.txt 31622 31622`



Repositorio:
URL: https://github.com/DanielZaBV/Proyecto_python
