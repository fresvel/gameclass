from setuptools import setup
from setuptools import find_packages

setup(
   name='gameplay',
   version='1.0',
   description='A task for practicing Classes',
   author='Velasteguí Izurieta Homero Javier',
   author_email='fresvel@outlook.com',
   packages=['game'],
   entry_points={
       'console_scripts': [
           'gameplay=game.__main__:main',
       ]
   }
   )