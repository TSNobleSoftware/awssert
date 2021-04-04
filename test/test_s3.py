from moto import mock_s3
import boto3

import awssert


@mock_s3
def test_s3_bucket_contains_object_assertion():
    mock_bucket = boto3.resource("s3").Bucket("MockBucket")
    mock_bucket.create(CreateBucketConfiguration={"LocationConstraint": "eu-west-1"})
    mock_bucket.put_object(Key="foo", Body=b"123")
    mock_bucket.should.contain("foo")
    mock_bucket.should_not.contain("bar")
