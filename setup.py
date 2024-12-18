from setuptools import find_packages,setup
from typing import List


def get_requirements()->List[str]:
    """
    This functions return list of requirements
    """
    requirement_lst:List[str]=[]
    try:
        with open('requirements.txt','r') as file:
            
            lines=file.readlines()
            for line in lines:
                requirement=line.strip()

                if requirement and requirement!='-e .':
                    requirement_lst.append(requirement)

    except FileNotFoundError:
        print("requirement.txt file not found")

    return requirement_lst

print(get_requirements())

setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="Akhil Ajith Nair",
    author_email="akhilajith757@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)