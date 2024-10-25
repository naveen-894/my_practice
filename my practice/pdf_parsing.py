from py_pdf_parser.loaders import load_file

document = load_file("simple_memo.pdf")

to_element = document.elements.filter_by_text_equal("TO:").extract_single_element()
from_element = document.elements.filter_by_text_equal("FROM:").extract_single_element()
date_element = document.elements.filter_by_text_equal("DATE:").extract_single_element()
subject_element = document.elements.filter_by_text_equal("SUBJECT:").extract_single_element()

# from py_pdf_parser.loaders import load_file

# def parse():

#     # Step 1 - Load the document
#     document = load_file("IntrwReport_naveen.pdf")
#     print(document)
#     for page in document.pages:
#         print(f"Page {page.number}:")
#         for element in page.elements:
#             print(f"Element: {element.text}")
#     # return
#     # We could visualise it here to check it looks correct:
#     # from py_pdf_parser.visualise import visualise
#     # visualise(document)

#     # Step 2 - Extract reference elements:
#     to_element = document.elements.filter_by_text_equal("TO:").extract_single_element()
#     from_element = document.elements.filter_by_text_equal("FROM:").extract_single_element()
#     date_element = document.elements.filter_by_text_equal("DATE:").extract_single_element()
#     subject_element = document.elements.filter_by_text_equal(
#         "SUBJECT:"
#     ).extract_single_element()

#     # Step 3 - Extract the data
#     to_text = document.elements.to_the_right_of(to_element).extract_single_element().text()
#     from_text = (
#         document.elements.to_the_right_of(from_element).extract_single_element().text()
#     )
#     date_text = (
#         document.elements.to_the_right_of(date_element).extract_single_element().text()
#     )
#     subject_text_element = document.elements.to_the_right_of(
#         subject_element
#     ).extract_single_element()
#     subject_text = subject_text_element.text()

#     content_elements = document.elements.after(subject_element)
#     content_text = "\n".join(element.text() for element in content_elements)

#     output = {
#         "to": to_text,
#         "from": from_text,
#         "date": date_text,
#         "subject": subject_text,
#         "content": content_text,
#     }
#     print(output)
# def parse():

#     import PyPDF2

#     file_path = "IntrwReport_naveen.pdf"
#     with open(file_path, "rb") as pdf_file:
#         reader = PyPDF2.PdfReader(pdf_file)
#         for page_num in range(len(reader.pages)):
#             page = reader.pages[page_num]
#             text = page.extract_text()
#             print(f"Page {page_num + 1} text:\n{text}\n")


# import pytesseract
# from pdf2image import convert_from_path

# file_path = "IntrwReport_naveen.pdf"

# # Convert each page of the PDF to an image
# pages = convert_from_path(file_path)

# # Perform OCR on each page
# for page_num, page_image in enumerate(pages, start=1):
#     text = pytesseract.image_to_string(page_image)
#     print(f"Page {page_num} text:\n{text}\n")


from PyPDF2 import PdfReader
from pdfminer.high_level import extract_text as fallback_text_extraction

text = ""
try:
    reader = PdfReader("simple_memo.pdf")
    for page in reader.pages:
        text += page.extract_text()
    print(text)
    print('iuytgfrdefrtgyhujikolp;oiuyt')
except Exception as exc:
    print(exc)
    text = fallback_text_extraction("IntrwReport_naveen.pdf")