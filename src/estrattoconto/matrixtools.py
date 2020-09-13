import typing


Matrix = typing.Iterable[typing.List[str]]


def merge_columns(it: Matrix, n=4, sep=' ') -> Matrix:
    '''merge all columns>=n, for each row in it
    merge_columns([[foo,bar,baz],[pippo,pluto,paperino]],1) ->
            [[foo, bar baz], [pippo, pluto paperino]]'''

    for orig in it:
        row = [''] * (n + 1)
        for i, cell in enumerate(orig):
            if i <= n:
                row[i] = cell
            else:
                row[n] += sep + cell
        yield row


def merge_rows(it: Matrix, i=0, sep=' ') -> Matrix:
    '''merge rows splitted in multiple rows.
    for every row in it, inspect the first column.
    if empty, merge the other rows in the previous row

    [[foo,bar,baz],[None,qux,quux]] -> [[foo, bar qux, baz quux]]

    '''

    itor = iter(it)
    previous_row: typing.Optional[typing.List[str]] = None
    while True:
        try:
            row = next(itor)
        except StopIteration:
            break

        if row[i]:
            # this is a new row
            if previous_row is None:
                # keep track of the row, don't yield it
                previous_row = row
            else:
                # this is a new legit row
                yield previous_row
                previous_row = row
        else:
            # this is a continuation
            if previous_row is None:
                # wtf?
                raise Exception(
                    f'no {row}[{i}] and previous_row is {previous_row}')
            else:
                # this row is a continuation of the previous one
                for j, cell in enumerate(row):
                    if i != j:  # ignore the "id"
                        previous_row[j] += sep + cell

    if previous_row is not None:
        yield previous_row
