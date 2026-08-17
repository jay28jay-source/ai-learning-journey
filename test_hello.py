"""Tests for the first Python program."""

import unittest

from hello import MESSAGE_LINES, build_message


class BuildMessageTests(unittest.TestCase):
    """Verify the learning message remains complete."""

    def test_message_contains_every_line(self) -> None:
        self.assertEqual(build_message(), "\n".join(MESSAGE_LINES))

    def test_message_mentions_ai_journey(self) -> None:
        self.assertIn("AI engineering journey", build_message())


if __name__ == "__main__":
    unittest.main()

