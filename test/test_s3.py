import pytest
import moto
import boto3
from awssert.fixture import awssert


@pytest.fixture
def mock_s3():
    with moto.mock_s3():
        yield


def test_s3_bucket_contains_object_assertion(mock_s3, awssert):
    bucket = boto3.resource("s3").Bucket("mock")
    bucket.create(CreateBucketConfiguration={"LocationConstraint": "eu-west-1"})
    bucket.put_object(Key="foo", Body=b"123")
    bucket.should.contain("foo")
    bucket.does.contain("foo")
