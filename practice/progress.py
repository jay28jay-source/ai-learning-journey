"""A tiny learning-progress calculator."""


def progress_summary(completed: int, total: int) -> str:
    """Return a readable progress summary.

    Args:
        completed: Number of completed learning tasks.
        total: Total number of learning tasks.

    Raises:
        ValueError: If the task counts are not logically valid.
    """
    if total <= 0:
        raise ValueError("total must be greater than zero")
    if completed < 0:
        raise ValueError("completed cannot be negative")
    if completed > total:
        raise ValueError("completed cannot be greater than total")

    percentage = completed / total * 100
    return f"已完成 {completed}/{total} 项（{percentage:.0f}%）"


if __name__ == "__main__":
    print(progress_summary(completed=3, total=5))

