import dataclasses
import datetime
import decimal
import json
import logging
import os
import tempfile
import typing

import camelot

from . import matrixtools, converttools, types


LOGGER = logging.getLogger(__name__)


def extract(in_: typing.BinaryIO) -> types.EstrattoConto:
    'basic extraction of the informations from the pdf'
    temp = tempfile.NamedTemporaryFile(suffix='.pdf', delete=False)
    try:
        temp.write(in_.read())
        temp.close()
        tables = camelot.read_pdf(
            temp.name,
            pages='all',
            flavor='stream',
            suppress_stdout=False)
    finally:
        os.remove(temp.name)

    rows: typing.List[types.Row] = []
    for table in tables:
        LOGGER.info('[table: %s]', table)

        data = matrixtools.merge_rows(matrixtools.merge_columns(table.data))
        rows.extend(map(converttools.convert, data))

    return types.EstrattoConto('', '', '', rows)


def to_string(estratto_conto: types.EstrattoConto) -> str:
    'fancy __repr__'

    class E(json.JSONEncoder):
        def default(self, o: typing.Any) -> typing.Any:  # pylint: disable=method-hidden
            if isinstance(o, datetime.date):
                return o.isoformat()
            if isinstance(o, decimal.Decimal):
                return '%.2f' % o
            if dataclasses.is_dataclass(o):
                return dataclasses.asdict(o)
            return super().default(o)

    return json.dumps(estratto_conto, cls=E, indent=4)


def serialize(estratto_conto: types.EstrattoConto, out: typing.TextIO) -> None:
    'write the estratto conto to the outstream'
    out.write(to_string(estratto_conto))
