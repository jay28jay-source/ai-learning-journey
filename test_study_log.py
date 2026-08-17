"""Tests for JSON study-log storage."""

import tempfile
import unittest
from pathlib import Path

from practice.study_log import load_entries, save_entries, total_minutes


class StudyLogTests(unittest.TestCase):
    def test_round_trip_preserves_entries(self) -> None:
        entries = [
            {"topic": "Python JSON", "minutes": 30, "completed": True},
            {"topic": "Git basics", "minutes": 20, "completed": False},
        ]
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "study_log.json"
            save_entries(entries, path)
            self.assertEqual(load_entries(path), entries)

    def test_missing_file_returns_empty_list(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "missing.json"
            self.assertEqual(load_entries(path), [])

    def test_total_minutes_adds_every_entry(self) -> None:
        entries = [
            {"topic": "Python", "minutes": 25, "completed": True},
            {"topic": "Git", "minutes": 35, "completed": True},
        ]
        self.assertEqual(total_minutes(entries), 60)

    def test_invalid_top_level_json_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "invalid.json"
            path.write_text('{"topic": "not a list"}', encoding="utf-8")
            with self.assertRaises(ValueError):
                load_entries(path)


if __name__ == "__main__":
    unittest.main()

