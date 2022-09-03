from setuptools import setup

try:
    with open("requirements.txt", "r") as rfile:
        requirements=rfile.readlines()
except FileNotFoundError:
    requirements = []

setup(
    name="afs_app",
    version="0.0.1",
    url="https://github.com/srcecde/azure-tutorial-code",

    author="Srce Cde (Chirag)",
    install_requires=requirements,

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python :: 3.8'
    ]

)
