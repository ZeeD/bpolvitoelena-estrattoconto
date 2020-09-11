import dataclasses
import datetime
import decimal
import json
import os
import tempfile
import typing

import camelot


@dataclasses.dataclass
class Row:
    data: datetime.date
    valuta: datetime.date
    addebiti: decimal.Decimal
    accrediti: decimal.Decimal
    descrizione_operazioni: str


@dataclasses.dataclass
class EstrattoConto:
    n: str
    intestato: str
    iban: str
    rows: typing.List[Row]


def extract(in_: typing.BinaryIO) -> EstrattoConto:
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

    for table in tables:
        print('table: ', table)
        # all as string
        # data = table.data[...][0]
        # valuta = table.data[...][1]
        # addebiti = table.data[...][2]
        # accrediti = table.data[...][3]
        # descrizione_operazioni = table.data[...][4--]
        # nota: descrizione va a capo, ci sono righe "vuote" dedicate

    return None


def to_string(estratto_conto: EstrattoConto) -> str:
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

    return json.dumps(estratto_conto, cls=E)


def serialize(estratto_conto: EstrattoConto, out: typing.TextIO) -> None:
    'write the estratto conto to the outstream'
    out.write(to_string(estratto_conto))
