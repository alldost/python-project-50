# import pytest
from gendiff.modules.generate_diff import generate_diff

"""@pytest.fixture
def file1():
    with open('tests/fixtures/file1.json') as file1:
        yield file1

@pytest.fixture
def file2():
    with open('tests/fixtures/file2.json') as file2:
        yield file2

@pytest.fixture
def result():
    with open('tests/fixtures/generate_diff_result') as result:
        yield result"""


FILE1_JSON = 'tests/fixtures/file1.json'
FILE2_JSON = 'tests/fixtures/file2.json'
FILE1_YAML = 'tests/fixtures/file1.yml'
FILE2_YAML = 'tests/fixtures/file2.yaml'
RESULT = 'tests/fixtures/generated_diff.txt'


def test_generate_diff():
    with open(RESULT) as result:
        result_content = result.read()
        assert generate_diff(FILE1_JSON, FILE2_JSON) == result_content
        assert generate_diff(FILE1_YAML, FILE2_YAML) == result_content
