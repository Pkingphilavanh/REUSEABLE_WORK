import re
from docx import Document
from openpyxl import Workbook

def extract_sentences_with_shall(docx_path):
    """Extracts sentences containing the word 'shall' from a Word document."""
    doc = Document(docx_path)
    sentences_with_shall = []

    # Iterate through paragraphs in the document
    for paragraph in doc.paragraphs:
        # Split the paragraph into sentences using regex
        sentences = re.split(r'(?<=[.!?]) +', paragraph.text)
        for sentence in sentences:
            if 'shall' in sentence.lower():  # Case-insensitive search for 'shall'
                sentences_with_shall.append(sentence.strip())
    
    return sentences_with_shall

def export_to_excel(sentences, output_excel_path):
    """Exports a list of sentences to an Excel file."""
    workbook = Workbook()
    sheet = workbook.active
    sheet.title = "Sentences with Shall"

    # Write sentences to individual rows
    for i, sentence in enumerate(sentences, start=1):
        sheet.cell(row=i, column=1, value=sentence)
    
    workbook.save(output_excel_path)

if __name__ == "__main__":
    input_docx = "input.docx"  # Replace with your Word document file path
    output_excel = "output.xlsx"  # Replace with your desired Excel file path

    # Extract sentences and export to Excel
    sentences = extract_sentences_with_shall(input_docx)
    if sentences:
        export_to_excel(sentences, output_excel)
        print(f"Exported {len(sentences)} sentences to '{output_excel}'.")
    else:
        print("No sentences containing 'shall' were found.")
