# AWSsert

![GitHub Workflow Status](https://img.shields.io/github/workflow/status/TSNoble/awssert/Test)
![PyPI](https://img.shields.io/pypi/v/awssert)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/awssert)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

AWSsert is a Python library providing declarative assertions about AWS resources to your tests.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install AWSsert.

```bash
pip install awssert
```

## Usage

AWSsert attaches assertions directly to [boto3](https://github.com/boto/boto3) resource objects, allowing you to write clean and declarative tests:

```python
import boto3

def test_bucket_contains_object():
   bucket = boto3.resource("s3").Bucket("foo")
   assert bucket.should_not.contain("bar")
   bucket.put_object(Key="bar", Body=b"123")
   assert bucket.should_contain("bar")
```

AWSsert also works in tandem with [moto](https://pypi.org/project/moto/), enabling the same level of clarity to be applied on mock infrastructure:

```python
import boto3
import moto
import pytest

@pytest.fixture
def mock_s3():
   with moto.mock_s3():
      yield

def test_bucket_contains_object(mock_s3):
   bucket = boto3.resource("s3").Bucket("foo")
   assert bucket.should_not.contain("bar")
   bucket.put_object(Key="bar", Body=b"123")
   assert bucket.should_contain("bar")
```

Note that AWSsert currently does not work with usage of moto as a decorator

## Progress

| AWS Service | Resource Object | AWSsert Supported |
|-------------|-----------------|-------------------|
|CloudFormation|Event           |:x:                |
|             |Stack            |:x:                |
|             |StackResource            |:x:                |
|             |StackResourceSummary            |:x:                |
|CloudWatch   |Alarm            |:x:                |
|             |Metric            |:x:                |
|Glacier             |Account            |:x:                |
|             |Archive            |:x:                |
|             |Job            |:x:                |
|             |MultipartUpload            |:x:                |
|             |Notification            |:x:                |
|             |Vault            |:x:                |
|S3           |Bucket           |:white_check_mark: |
|DynamoDB     |Table            |:white_check_mark: |


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[Apache Software License 2.0](https://www.apache.org/licenses/LICENSE-2.0)