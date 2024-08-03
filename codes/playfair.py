# https://en.wikipedia.org/wiki/Playfair_cipher

from argparse import ArgumentParser

from dotenv import load_dotenv
from rich.console import Console

from .cli import key_input_args
from .utils import LETTERS, chunk, print

load_dotenv(override=True)


def make_grid(key: str):
    # format the key like we would the message
    key = format_string(key)
    k = []
    # remove any duplicates from the key
    for j in key:
        if j not in k:
            k.append(j)
    # remove duplicate letters
    flat = k + [l for l in LETTERS if l not in key]
    return chunk(flat, 5)


def separate_dups(msg: str) -> str:
    positions_to_insert: list = []
    for i, letter in enumerate(msg[1:], 1):
        if letter == msg[i - 1]:
            positions_to_insert.append(i + len(positions_to_insert))
    msg: list = list(msg)
    for j in positions_to_insert:
        msg.insert(j, "X")
    return "".join(msg)


def format_string(msg: str) -> str:
    msg: str = msg.upper().replace(" ", "")
    msg: str = msg.replace("J", "I")
    return msg


def format_message(msg: str, separate_duplicates: bool) -> str:
    msg: str = format_string(msg)
    if separate_duplicates:
        msg: str = separate_dups(msg)
    print(msg)
    return chunk(list(msg), 2)


def get_cord(grid: list, letter: str) -> int:
    for r, row in enumerate(grid):
        for c, col in enumerate(row):
            if col == letter:
                return r, c


def prep(key: str, msg: str, separate_duplicates: bool) -> tuple:
    grid = make_grid(key)
    msg = format_message(msg, separate_duplicates)
    return grid, msg


def determine_new_str_encode(c1, c2, grid):
    # same row
    if c1[0] == c2[0]:
        return grid[c1[0]][(c1[1] + 1) % 5] + grid[c2[0]][(c2[1] + 1) % 5]
    # same column
    elif c1[1] == c2[1]:
        return grid[(c1[0] + 1) % 5][c1[1]] + grid[(c2[0] + 1) % 5][c2[1]]
    # rectangle
    return grid[c1[0]][c2[1]] + grid[c2[0]][c1[1]]


def determine_new_str_decode(c1, c2, grid):
    # same row
    if c1[0] == c2[0]:
        return grid[c1[0]][(c1[1] - 1) % 5] + grid[c2[0]][(c2[1] - 1) % 5]
    # same column
    elif c1[1] == c2[1]:
        return grid[(c1[0] - 1) % 5][c1[1]] + grid[(c2[0] - 1) % 5][c2[1]]
    # rectangle
    return grid[c1[0]][c2[1]] + grid[c2[0]][c1[1]]


def encode(key: str, msg: str):
    grid, msg = prep(key, msg, True)
    print(grid)
    encoded_msg = []
    for iteration, pair in enumerate(msg):
        print(f"{iteration=}")
        c1 = get_cord(grid, pair[0])
        # we have an even number of letters
        if len(pair) != 1:
            c2 = get_cord(grid, pair[1])
            new_str = determine_new_str_encode(c1, c2, grid)
        # we have an odd number of letters
        # flip the letter across both axis
        else:
            new_str = grid[4 - c1[0]][4 - c1[1]]

        encoded_msg.append(new_str)
        print(f"{''.join(pair)} -> {new_str}")
    return "".join(encoded_msg)


def decode(key: str, msg: str):
    grid, msg = prep(key, msg, False)
    decoded_msg = []
    for iteration, pair in enumerate(msg):
        print(f"{iteration=}, {pair=}")
        c1 = get_cord(grid, pair[0])
        # we have an even number of letters
        if len(pair) != 1:
            c2 = get_cord(grid, pair[1])
            new_str = determine_new_str_decode(c1, c2, grid)
        # we have an odd number of letters
        # flip the letter across both axis
        else:
            new_str = grid[4 - c1[0]][4 - c1[1]]

        decoded_msg.append(new_str)
        print(f"{''.join(pair)} -> {new_str}")
    return "".join(decoded_msg)


def main():
    key_input_args("Encode/Decode Playfair cipher", decode, encode)


if __name__ == "__main__":
    main()
