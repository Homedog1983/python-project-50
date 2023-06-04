import pytest
from gendiff.file_parser import get_dict_from_file
from tests.test_generate_diff import get_fixture_path


@pytest.mark.parametrize("file, result", [
    ('file1.json', 'dict_1.txt'),
    ('file2.json', 'dict_2.txt'),
    ('file1.yml', 'dict_1.txt'),
    ('file2.yml', 'dict_2.txt'),
    ('file1.yaml', 'dict_1.txt'),
    ('file2.yaml', 'dict_2.txt'),
    ('file2.yml', 'dict_2.txt'),
    ('file1.yaml', 'dict_1.txt'),
])
def test_get_dict_from_file(file, result):
    file_path, result_path = map(get_fixture_path, (file, result))
    with open(result_path) as result_file:
        result_expected = eval(result_file.read())
        assert get_dict_from_file(file_path) == result_expected


@pytest.mark.parametrize("file, result", [
    ('wrong.txt', 'wrong_format_message.txt'),
])
def test_exception(file, result):
    file_path, result_path = map(get_fixture_path, (file, result))
    with open(result_path) as result_file:
        result_expected = result_file.read()
    with pytest.raises(Exception) as e:
        get_dict_from_file(file_path)
    assert str(e.value) == result_expected
