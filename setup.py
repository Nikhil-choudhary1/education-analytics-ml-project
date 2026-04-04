from setuptools import setup, find_packages
from typing import List

def get_requirements(file_path:str) -> List[str]:
    requirements = []
    with open(file_path) as file:
        requirements = file.readlines()
        
    requirements = [req.replace("\n", "") for req in requirements]

setup(
    name='education_analytics',
    version='0.1.0',
    author='Nikhil Choudhary',
    author_email='nikhil.choudhary3112@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
    )