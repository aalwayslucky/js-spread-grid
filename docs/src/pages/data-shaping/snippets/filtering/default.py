app.layout = DashSpreadGrid(  # type: ignore
    data={
        # collapse: true
        # default dict data
        # collapse: false
    },
    # collapse: true
    columns=[{"type": "DATA-BLOCK", "width": 70}],
    # collapse: false
    rows=[
        {"type": "HEADER"},
        {"type": "FILTER"},
        {"type": "DATA-BLOCK"},
    ],
    filters=[{"columnId": "registered", "expression": True}],
)
