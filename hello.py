"""My first Python program in the AI engineering journey."""


MESSAGE_LINES = (
    "Hello, AI engineering journey!",
    "今天完成一个小步骤，长期积累一个作品集。",
)


def build_message() -> str:
    """Return the message printed by this program."""
    return "\n".join(MESSAGE_LINES)


def main() -> None:
    """Print a short message that confirms the program can run."""
    print(build_message())


if __name__ == "__main__":
    main()
