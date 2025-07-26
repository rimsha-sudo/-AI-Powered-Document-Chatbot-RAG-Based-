import os
import docx2txt
import PyPDF2

def read_file(file_path):
    ext = os.path.splitext(file_path)[-1].lower()

    if ext == ".txt":
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()

    elif ext == ".pdf":
        pdf = PyPDF2.PdfReader(file_path)
        text = ""
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text
        return text

    elif ext == ".docx":
        return docx2txt.process(file_path)

    else:
        raise ValueError("Unsupported file type Upload a .txt, .pdf, or .docx file.")
