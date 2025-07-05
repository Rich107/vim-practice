import json

"""
This exercise is about switching the property access to a dictionary access.
This happened due to the example code expecting an object with properties.
But when using json files, the data is loaded as a dictionary.
"""


with open("sample_outputs/barclays.json") as file:
    # Load the JSON data from the file
    raw_data = json.load(file)
result = raw_data.get("analyzeResult")


for idx, style in enumerate(result.get("styles")):
    print(
        "Document contains {} content".format(
            "handwritten" if style.get("is_handwritten") else "no handwritten"
        )
    )

for page in result.get("pages"):
    for line_idx, line in enumerate(page.get("lines")):
        print(
            "...Line # {} has text content '{}'".format(
                line_idx, line.get("content").encode("utf-8")
            )
        )

    for selection_mark in page.get("selection_marks"):
        print(
            f"...Selection mark is '{selection_mark.get('state')}' and has a confidence of {selection_mark.get('confidence')}"
        )

for table_idx, table in enumerate(result.get("tables")):
    print(
        f"Table # {table_idx} has {table.row_count} rows and {table.column_count} columns"
    )

    for cell in table.cells:
        print(
            "...Cell[{}][{}] has content '{}'".format(
                cell.get("row_index"),
                cell.get("column_index"),
                cell.get("content").encode("utf-8"),
            )
        )

print("----------------------------------------")
