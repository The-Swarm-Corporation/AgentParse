# YamlModel

from agentparse import YamlModel


# Test the to_yaml method
def test_to_yaml():
    user = YamlModel(
        input_dict={"name": "Alice", "age": 30, "is_active": True}
    )
    yaml_output = user.to_yaml()
    assert "name: Alice" in yaml_output
    assert "age: 30" in yaml_output
    assert "is_active: true" in yaml_output


# Test the from_yaml method
def test_from_yaml():
    yaml_str = "name: Bob\nage: 25\nis_active: false"
    user_instance = YamlModel.from_yaml(YamlModel, yaml_str)
    assert user_instance.input_dict["name"] == "Bob"
    assert user_instance.input_dict["age"] == 25
    assert user_instance.input_dict["is_active"] is False


# Test from_yaml with invalid YAML
def test_from_yaml_invalid():
    invalid_yaml_str = "name: Bob\nage: twenty-five\nis_active: false"
    user_instance = YamlModel.from_yaml(YamlModel, invalid_yaml_str)
    assert user_instance is None


# Test the json_to_yaml method
def test_json_to_yaml():
    json_string = '{"name": "Charlie", "age": 28, "is_active": true}'
    yaml_output = YamlModel.json_to_yaml(json_string)
    assert "name: Charlie" in yaml_output
    assert "age: 28" in yaml_output
    assert "is_active: true" in yaml_output


# Test the save_to_yaml method
def test_save_to_yaml(tmp_path):
    user = YamlModel(
        input_dict={"name": "Alice", "age": 30, "is_active": True}
    )
    yaml_file = tmp_path / "user.yaml"
    user.save_to_yaml(str(yaml_file))

    # Check if the file was created and contains the correct data
    with open(yaml_file) as f:
        content = f.read()
        assert "name: Alice" in content
        assert "age: 30" in content
        assert "is_active: true" in content


# Test the create_yaml_schema_from_dict method
def test_create_yaml_schema_from_dict():
    data = {"name": "Alice", "age": 30, "is_active": True}
    schema = YamlModel.create_yaml_schema_from_dict(data, YamlModel)
    assert "name:" in schema
    assert "age:" in schema
    assert "is_active:" in schema


# Test the yaml_to_dict method
def test_yaml_to_dict():
    yaml_str = "name: Bob\nage: 25\nis_active: false"
    result = YamlModel.yaml_to_dict(yaml_str)
    assert result["name"] == "Bob"
    assert result["age"] == 25
    assert result["is_active"] is False


# Test the dict_to_yaml method
def test_dict_to_yaml():
    data = {"name": "Alice", "age": 30, "is_active": True}
    yaml_output = YamlModel.dict_to_yaml(data)
    assert "name: Alice" in yaml_output
    assert "age: 30" in yaml_output
    assert "is_active: true" in yaml_output
