from typing import List
from setuptools import setup,find_packages

hypen_dot = '-e .'
required_packages=[]
def get_requirements(file_path):
    with open(file_path, 'r') as file:
        required_packages=file.readlines()
        required_packages=[package.replace("\n","") for package in required_packages]
        if hypen_dot in required_packages:
            required_packages.remove(hypen_dot)
    return required_packages


setup( 
    name='ML-Project',
    version='0.0.1',
    packages=find_packages(),
    author='Arjun',
    author_email='vishnukumar1105@gmail.com',
    install_requires=get_requirements('requirements.txt')
)