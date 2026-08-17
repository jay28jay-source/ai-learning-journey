"""Save and load a small study log as JSON."""

from __future__ import annotations

import json
from pathlib import Path
from typing import TypedDict


class StudyEntry(TypedDict):
    """The shape of one study-log entry."""

    topic: str
    minutes: int
    completed: bool


def save_entries(entries: list[StudyEntry], path: Path) -> None:
    """Write study entries to a UTF-8 JSON file."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(entries, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


def load_entries(path: Path) -> list[StudyEntry]:
    """Read study entries, returning an empty list when the file is absent."""
    if not path.exists():
        return []

    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, list):
        raise ValueError("study log must contain a JSON list")
    return data


def total_minutes(entries: list[StudyEntry]) -> int:
    """Return the total study time."""
    return sum(entry["minutes"] for entry in entries)


if __name__ == "__main__":
    example_path = Path("study_log.json")
    example_entries: list[StudyEntry] = [
        {"topic": "Python JSON", "minutes": 30, "completed": True},
        {"topic": "Git basics", "minutes": 20, "completed": True},
    ]
    save_entries(example_entries, example_path)
    print(f"已记录 {total_minutes(load_entries(example_path))} 分钟学习时间。")

