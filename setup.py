import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='nepali_roman',
    version='1.1',
    author="Suraj Regmi",
    author_email="regmi125@gmail.com",
    description="Convert Nepali text to roman English",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Suraj1127/nepali-roman",
    packages=setuptools.find_packages(),
    py_modules=["romanize"],
    classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
)
