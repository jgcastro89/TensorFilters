from setuptools import setup, find_namespace_packages

long_description = ""

setup(
    name="tensor_filter",
    version="0.0.1",
    description="Python package that applies filters to tensors",
    long_description=long_description,
    author="Joel Castro",
    packages=find_namspace_packages(":", "src"),
    install_requires=["numpy"]
    )
