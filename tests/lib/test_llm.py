import pytest
from unittest.mock import patch
from lib.llm import summarize, translate, reword, respond, MODELS

# Mock response class to simulate litellm responses
class MockResponse:
    class Choice:
        class Message:
            def __init__(self, content):
                self.content = content
        
        def __init__(self, content):
            self.message = self.Message(content)
    
    def __init__(self, content):
        self.choices = [self.Choice(content)]

@pytest.fixture
def mock_completion():
    with patch('lib.llm.completion') as mock:
        def side_effect(model, messages):
            # Return different responses based on the input
            text = messages[0]['content']
            if "Summarize" in text:
                return MockResponse("Test summary")
            elif "Translate" in text:
                return MockResponse("Překlad textu")
            elif "Change the following" in text:
                return MockResponse("Reworded text in sentences.")
            return MockResponse("Default response")
        
        mock.side_effect = side_effect
        yield mock


def test_respond(mock_completion):
    result = respond("Test message", "r1")
    assert isinstance(result, str)
    assert result == "Default response"
    mock_completion.assert_called_with(
        model=MODELS["r1"],
        messages=[{"content": "Test message", "role": "user"}]
    )

def test_models_configuration():
    assert MODELS["claude"] == "anthropic/claude-3-5-sonnet-20241022"
    assert MODELS["deepseek"] == "deepseek/deepseek-chat"
    assert MODELS["r1"] == "deepseek/deepseek-reasoner"
    assert len(MODELS) == 3

def test_summarize(mock_completion):
    test_text = "This is a test text to summarize."
    result = summarize(test_text)
    assert result == "Test summary"
    mock_completion.assert_called_with(
        model=MODELS["claude"],
        messages=[{"content": "\nSummarize the text. Return a well-formatted summary of the following text:\n" + test_text, "role": "user"}]
    )
def test_summarize(mock_completion):
    test_text = "This is a test text to summarize."
    result = summarize(test_text)
    assert result == "Test summary"
    mock_completion.assert_called_with(
        model=MODELS["claude"],
        messages=[{"content": "Summarize the text. Return a well-formatted summary of the following text:\n" + test_text, "role": "user"}]
    )

def test_translate(mock_completion):
    test_text = "Hello world"
    result = translate(test_text)
    assert result == "Překlad textu"
    expected_prompt = (
        "\nTranslate the following text to Czech:\n"
        "Do not mention any details besides the translation itself.\n"
        "Return all dates and numbers as words instead, as if the text were read by a person instead of written.\n"
        'Like: "The year 2022" -> "The year two thousand twenty-two" but in Czech ofcourse.\n'
        + test_text
    )
    mock_completion.assert_called_with(
        model=MODELS["r1"],
        messages=[{"content": expected_prompt, "role": "user"}]
    )
def test_translate(mock_completion):
    test_text = "Hello world"
    result = translate(test_text)
    assert result == "Překlad textu"
    expected_prompt = (
        "Translate the following text to Czech:\n"
        "Do not mention any details besides the translation itself.\n"
        "Return all dates and numbers as words instead, as if the text were read by a person instead of written.\n"
        'Like: "The year 2022" -> "The year two thousand twenty-two" but in Czech ofcourse.\n'
        + test_text
    )
    mock_completion.assert_called_with(
        model=MODELS["r1"],
        messages=[{"content": expected_prompt, "role": "user"}]
    )

def test_reword(mock_completion):
    test_text = "- point 1\n- point 2"
    result = reword(test_text)
    assert result == "Reworded text in sentences."
    mock_completion.assert_called_with(
        model=MODELS["r1"],
        messages=[{"content": "\nChange the following input text to be formed into sentences instead of points. It should be comprised of whole sentences, that are grammatically correct.\n" + test_text, "role": "user"}]
    )
def test_reword(mock_completion):
    test_text = "- point 1\n- point 2"
    result = reword(test_text)
    assert result == "Reworded text in sentences."
    mock_completion.assert_called_with(
        model=MODELS["r1"],
        messages=[{"content": "Change the following input text to be formed into sentences instead of points. It should be comprised of whole sentences, that are grammatically correct.\n" + test_text, "role": "user"}]
    )
