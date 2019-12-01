import pytest
from dosym import inputs

def test_toml_file_parser_good_file():
    file = "tests/good_toml_input.toml"
    assert type(inputs.toml_file_parser(file)) == dict

def test_toml_file_parser_bad_file():
    file = "tests/bad_toml_input.toml"
    with pytest.raises(Exception) as e:
        inputs.toml_file_parser(file)

