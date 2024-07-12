from setuptools import setup, find_packages

setup(
    name='my_project',
    version='0.1',
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    install_requires=[
        # Aquí puedes añadir cualquier dependencia que necesite tu proyecto
    ],
)

# Correr pip install -e . en la raiz donde este el setup.py
