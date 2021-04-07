# Contribution Guide

## Getting set up

Start by creating a fork of the repository and pulling down the code. The project's tests can be run using pytest:

```shell script
pip install -r requirements-test.txt
pytest test/
```

Linting tools are also provided and can be run through the command line:

```shell script
pip install -r requirements-dev.txt
black --check awssert/ test/
flake8 awssert/ test/
```



## Making changes

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change. When adding new assertions, please add a new test demonstrating positive and negative usage.

Make sure your code is properly formatted before submitting a pull request!

```
black awssert/ test
```

## Updating the changelog

When making changes, please add a short *human-readable* description of the change to the latest (unreleased) entry in the changelog. Changes should be added under the relevant category:

### :sparkles: Added

- New code features go here

### :pencil2: Changed

- Changes to existing code features go here

### :scissors: Removed

- Removals of code features go here

### :books: Documentation

- Changes to documentation go here

### :hammer_and_wrench: Fixes

- Bugfixes go here

### :bug: Known bugs

- Identifed (unresolved) bugs go here

If you are planning to release a new version of AWSsert, don't worry about adding dates or a new version to the changelog. [Zest](https://pypi.org/project/zest.releaser/) will handle that!
## Releasing a new version

AWSsert uses [Zest](https://pypi.org/project/zest.releaser/) and Github Actions to automate the release process. In order to do so, manually run the Release workflow from the base repository. This will add the current date to the changelog, build and publish artifacts to PyPI, and bump the version number in all the places that matter.