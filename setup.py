from setuptools import setup, find_packages
from pathlib import Path

version = "0.0.6"
here = Path(__file__).parent.resolve()

with open(here.joinpath("README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="awssert",
    version=version,
    description="Declarative assertions for AWS",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/TSNoble/awssert",
    author="Tom Noble",
    author_email="t.s.noble@outlook.com",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Framework :: AWS CDK",
        "Framework :: Pytest",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    keywords=["aws", "python", "pytest", "boto3", "testing"],
    packages=find_packages(),
    python_requires=">=3.5",
    install_requires=[
        "pytest",
        "boto3",
    ],
    entry_points={"pytest11": ["name_of_plugin = awssert"]},
    project_urls={
        "Bug Reports": "https://github.com/TSNoble/awssert/issues",
        "Source": "https://github.com/TSNoble/awssert",
    }
)
