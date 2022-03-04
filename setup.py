from setuptools import setup, find_packages

long_description = ""

setup(
    name="tensor_filter",
    version="0.0.1",
    description="Python package that applies filters to tensors",
    long_description=long_description,
    author="Joel Castro",
    packages=find_packages(),
    install_requires=["numpy"]
    )