from setuptools import setup

setup(name='core',
      version='1.1',
      description='Vitens EPANET 2.0 wrapper and utilities',
      url='https://github.com/vitenstc/epynet',
      author='Abel Heinsbroek',
      author_email='abel.heinsbroek@vitens.nl',
      license='Apache Licence 2.0',
      packages=['core'],
      package_data={'core': ['lib/*']},
      install_requires=[
          'pandas'
      ],
      zip_safe=False)