#import pytest
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


FILE1 = 'tests/fixtures/file1.json'
FILE2 = 'tests/fixtures/file2.json'
RESULT = 'tests/fixtures/generated_diff.txt'


def test_generate_diff():
    with open(RESULT) as result:
        result_content = result.read()
        assert generate_diff(FILE1, FILE2) == result_content
