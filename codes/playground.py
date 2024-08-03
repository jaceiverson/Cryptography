import numpy as np

from .utils import chunk

# import inflect

ascii_min = 32
ascii_max = 126
ascii_shift = ascii_max - ascii_min + 1


def encrypt(text, key):
    pass


def decrypt(text, key, difficulty):
    buckets = len(text) // key
    decode = ""
    code = chunk(text[::-1], buckets)

    for x in range(buckets):
        for y in code:
            decode += y[x]

    return decode, code


def level_1_e(text):
    return text[::-1]


def level_2_e(text):
    # https://www.tutorialspoint.com/cryptography_with_python/cryptography_with_python_quick_guide.htm
    # Ceaser
    code = ""
    for x in text:
        char = text[x]
        if char.isupper():
            code += chr((ord(char) + s - 65) % 26 + 65)
        # Encrypt lowercase characters in plain text
        else:
            code += chr((ord(char) + s - 97) % 26 + 97)

    return code


def level_5_e(text):
    """ """


def j_encrypt(steps, text):
    return flip(transpose_cols(text, steps))


def flip(text):
    return text[::-1]


def transpose_cols(text, steps):
    """
    3 modes of using this
    Basic: left to right, new line
    Snake: left to right, right to left, etc.
    Diagnal: crazy stuff, start top right, down one, over one, etc.
    """
    steps = 6
    if steps % 2 == 0 and steps % 3 == 0:
        # both mult 2 and 3 diagnal snake
        steps = 4
        temp = snake(text, steps)

        temp = diagnal("".join(temp), steps)
        return read("".join(temp), steps)

    elif steps % 2 == 0:
        # multiple of 2 means snake
        temp = snake(text, steps)
        return read("".join(temp), steps)

    elif steps % 3 == 0:
        # multiple of 3 = diagnal
        temp = diagnal(text, steps)
        return read("".join(temp), steps)

    else:
        # base case just simple transpose
        return read(text, steps)


def diagnal(text, steps):
    print(text)
    chart = chunk(text, steps)
    multi = max(len(chart) // steps, 2)
    for x in range(len(chart)):
        chart[x] = chart[x] * (multi)

    print(chart)
    msg = ""
    for x in range(len(chart)):
        for y in range(len(chart[0])):
            try:
                msg += chart[y][x + y]
            except:
                msg += "#"

    return msg


def snake(text, steps):
    chart = chunk(text, steps)
    for x in range(len(chart)):
        if x % 2 != 0:
            chart[x] = chart[x][::-1]

    return chart


def read(text, cols):
    text_l = chunk(text, cols)
    msg = ""
    for x in range(cols):
        for y in text_l:
            try:
                msg += y[x]
            except IndexError:
                msg += "#"
    return msg


def trans(text, steps):
    text_l = chunk(text, steps)
    msg = ""
    for x in range(steps):
        pass


def substitute(text, offset):
    code = ""
    for x in text:
        new_chr = ord(x) + offset
        if new_chr < ascii_min:
            new_chr += ascii_shift
        elif new_chr > ascii_max:
            new_chr -= ascii_shift

        code += chr(new_chr)

    return code


j = "jace shawn iverson"
code = 4
# difficulty 1-5
level = 1
f = j_encrypt(4, j)
f_f = j_encrypt(4, j)


print(substitute(" !@#$$%T:LKJDF", -1))
