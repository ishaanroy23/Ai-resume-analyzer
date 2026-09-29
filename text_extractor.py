from PyPDF2 import PdfReader

def extract_text_from_pdf(file):
    try:
        reader = PdfReader(file)
        text = ''
        for page in reader.pages:
            text+=page.extract_text() + '\n'
        return text
    except Exception as e:
        return None