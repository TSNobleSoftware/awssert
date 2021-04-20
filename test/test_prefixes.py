from awssert.prefixes import AssertionPrefixes, positives, negatives


class MockClass:
    @positives("should")
    @negatives("should_not")
    def foo(self):
        pass


def test_get_positives():
    assert AssertionPrefixes.get_positives(MockClass) == ["should"]


def test_get_negatives():
    assert AssertionPrefixes.get_negatives(MockClass) == ["should_not"]


def test_get_prefixes():
    assert AssertionPrefixes.get_prefixes(MockClass) == ["should", "should_not"]


def test_get_methods_allowing_prefix():
    assert AssertionPrefixes.get_methods_allowing_prefix(MockClass, "should") == {
        "foo": MockClass.foo
    }
    assert AssertionPrefixes.get_methods_allowing_prefix(MockClass, "should_not") == {
        "foo": MockClass.foo
    }
    assert (
        AssertionPrefixes.get_methods_allowing_prefix(MockClass, "not_a_real_prefix")
        == {}
    )
