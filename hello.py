"""My first Python program in the AI engineering journey."""


MESSAGE_LINES = (
    "Hello, AI engineering journey!",
    "今天我亲手修改并运行了第一个 Python 程序。,",
)


def build_message() -> str:
    """Return the message printed by this program."""
    return "\n".join(MESSAGE_LINES)


def main() -> None:
    """Print a short message that confirms the program can run."""
    print(build_message())


if __name__ == "__main__":
    main()
