import dataclasses
import datetime
import decimal
import typing


@dataclasses.dataclass
class Row:
    data: datetime.date
    valuta: typing.Optional[datetime.date]
    addebiti: decimal.Decimal
    accrediti: decimal.Decimal
    descrizione_operazioni: str


@dataclasses.dataclass
class EstrattoConto:
    n: str
    intestato: str
    iban: str
    rows: typing.List[Row]
