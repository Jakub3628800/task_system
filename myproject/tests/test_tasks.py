import pytest
from unittest.mock import patch, mock_open
from myproject.tasks.example_tasks import read_prompt_and_save, example_task

def test_example_task():
    assert example_task(2, 3) == 5

@pytest.fixture
def mock_file_content():
    return "Test prompt"

@patch("builtins.open", new_callable=mock_open)
def test_read_prompt_and_save(mock_file, mock_file_content):
    mock_file.return_value.__enter__.return_value.read.return_value = mock_file_content

    result = read_prompt_and_save()

    assert result == f"Processed prompt: {mock_file_content}"
    mock_file.assert_any_call('/workspace/taskai/myproject/prompts/input_prompt.txt', 'r')
    mock_file.assert_any_call('/workspace/taskai/myproject/prompts/output_result.txt', 'w')
    mock_file().write.assert_called_once_with(f"Processed prompt: {mock_file_content}")