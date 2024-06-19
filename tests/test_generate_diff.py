import pytest
from gendiff.generate_diff import generate_diff
from gendiff.formatters.stylish import stylish
from gendiff.formatters.plain import plain
from gendiff.formatters.json_ import to_json


JSON_FLAT1 = 'tests/fixtures/first_flat_file.json'
JSON_FLAT2 = 'tests/fixtures/second_flat_file.json'
YAML_FLAT1 = 'tests/fixtures/first_flat_file.yml'
YAML_FLAT2 = 'tests/fixtures/second_flat_file.yaml'

JSON_NESTED1 = 'tests/fixtures/first_nested_file.json'
JSON_NESTED2 = 'tests/fixtures/second_nested_file.json'
YAML_NESTED1 = 'tests/fixtures/first_nested_file.yml'
YAML_NESTED2 = 'tests/fixtures/second_nested_file.yaml'

STYLISHED_FLAT_RESULT = 'tests/fixtures/stylished_flat_diff.txt'
STYLISHED_NESTED_RESULT = 'tests/fixtures/stylished_nested_diff.txt'
PLAINED_RESULT = 'tests/fixtures/plained_diff.txt'
JSON_FLAT_RESULT = 'tests/fixtures/flat_diff.json'
JSON_NESTED_RESULT = 'tests/fixtures/nested_diff.json'

STYLISH_INPUT = [
    (JSON_FLAT1, JSON_FLAT2, stylish, STYLISHED_FLAT_RESULT),
    (YAML_FLAT1, YAML_FLAT2, stylish, STYLISHED_FLAT_RESULT),
    (JSON_NESTED1, JSON_NESTED2, stylish, STYLISHED_NESTED_RESULT),
    (YAML_NESTED1, YAML_NESTED2, stylish, STYLISHED_NESTED_RESULT)
]

PLAIN_INPUT = [
    (JSON_NESTED1, JSON_NESTED2, plain, PLAINED_RESULT),
    (YAML_NESTED1, YAML_NESTED2, plain, PLAINED_RESULT)
]

JSON_INPUT = [
    (JSON_FLAT1, JSON_FLAT2, to_json, JSON_FLAT_RESULT),
    (YAML_FLAT1, YAML_FLAT2, to_json, JSON_FLAT_RESULT),
    (JSON_NESTED1, JSON_NESTED2, to_json, JSON_NESTED_RESULT),
    (YAML_NESTED1, YAML_NESTED2, to_json, JSON_NESTED_RESULT)
]

TEST_INPUT = STYLISH_INPUT + PLAIN_INPUT + JSON_INPUT


@pytest.mark.parametrize("file1, file2, formater, result", TEST_INPUT)
def test_generate_diff(file1, file2, formater, result):
    with open(result) as result:
        expected = result.read()
        assert generate_diff(file1, file2, formater) == expected
