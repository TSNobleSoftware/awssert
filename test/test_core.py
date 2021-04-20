import pytest

from awssert.prefixes import positives, negatives
from awssert.core import AssertionPrefixRouter, BotoObjectProxy
from awssert.exceptions import DisallowedPrefixOnMethodError


class MockClass:
    def __init__(self):
        self.foo_was_called = False

    @positives("should")
    @negatives("should_not")
    def foo(self, _, context):
        self.foo_was_called = True
        context["result"] = True


def test_assertion_prefix_router_calls_method_with_allowed_prefix():
    object = MockClass()
    router = AssertionPrefixRouter("should", object, BotoObjectProxy())
    router.foo()
    assert object.foo_was_called


def test_assertion_prefix_router_throws_error_with_disallowed_prefix():
    router = AssertionPrefixRouter("not_real", MockClass(), BotoObjectProxy())
    with pytest.raises(DisallowedPrefixOnMethodError):
        router.foo()
