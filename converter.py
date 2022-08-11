import argparse
import hex2bin
import bin2hex


## Чек комменты в комиите


## New line 11
## New line 22
# Новая строка 1
# Новая строка 2

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
    bin2hex.convert(args.bin)


    #Новая строка в конце 1
    #Новая строка в конце 2

    ## New line in end of file 11
    ## New line in end of file 22

# 2 Чек комменты в коммите

# Это должен быть отдельный прекоммит
