from . import estrattoconto


def extract(infn: str, outfn: str) -> None:
    'read from infn (a .pdf) and write to outfn (a .txt)'

    with open(infn, 'rb') as in_:
        estratto_conto = estrattoconto.extract(in_)
        with open(outfn, 'w') as out:
            estrattoconto.serialize(estratto_conto, out)
