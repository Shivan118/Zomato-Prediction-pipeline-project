from setuptools import find_packages, setup
from typing import List

HYPHON_E_DOT = '-e .'

def get_requriments(file_path:str)-> List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPHON_E_DOT in requirements:
            requirements.remove(HYPHON_E_DOT)

setup(name='Zomato Delivery Prediction',
      version='0.0.1',
      description='Machine Learning project',
      author='Shivan Kumar',
      author_email='dummay@gmail.com',
      install_requires = get_requriments('requirements.txt'),
      packages = find_packages()
     )
