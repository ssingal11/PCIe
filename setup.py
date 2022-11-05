from setuptools import setup, find_packages

VERSION = '0.1.0'
DESCRIPTION = 'Simple Python module to access PCIe devices'
with open("README.md", "r", encoding="utf-8") as fh:
    LONG_DESCRIPTION = fh.read()

# Setting up
setup(
    name="pyPCIe",
    version=VERSION,
    author="Shivam Singal",
    author_email="<ssingal@nvidia.com>",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    url="https://github.com/ssingal11/PCIe",
    install_requires=[],
    keywords=['python', 'pcie'],
    classifiers= [
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: NVIDIA License",
        "Operating System :: POSIX :: Linux",
    ]
)
