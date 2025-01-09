import unittest
from celery_app import app
from tasks import get_claude_response

class TestIntegration(unittest.TestCase):
    def setUp(self):
        self.celery_app = app
        self.celery_app.conf.update(CELERY_ALWAYS_EAGER=True)

    def test_get_claude_response_integration(self):
        # Arrange
        test_prompt = "What is the capital of France?"

        # Act
        result = get_claude_response.delay(test_prompt)

        # Assert
        self.assertIsNotNone(result.get())
        self.assertIsInstance(result.get(), str)
        self.assertGreater(len(result.get()), 0)

if __name__ == '__main__':
    unittest.main()