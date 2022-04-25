import argparse

parser = argparse.ArgumentParser(description='Convert hex to bin or bin to hex')
parser.add_argument(
    '--hex2bin',
    type=str,
    default=None,
    help='Enter a hexadecimal number'
)
parser.add_argument(
    '--bin2hex',
    type=str,
    default=None,
    help='Enter a binary number'
)
args = parser.parse_args()
print(args.hex2bin)
print(args.bin2hex)