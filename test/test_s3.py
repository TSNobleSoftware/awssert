import moto
import boto3


@moto.mock_s3
def test_s3_bucket_contains_object_assertion():
    bucket = boto3.resource("s3").Bucket("mock")
    good_object = boto3.resource("s3").Object(bucket.name, "foo")
    bad_object = boto3.resource("s3").Object(bucket.name, "bar")
    bucket.create(CreateBucketConfiguration={"LocationConstraint": "eu-west-1"})
    bucket.put_object(Key="foo", Body=b"123")
    bucket.should.contain(good_object)
    bucket.should.contain(good_object.key)
    bucket.does.contain(good_object)
    bucket.does.contain(good_object.key)
    bucket.should_not.contain(bad_object)
    bucket.should_not.contain(bad_object.key)
    bucket.does_not.contain(bad_object)
    bucket.does_not.contain(bad_object.key)


@moto.mock_s3
def test_s3_bucket_is_empty_assertion():
    bucket = boto3.resource("s3").Bucket("mock")
    bucket.create(CreateBucketConfiguration={"LocationConstraint": "eu-west-1"})
    bucket.should_be.empty()
    bucket.put_object(Key="foo", Body=b"123")
    bucket.should_not_be.empty()


@moto.mock_s3
def test_s3_bucket_exists_assertion():
    bucket = boto3.resource("s3").Bucket("mock")
    bucket.should_not.exist()
    bucket.does_not.exist()
    bucket.create(CreateBucketConfiguration={"LocationConstraint": "eu-west-1"})
    bucket.should.exist()
    bucket.does.exist()
