from setuptools import setup

#If you don't have a README.md you can delete these 2 line below
with open("README.md", "r", encoding="utf8") as fh:
    long_description = fh.read()

setup(
    name='name',
    version='0.1.0',
    description='Description of your package',
    py_modules=['name'],
    package_dir={'':'src'},
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url='https://github.com/...',
    author = "Your name",
    author_email = "Your email",
    license='name of your license',
    install_requires=[
          'numpy',
          'matplotlib',
          '...',
      ],
)
