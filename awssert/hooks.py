import pytest
import boto3

from awssert.s3 import register_s3_assertions
from awssert.dynamodb import register_dynamodb_assertions


@pytest.hookimpl
def pytest_runtest_call():
    default_session = boto3._get_default_session()
    default_session.events.register(
        "creating-resource-class.s3.Bucket", register_s3_assertions
    )
    default_session.events.register(
        "creating-resource-class.dynamodb.Table", register_dynamodb_assertions
    )
