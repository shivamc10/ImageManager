import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


def read_requires():
    requirement = list()
    with open('requirement.txt', 'r') as f:
        requirement.append(f.readline())
    return requirement


setuptools.setup(
    name="ImageManager", # Replace with your own username
    version="0.0.1",
    author="Shivam Choubey",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/shivamc10/ImageManager",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3"
    ],
    python_requires='>=3.6',
    install_requires=read_requires()
)

# python3 setup.py sdist bdist_wheel