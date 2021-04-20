from setuptools import setup, find_packages
from pathlib import Path

version = "1.0.0"
here = Path(__file__).parent.resolve()

with open(here.joinpath("README.md"), encoding="utf-8") as f:
    long_description = f.read()

with open(here.joinpath("requirements.txt"), encoding="utf-8") as f:
    requirements = f.readlines()

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
        "Development Status :: 4 - Beta",
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
    python_requires=">=3.6",
    install_requires=[requirements],
    entry_points={"pytest11": ["name_of_plugin = awssert"]},
    project_urls={
        "Bug Reports": "https://github.com/TSNobleSoftware/awssert/issues",
        "Source": "https://github.com/TSNobleSoftware/awssert",
    }
)
