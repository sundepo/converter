import argparse
import hex2bin

parser = argparse.ArgumentParser(description='Convert hex to bin or bin to hex')
parser.add_argument(
    '--hex',
    type=str,
    default=None,
    help='Enter a hexadecimal number'
)
parser.add_argument(
    '--bin',
    type=str,
    default=None,
    help='Enter a binary number'
)

args = parser.parse_args()    # Теперь в args лежит наше число

if args.hex is not None:
    hex2bin.convert(args.hex)
else:
    pass
