import dataclasses
import datetime
import decimal
import json
import typing


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
    raise NotImplementedError('extract')


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
