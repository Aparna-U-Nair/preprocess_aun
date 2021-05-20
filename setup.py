import setuptools

with open("README.md","r") as file:
    file_desc = file.read()

setuptools.setup(
    name = "preprocess_aun",
    version = 0.0.1,
    author = "Aparna",
    author_email = "nairaparna@gmail.com",
    description = "Text preprocessing package",
    long_description = file_desc,
    long_description_content_type = "text/markdown",
    packages = setuptools.find_packages(),
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Aproved :: MIT License",
        "Operating System :: OS Independent"
    ],
    python_requires = ">=3.5"

)