#!/usr/bin/env python

from glob import glob
from sys import argv
import logging

import estrattoconto

LOGGER = logging.getLogger(__name__)


def main() -> None:
    'call the extration for each parameter passed'

    args = argv[1:] if len(argv) > 1 else ('resources/*.pdf',)

    for arg in args:
        for infn in glob(arg):
            outfn = infn.replace('.pdf', '.json')

            LOGGER.info(' - convert %s to %s', infn, outfn)

            estrattoconto.extract(infn, outfn)


if __name__ == '__main__':
    logging.basicConfig(
        format='[%(asctime)s][%(levelname)-8s][%(name)s] %(module)s.%(funcName)s%(message)s',
        level=logging.INFO)
    logging.getLogger('pdfminer').setLevel(logging.WARNING)
    logging.getLogger('camelot').setLevel(logging.WARNING)
    main()
