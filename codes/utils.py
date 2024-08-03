import builtins
import os

from rich import print as r_print

LETTERS = "ABCDEFGHIKLMNOPQRSTUVWXYZ"


def print(*args) -> None:
    """custom print function that only prints if SHOW_OUTPUTS is set in the .env file"""
    if os.environ.get("SHOW_OUTPUTS", "false").lower() == "true":
        if os.environ.get("RICH_PRINT", "false").lower() == "true":
            r_print(*args)
        else:
            builtins.print(*args)


def chunk(l: list, n: int):
    """Groups a list into sections of n length."""
    return [l[i * n : (i + 1) * n] for i in range((len(l) + n - 1) // n)]
