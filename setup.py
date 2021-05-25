from setuptools import setup

with open("README.md", "r", encoding="utf8") as fh:
    long_description = fh.read()

setup(
    name='empyrial',
    version='0.1.4',
    description='Empyrial makes portfolio management and analysis faster and easier',
    py_modules=['empyrial'],
    package_dir={'':'src'},
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url='https://github.com/ssantoshp/Empyrial',
    author = "Santosh Passoubady",
    author_email = "santoshpassoubady@gmail.com",
    license='MIT',
    install_requires=[
          'numpy',
          'matplotlib',
          'pykalman',
          'seaborn',
          'scipy',
          'pandas_datareader',
          'datetime',
          'statsmodels',
          'sklearn',
          'empyrical',
          'quantstats',
          'python-dateutil',
          'python-math',
          'yfinance'
      ],
)
