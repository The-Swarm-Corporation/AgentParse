# YamlOutputParser

import pytest
import re
from pydantic import BaseModel
from agentparse import YamlOutputParser


# Define a sample Pydantic model for testing
class MyModel(BaseModel):
    name: str
    age: int


# Test the initialization of YamlOutputParser
def test_yaml_output_parser_initialization():
    parser = YamlOutputParser(MyModel)
    assert parser.pydantic_object == MyModel
    assert isinstance(parser.pattern, re.Pattern)


# Test parsing without YAML code block
def test_parse_without_yaml_code_block():
    parser = YamlOutputParser(MyModel)
    text = "name: John\nage: 42"
    model = parser.parse(text)
    assert model.name == "John"
    assert model.age == 42


# Test parsing with no matching pattern
def test_parse_no_match_pattern():
    parser = YamlOutputParser(MyModel)
    text = "This is some random text without YAML."

    with pytest.raises(Exception) as exc_info:
        parser.parse(text)

    assert "Failed to parse MyModel" in str(exc_info.value)


# Test get_format_instructions method
def test_get_format_instructions():
    parser = YamlOutputParser(MyModel)
    instructions = parser.get_format_instructions()
    assert "YAML Formatting Instructions:" in instructions
    assert '"name": {"type": "string"}' in instructions
    assert '"age": {"type": "integer"}' in instructions
