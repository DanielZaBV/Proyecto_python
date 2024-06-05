from setuptools import setup, find_packages

setup(
    name='Analisis_coloriespaciales',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'Pillow>=8.4.0',
    ],
    entry_points={
        'console_scripts': [
            'generate_image=Analisis_coloriespaciales.generate_image:main',
        ],
    },
    author='Daniel_Bautista',
    author_email='danielzb@lcg.unam.mx',
    description='Paquete para análisis de colores en imágenes',
    url='https://github.com/DanielZaBV/Proyecto_python',
    license='Apache 2.0',
)
