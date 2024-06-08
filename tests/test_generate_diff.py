import pytest
from gendiff.generate_diff import generate_diff


JSON_FLAT1 = 'tests/fixtures/first_flat_file.json'
JSON_FLAT2 = 'tests/fixtures/second_flat_file.json'
YAML_FLAT1 = 'tests/fixtures/first_flat_file.yml'
YAML_FLAT2 = 'tests/fixtures/second_flat_file.yaml'
FLAT_RESULT = 'tests/fixtures/flat_diff.txt'

JSON_NESTED1 = 'tests/fixtures/first_nested_file.json'
JSON_NESTED2 = 'tests/fixtures/second_nested_file.json'
YAML_NESTED1 = 'tests/fixtures/first_nested_file.yml'
YAML_NESTED2 = 'tests/fixtures/second_nested_file.yaml'
NESTED_RESULT = 'tests/fixtures/nested_diff.txt'

PARAMETRIZE_INPUT = [
    (JSON_FLAT1, JSON_FLAT2, FLAT_RESULT),
    (YAML_FLAT1, YAML_FLAT2, FLAT_RESULT),
    (JSON_NESTED1, JSON_NESTED2, NESTED_RESULT),
    (YAML_NESTED1, YAML_NESTED2, NESTED_RESULT),
]


@pytest.mark.parametrize("file1,file2,result", PARAMETRIZE_INPUT)
def test_generate_diff(file1, file2, result):
    with open(result) as result:
        expected = result.read()
        assert generate_diff(file1, file2) == expected
