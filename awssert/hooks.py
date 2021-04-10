import mock

import pytest
import boto3

from awssert.s3 import register_s3_assertions
from awssert.dynamodb import register_dynamodb_assertions


def attach_assertions_to_session(session):
    session.events.register("creating-resource-class.s3.Bucket", register_s3_assertions)
    session.events.register(
        "creating-resource-class.dynamodb.Table", register_dynamodb_assertions
    )


def resource_with_assertions(*args, **kwargs):
    session = boto3.Session()
    attach_assertions_to_session(session)
    return session.resource(*args, **kwargs)


resource_patcher = mock.patch("boto3.resource", resource_with_assertions)


@pytest.hookimpl
def pytest_sessionstart():
    resource_patcher.start()


@pytest.hookimpl
def pytest_sessionfinish():
    resource_patcher.stop()
