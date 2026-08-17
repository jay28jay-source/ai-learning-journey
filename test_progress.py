"""Tests for the learning-progress calculator."""

import unittest

from practice.progress import progress_summary


class ProgressSummaryTests(unittest.TestCase):
    def test_formats_progress_as_percentage(self) -> None:
        self.assertEqual(progress_summary(3, 5), "已完成 3/5 项（60%）")

    def test_accepts_zero_completed_tasks(self) -> None:
        self.assertEqual(progress_summary(0, 4), "已完成 0/4 项（0%）")

    def test_rejects_impossible_progress(self) -> None:
        with self.assertRaises(ValueError):
            progress_summary(6, 5)

    def test_rejects_zero_total(self) -> None:
        with self.assertRaises(ValueError):
            progress_summary(0, 0)


if __name__ == "__main__":
    unittest.main()

