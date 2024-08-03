from codes.playfair import decode, encode


def main():
    input = "hide the gold in the tree stumps"
    expected = "BMODZBXDNABEKUDMUIXMMOUVIF"
    output = encode("PLAYFAIR EXAMPLE", input)
    output_straight_decoded = decode("PLAYFAIR EXAMPLE", input)
    new_output = decode("PLAYFAIR EXAMPLE", output)
    print(f"{input=}")
    print(f"{output=}")
    print(f"{new_output=}")
    print(f"{output_straight_decoded=}")


if __name__ == "__main__":
    main()
