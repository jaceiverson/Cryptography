import pytest

from codes.playfair import decode, encode


def playfair_test():
    input = "hide the gold in the tree stumps"
    expected = "BMODZBXDNABEKUDMUIXMMOUVIF"
    output = encode("PLAYFAIR EXAMPLE", input)
    assert output == expected
    new_output = decode("PLAYFAIR EXAMPLE", output)
    assert new_output == input
