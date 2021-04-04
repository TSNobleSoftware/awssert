import pytest
import boto3

from awssert.s3 import register_s3_assertions


@pytest.fixture
def awssert():
    boto3._get_default_session().events.register(
        'creating-resource-class.s3.Bucket', register_s3_assertions
    )
