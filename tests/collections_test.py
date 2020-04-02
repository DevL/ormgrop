import pytest

from src.ormgrop.collections import get_in, require_in, NestedValueNotFoundError


TESTS_WITHOUT_SPECIFIED_DEFAULT_VALUE = {
    "empty path returns None": ({}, [], None),
    "empty collection returns None": ({}, ["some", "path"], None),
    "an existing path returns the found value": (
        {"some": {"key": "value"}},
        ["some", "key"],
        "value",
    ),
    "a wrong path returns None": ({"some": {"other": "value"}}, ["some", "key"], None),
    "a nested list can be indexed": (
        {"some": {"list": ["value"]}},
        ["some", "list", 0],
        "value",
    ),
    "an out of bound list index returns None": (
        {"some": {"list": []}},
        ["some", "list", 0],
        None,
    ),
    "an illegal list index returns None": (
        {"some": {"list": []}},
        ["some", "list", "not_an_index"],
        None,
    ),
    "a string as nested collection returns None": (
        "a string which is technically a list",
        ["some", "value"],
        None,
    ),
    "a string with a single index as path returns that substring": (
        "a string which is technically a list",
        [0],
        "a",
    ),
}


@pytest.mark.parametrize(
    "collection, path, expected",
    TESTS_WITHOUT_SPECIFIED_DEFAULT_VALUE.values(),
    ids=list(TESTS_WITHOUT_SPECIFIED_DEFAULT_VALUE.keys()),
)
def test_get_in_without_specified_default_value(collection, path, expected):
    assert get_in(collection, path) == expected


TESTS_WITH_SPECIFIED_DEFAULT_VALUE = {
    "empty path returns the default value": ({}, [], "default", "default"),
    "empty collection returns the default value": (
        {},
        ["some", "path"],
        "default",
        "default",
    ),
    "a wrong path returns the default value": (
        {"some": {"other": "value"}},
        ["some", "key"],
        "default",
        "default",
    ),
    "a wrong list index returns the default value": (
        {"some": {"list": []}},
        ["some", "list", 0],
        "default",
        "default",
    ),
    "an illegal list index returns the default value": (
        {"some": {"list": []}},
        ["some", "list", "not_an_index"],
        "default",
        "default",
    ),
    "a string as nested collection returns the default value": (
        "a string which is technically a list",
        ["some", "value"],
        "default",
        "default",
    ),
}


@pytest.mark.parametrize(
    "collection, path, default, expected",
    TESTS_WITH_SPECIFIED_DEFAULT_VALUE.values(),
    ids=list(TESTS_WITH_SPECIFIED_DEFAULT_VALUE.keys()),
)
def test_get_in_with_specified_default_value(collection, path, default, expected):
    assert get_in(collection, path, default) == expected


TESTS_THAT_RAISES = {
    "empty path raises": ({}, [], "not found"),
    "empty collection raises": ({}, ["some", "path"], "not found"),
    "a wrong path raises": ({"some": {"other": "value"}}, ["some", "key"], "not found"),
    "an out of bound list index raises": (
        {"some": {"list": []}},
        ["some", "list", 0],
        "not found",
    ),
    "an illegal list index raises": (
        {"some": {"list": []}},
        ["some", "list", "not_an_index"],
        "not found",
    ),
    "a string as nested collection raises": (
        "a string which is technically a list",
        ["some", "value"],
        "not found",
    ),
}


@pytest.mark.parametrize(
    "collection, path, expected_error",
    TESTS_THAT_RAISES.values(),
    ids=list(TESTS_THAT_RAISES.keys()),
)
def test_require_in_raises(collection, path, expected_error):
    with pytest.raises(NestedValueNotFoundError) as error_info:
        require_in(collection, path)
    assert expected_error in str(error_info.value)
