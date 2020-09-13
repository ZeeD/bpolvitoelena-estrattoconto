#!/usr/bin/env python

from glob import glob
from sys import argv

import estrattoconto


def main() -> None:
    'call the extration for each parameter passed'

    args = argv[1:] if len(argv) > 1 else ('resources/*.pdf',)

    for arg in args:
        for infn in glob(arg):
            outfn = infn.replace('.pdf', '.json')

            estrattoconto.extract(infn, outfn)


if __name__ == '__main__':
    main()
