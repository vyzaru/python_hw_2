import pytest
from func_to_test import merge_and_write

@pytest.fixture
def test_files(tmp_path):
    file_inp_1 = tmp_path / 'file_inp_1.txt'
    file_inp_2 = tmp_path / 'file_inp_2.txt'
    with open(file_inp_1, 'w') as file1:
        file1.write('homework')
    with open(file_inp_2, 'w') as file2:
        file2.write('six')
    file_outp = tmp_path / 'output.txt'

    return file_inp_1, file_inp_2, file_outp

def test_output_content(test_files):
    file_1, file_2, file_output = test_files
    assert merge_and_write(file_1, file_2, file_output) == 'homework six'

def test_exist_files(test_files):
    file_1, file_2, output_file = test_files
    assert merge_and_write(file_1, 'test_file.txt', output_file) == "Один из файлов не найден"
    assert merge_and_write('test_file.txt', file_2, output_file) == "Один из файлов не найден"
    assert merge_and_write('test_file1.txt', 'test_file2.txt', output_file) == "Один из файлов не найден"


