from setuptools import find_packages, setup

setup(
    name="SQANTI3",
    version="5.1.2",
    url="https://github.com/ConesaLab/SQANTI3",
    packages=find_packages(".", exclude=["*tests*"]),
)
