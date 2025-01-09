import unittest
from unittest.mock import patch, MagicMock
from tasks import get_claude_response

class TestTasks(unittest.TestCase):
    @patch('tasks.claude_api')
    def test_get_claude_response(self, mock_claude_api):
        # Arrange
        mock_claude_api.get_response.return_value = "Mocked response"
        test_prompt = "Test prompt"

        # Act
        result = get_claude_response(test_prompt)

        # Assert
        mock_claude_api.get_response.assert_called_once_with(test_prompt)
        self.assertEqual(result, "Mocked response")

if __name__ == '__main__':
    unittest.main()