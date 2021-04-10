import moto
import boto3


@moto.mock_s3
def test_s3_bucket_contains_object_assertion():
    bucket = boto3.resource("s3").Bucket("mock")
    bucket.create(CreateBucketConfiguration={"LocationConstraint": "eu-west-1"})
    bucket.put_object(Key="foo", Body=b"123")
    assert bucket.should.contain("foo")
    assert bucket.does.contain("foo")
    assert bucket.should_not.contain("bar")
    assert bucket.does_not.contain("bar")


@moto.mock_s3
def test_s3_bucket_empty_assertion():
    bucket = boto3.resource("s3").Bucket("mock")
    bucket.create(CreateBucketConfiguration={"LocationConstraint": "eu-west-1"})
    assert bucket.should_be.empty()
    bucket.put_object(Key="foo", Body=b"123")
    assert bucket.should_not_be.empty()


@moto.mock_s3
def test_s3_bucket_exists_assertion():
    bucket = boto3.resource("s3").Bucket("mock")
    assert bucket.should_not.exist()
    assert bucket.does_not.exist()
    bucket.create(CreateBucketConfiguration={"LocationConstraint": "eu-west-1"})
    assert bucket.should.exist()
    assert bucket.does.exist()
