from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.8'
DESCRIPTION = 'CodeMe - Automatic Python Coder'
LONG_DESCRIPTION = 'A python package which automatically codes for you.'

# Setting up
setup(
    name="codeme",
    version=VERSION,
    author="Neetish Singh(AAYS Anaytics)",
    author_email="<neetishsingh97@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['requests'],
    keywords=['python', 'pyspark','spark','ingestion','data','dataframe','analysis','schema','pandas','chatgpt','auto','bot'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)