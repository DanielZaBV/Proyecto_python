# setup.py
from setuptools import setup, find_packages

setup(
    name="my_image_analysis",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "dask",
        "numpy",
        "Pillow"
    ],
    entry_points={
        "console_scripts": [
            "run_analysis=my_image_analysis.__main__:main"
        ]
    },
)
