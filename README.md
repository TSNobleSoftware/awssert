# AWSsert

![GitHub Workflow Status](https://img.shields.io/github/workflow/status/TSNobleSoftware/awssert/Test)
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

Installing the package will make AWSserts extra assertions available to all of your tests. Assertions are attached directly to [boto3](https://github.com/boto/boto3) resource objects, allowing you to write clean and declarative tests:

```python
import boto3

def test_bucket_contains_object():
   bucket = boto3.resource("s3").Bucket("foo")
   assert bucket.should_not.contain("bar")
   bucket.put_object(Key="bar", Body=b"123")
   assert bucket.should.contain("bar")
```

AWSsert also works in tandem with [moto](https://pypi.org/project/moto/), enabling the same level of clarity to be applied on mock infrastructure:

```python
import boto3
from moto import mock_s3

@mock_s3
def test_mock_bucket_contains_object():
   bucket = boto3.resource("s3").Bucket("foo")
   assert bucket.should_not.contain("bar")
   bucket.put_object(Key="bar", Body=b"123")
   assert bucket.should.contain("bar")
```

## Progress

| AWS Service | Resource Object             | AWSsert Supported |
|-------------|-----------------------------|-------------------|
|CloudFormation|Event                       |:x:                |
|             |Stack                        |:x:                |
|             |StackResource                |:x:                |
|             |StackResourceSummary         |:x:                |
|CloudWatch   |Alarm                        |:x:                |
|             |Metric                       |:x:                |
|DynamoDB     |Table                        |:white_check_mark: |
|EC2          |ClassicAddress               |:x:                |
|             |DhcpOptions                  |:x:                |
|             |Image                        |:x:                |
|             |Instance                     |:x:                |
|             |InternetGateway              |:x:                |
|             |KeyPair                      |:x:                |
|             |KeyPairInfo                  |:x:                |
|             |NetworkAcl                   |:x:                |
|             |NetworkInterface             |:x:                |
|             |NetworkInterfaceAssociation  |:x:                |
|             |PlacementGroup               |:x:                |
|             |Route                        |:x:                |
|             |RouteTable                   |:x:                |
|             |RouteTableAssociation        |:x:                |
|             |SecurityGroup                |:x:                |
|             |Snapshot                     |:x:                |
|             |Subnet                       |:x:                |
|             |Tag                          |:x:                |
|             |Volume                       |:x:                |
|             |Vpc                          |:x:                |
|             |VpcPeeringConnection         |:x:                |
|             |VpcAddress                   |:x:                |
|Glacier      |Account                      |:x:                |
|             |Archive                      |:x:                |
|             |Job                          |:x:                |
|             |MultipartUpload              |:x:                |
|             |Notification                 |:x:                |
|             |Vault                        |:x:                |
|IAM          |AccessKey                    |:x:                |
|             |AccessKeyPair                |:x:                |
|             |AccountPasswordPolicy        |:x:                |
|             |AccountSummary               |:x:                |
|             |AssumeRolePolicy             |:x:                |
|             |CurrentUser                  |:x:                |
|             |Group                        |:white_check_mark: |
|             |GroupPolicy                  |:x:                |
|             |InstanceProfile              |:x:                |
|             |LoginProfile                 |:x:                |
|             |MfaDevice                    |:x:                |
|             |Policy                       |:white_check_mark: |
|             |PolicyVersion                |:x:                |
|             |Role                         |:white_check_mark: |
|             |RolePolicy                   |:x:                |
|             |SamlProvider                 |:x:                |
|             |ServerCertificate            |:x:                |
|             |SigningCertificate           |:x:                |
|             |User                         |:white_check_mark: |
|             |UserPolicy                   |:x:                |
|             |VirtualMfaDevice             |:x:                |
|OpsWorks     |Layer                        |:x:                |
|             |Stack                        |:x:                |
|             |StackSummary                 |:x:                |
|S3           |Bucket                       |:white_check_mark: |
|             |BucketAcl                    |:x:                |
|             |BucketCors                   |:x:                |
|             |BucketLifecycle              |:x:                |
|             |BucketLifecycleConfiguration |:x:                |
|             |BucketLogging                |:x:                |
|             |BucketNotification           |:x:                |
|             |BucketPolicy                 |:x:                |
|             |BucketRequestPayment         |:x:                |
|             |BucketTagging                |:x:                |
|             |BucketVersioning             |:x:                |
|             |BucketWebsite                |:x:                |
|             |MultipartUpload              |:x:                |
|             |MultipartUploadPart          |:x:                |
|             |Object                       |:x:                |
|             |ObjectAcl                    |:x:                |
|             |ObjectSummary                |:x:                |
|             |ObjectVersion                |:x:                |
|SNS          |PlatformApplication          |:x:                |
|             |PlatformEndpoint             |:x:                |
|             |Subscription                 |:x:                |
|             |Topic                        |:white_check_mark: |
|SQS          |Message                      |:x:                |
|             |Queue                        |:x:                |


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

A full [contribution guide](CONTRIBUTING.md) and [code of conduct](CODE_OF_CONDUCT.md) are supplied with the repository. In essence, update the unit tests and changelog, and treat fellow users with respect!

## License
[Apache Software License 2.0](https://www.apache.org/licenses/LICENSE-2.0)
