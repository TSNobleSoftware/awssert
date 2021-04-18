from functools import partial

import mock
import pytest
import boto3

from awssert.core import (
    BotoObjectProxy,
    BotoObjectProxyRegister,
    AssertionPrefixRouter,
)
from awssert.prefixes import AssertionPrefixes
from awssert.s3 import BucketAssertions
from awssert.dynamodb import TableAssertions
from awssert.iam import (
    UserAssertions,
    PolicyAssertions,
    GroupAssertions,
    RoleAssertions,
)
from awssert.sns import TopicAssertions

ASSERTIONS = [
    BucketAssertions(),
    TableAssertions(),
    UserAssertions(),
    PolicyAssertions(),
    GroupAssertions(),
    RoleAssertions(),
    TopicAssertions(),
]


def attach_assertions_to_session(session, assertions):
    def register(assertion, class_attributes, base_classes, **kwargs):
        proxy = BotoObjectProxy()
        base_classes.insert(0, BotoObjectProxyRegister)
        class_attributes["proxy"] = proxy
        for prefix in AssertionPrefixes.get_prefixes(type(assertion)):
            class_attributes[prefix] = AssertionPrefixRouter(prefix, assertion, proxy)

    for assertion in assertions:
        session.events.register(
            f"creating-resource-class.{assertion.attaches_to}",
            partial(register, assertion),
        )


def resource_with_assertions(*args, **kwargs):
    session = boto3.Session()
    attach_assertions_to_session(session, ASSERTIONS)
    return session.resource(*args, **kwargs)


resource_patcher = mock.patch("boto3.resource", resource_with_assertions)


@pytest.hookimpl
def pytest_sessionstart():
    resource_patcher.start()


@pytest.hookimpl
def pytest_sessionfinish():
    resource_patcher.stop()
