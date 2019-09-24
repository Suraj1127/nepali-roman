import setuptools

setuptools.setup(
    name='nepali_roman',
    version='0.43',
    author="Suraj Regmi",
    author_email="regmi125@gmail.com",
    description="Convert Nepali text to roman English",
    long_description="Convert Nepali text to roman English",
    url="https://github.com/Suraj1127/nepali-roman",
    packages=setuptools.find_packages(),
    py_modules=["romanize"],
    classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
)
