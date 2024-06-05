# Analisis_coloriespaciales

Este paquete proporciona herramientas para realizar análisis de colores en imágenes.
Uso
Generar una Imagen de Muestra
Primero, puedes generar una imagen de muestra con el script generate_image.py. Por ejemplo:

```bash

python -m Analisis_coloriespaciales.generate_image
```

Esto generará una imagen de muestra en el directorio data.

Realizar el Análisis de Colores

Una vez que tengas la imagen de muestra, puedes realizar un análisis de colores espaciales. Por ejemplo:
```bash
python -m Analisis_coloriespaciales data/selected_colors.txt 31622 31622
```
Esto analizará los colores en la imagen utilizando los datos del archivo selected_colors.txt y generará un informe de análisis.