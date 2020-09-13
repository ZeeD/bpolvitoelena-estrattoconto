import datetime
import decimal
import typing

from . import types


def convert(l: typing.List[str]) -> types.Row:
    return types.Row(date(l[0]),
                     optional_date(l[1]),
                     dec(l[2]),
                     dec(l[3]),
                     l[4])


def date(raw: str) -> datetime.date:
    raw = raw.strip()
    return datetime.datetime.strptime(raw, '%d/%m/%y').date()


def optional_date(raw: str) -> typing.Optional[datetime.date]:
    raw = raw.strip()
    return date(raw) if raw else None


def dec(raw: str) -> decimal.Decimal:
    raw = raw.strip()
    return decimal.Decimal(raw.replace(',', '.') if raw else 0)
