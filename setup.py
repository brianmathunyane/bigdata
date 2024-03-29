from setuptools import setup, find_packages

setup(
    name='bigdata',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='MY data science python package.',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/brianmathunyane/bigdata',
    author='Brian Mathunyane',
    author_email='brianmath96@gmail.com'
)
