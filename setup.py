from setuptools import setup,find_packages
from typing import List
def get_requirements(filename:str)->List[str]:
    requirements=[]
    hyphen_e_dot='-e .'
    with open(filename) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("/n","") for req in requirements]
        if hyphen_e_dot in requirements:
            requirements.remove(hyphen_e_dot)
    return requirements
setup(
    name="mlprojet",
    version='0.0.1',
    author='nagasai',
    author_email='jonnalagaddanagasai6@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
    
)