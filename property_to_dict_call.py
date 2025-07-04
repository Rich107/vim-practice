import json

with open("sample_outputs/barclays.json") as file:
    # Load the JSON data from the file
    raw_data = json.load(file)
result = raw_data.get("analyzeResult")


for idx, style in enumerate(result.get("styles")):
    print(
        "Document contains {} content".format(
            "handwritten" if style.is_handwritten else "no handwritten"
        )
    )

for page in result.get("pages"):
    for line_idx, line in enumerate(page.lines):
        print(
            "...Line # {} has text content '{}'".format(
                line_idx, line.content.encode("utf-8")
            )
        )

    for selection_mark in page.selection_marks:
        print(
            f"...Selection mark is '{selection_mark.state}' and has a confidence of {selection_mark.confidence}"
        )

for table_idx, table in enumerate(result.get("tables")):
    print(
        f"Table # {table_idx} has {table.row_count} rows and {table.column_count} columns"
    )

    for cell in table.cells:
        print(
            "...Cell[{}][{}] has content '{}'".format(
                cell.row_index,
                cell.column_index,
                cell.content.encode("utf-8"),
            )
        )

print("----------------------------------------")
