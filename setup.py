from setuptools import setup

setup(
    name="quantum-poker",
    version="0.0.1",
    author="Franz Fuchs",
    url="https://github.com/sintefmath/QuantumPoker",
    packages=['quantum_poker'],
    install_requires=['qiskit >= 0.39.3',
                      'matplotlib >= 3.6.2',
                      'matplotlib-inline == 0.1.6',
                      'tk >= 0.1.0'],
)
