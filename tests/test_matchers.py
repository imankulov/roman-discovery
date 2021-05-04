import pytest

from roman_discovery.matchers import MatchByCallableAttribute, MatchByPattern


@pytest.mark.parametrize(
    "patterns, package, result",
    [
        (["*.bar"], "foo.bar", True),
        (["*.bar.*"], "foo.bar", False),
        (["*.bar", "*.bar.*"], "foo.bar", True),
    ],
)
def test_match_by_pattern_should_return_relevant_packages(patterns, package, result):
    matcher = MatchByPattern(patterns)
    assert matcher(package) == result


@pytest.mark.parametrize(
    "attribute, obj, result",
    [
        ("strip", "", True),  # instances match
        ("strip", str, False),  # classes don't match
        ("foo", "", False),  # non-existent attribute
    ],
)
def test_match_by_callable_attribute_should_return_relevant_objects(
    attribute, obj, result
):
    matcher = MatchByCallableAttribute(attribute)
    assert matcher(obj) == result
