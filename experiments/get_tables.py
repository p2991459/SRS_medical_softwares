# import camelot
#
# # extract all the tables in the PDF file
# abc = camelot.read_pdf("SRS.pdf") #address of file location
#
# # print the first table as Pandas DataFrame
# print(abc[0].df)
# from tabula import read_pdf
# from tabulate import tabulate

#reads table from pdf file
# df = read_pdf("SRS.pdf",pages="all") #address of pdf file
# print(tabulate(df))

from docx import Document
import pandas as pd
document = Document('SRS.docx')
tables = []
table_data = []
for table in document.tables:


    # Iterate over each row in the table
    for row in table.rows:
        row_data = []

        # Iterate over each cell in the row
        for cell in row.cells:
            row_data.append(cell.text)

        table_data.append(row_data)

    # Convert the table data to a pandas DataFrame
df = pd.DataFrame(table_data)
print(df)
df.to_csv("table.csv")
    # Append the DataFrame to the list of tables
    # tables.append(df)

# Display all the extracted tables
# for i, table in enumerate(tables):
#     print(f"Table {i + 1}:")
#     print(table)
#     print()

from deficiencies_mapper import get_deficiencies

print(get_deficiencies(str(df)))