import docx2txt

def extract_tables_and_paragraphs(docx_file):
  """Extracts tables and paragraphs from a DOCX file.

  Args:
    docx_file: The path to the DOCX file.

  Returns:
    A list of tables and paragraphs.
  """

  tables = []
  paragraphs = []

  text = docx2txt.process(docx_file)
  print(text)
  for i, paragraph in enumerate(text.split("\n")):
    if paragraph.startswith("Table "):
      tables.append(paragraph)
    else:
      paragraphs.append((i, paragraph))

  return tables, paragraphs

if __name__ == "__main__":
  docx_file = "SRS.docx"
  tables, paragraphs = extract_tables_and_paragraphs(docx_file)

  for table in tables:
    print(table)

  for index, paragraph in paragraphs:
    print("Index:", index, "Paragraph:", paragraph)