from distutils.core import setup

setup(
    name="awssert",
    packages=["awssert"],
    version="0.0.1",
    license="Apache Software License 2.0",
    description="Declarative assertions for AWS",
    author="Tom Noble",
    author_email="t.s.noble@outlook.com",
    url="TODO",
    download_url="TODO",
    keywords=["aws", "pytest", "python", "testing"],
    install_requires=[
        "pytest",
        "boto3",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Framework :: AWS CDK",
        "Framework :: Pytest",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
)