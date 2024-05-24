from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="s3-logger",
    version="0.1.0",
    author="George Alvarez",
    author_email="alvarez@wjh.harvard.edu",
    description="An s3 logger for experiment results",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/harvard-visionlab/s3-logger",
    packages=find_packages(),
    install_requires=[
        "boto3>=1.34.0",
        "pandas",
        "torchvision",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
