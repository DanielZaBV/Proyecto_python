from PIL import Image
import random

# Definir dimensiones de la imagen
width = 31622
height = 31622

# Definir umbral de diferencia de color
umbral = 20  # Puedes ajustar este valor segun tus necesidades

# Crear una nueva imagen RGB vacia
image = Image.new("RGB", (width, height))

# Cargar los pixeles de la imagen
pixels = image.load()

# Funcion para generar un color aleatorio con umbral
def color_aleatorio_umbral(umbral):
    return random.randint(umbral, 255)

# Rellenar la imagen con colores aleatorios
for y in range(height):
    for x in range(width):
        # Generar componentes de color aleatorios con umbral
        red = color_aleatorio_umbral(umbral)
        green = color_aleatorio_umbral(umbral)
        blue = color_aleatorio_umbral(umbral)
        # Asignar color al pixel
        pixels[x, y] = (red, green, blue)

# Guardar la imagen
image.save("imagen_con_umbral.png")

print("Imagen generada y guardada como 'imagen_con_umbral.png'")