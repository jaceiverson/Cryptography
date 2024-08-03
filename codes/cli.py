from argparse import ArgumentParser

from rich.console import Console


def key_input_args(description: str, decode_fc, encode_fc):
    """
    CLI argparser for ciphers that require a key and input
    """
    parser = ArgumentParser(description=description)
    c = Console()
    parser.add_argument("input", help="input for the cipher")
    parser.add_argument("--key", "-k", help="key for the cipher")
    parser.add_argument("--decode", "-d", help="decode the input", action="store_true")
    args = parser.parse_args()
    if args.decode:
        output = decode_fc(args.key, args.input)
        c.print(output, style="bold green")
    else:
        output = encode_fc(args.key, args.input)
        c.print(output, style="bold blue")


def input_only_args(description: str, decode_fc, encode_fc):
    """
    CLI argparser for ciphers that don't require a key, just input
    """
    parser = ArgumentParser(description=description)
    c = Console()
    parser.add_argument("input", help="input for the cipher")
    parser.add_argument("--decode", "-d", help="decode the input", action="store_true")
    args = parser.parse_args()
    if args.decode:
        output = decode_fc(args.input)
        c.print(output, style="bold green")
    else:
        output = encode_fc(args.input)
        c.print(output, style="bold blue")
