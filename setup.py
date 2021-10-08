from setuptools import setup, find_packages
with open('requirements.txt') as f:
    data = f.read()
reqs = data.split()

setup(
    name='ficosa_exam_scg',
    version='1.0',
    packages=find_packages(),
    license='MIT',
    author='Sergio Campos Gallego',
    author_email='camposgallego@gmail.com',
    description='Ficosa test code',
    install_requires=reqs
)
