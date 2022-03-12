from setuptools import find_namespace_packages
from setuptools import setup

long_description = ""

setup(
    name="tensor_filter",
    version="0.0.1",
    description="Python package that applies filters to images",
    long_description=long_description,
    author="Joel Castro",
    packages=find_namespace_packages("", "src"),
    install_requires=["numpy"],
)
