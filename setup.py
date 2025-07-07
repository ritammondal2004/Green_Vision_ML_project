
#it is the build script for setup tools, a tool used to package and distribute 
# Python projects. It defines the metadata and configuration for the project.its like a blueprint that tells python 
#how to install the project


from setuptools import find_packages, setup

setup(
    name="Green_vision" ,
    version="0.0.1",
    author= "Ritam_Mondal",
    author_email="ritamm134@gmail.com" ,
    packages= find_packages() ,
    install_requires=[]
)
