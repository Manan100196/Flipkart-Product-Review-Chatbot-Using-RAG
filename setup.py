from setuptools import find_packages, setup

setup(name="flipkart-bot",
       version="0.0.1",
       author="Manan",
       author_email="manan10195@gmail.com",
       packages=find_packages(),
       install_requires=['langchain-astradb','langchain'])