from PyPDF2 import PdfReader

def extract_text_from_pdf(file_path):

    # Open PDF file in binary read mode
    with open(file_path, "rb") as file:

        # Create PDF reader object
        reader = PdfReader(file)

        # Empty string to store all text
        text = ""

        # Loop through all pages
        for page in reader.pages:

            # Extract text and add to text variable
            text += page.extract_text()

        # Return all extracted text
        return text