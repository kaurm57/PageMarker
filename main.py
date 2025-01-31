from docx import Document 
from docx.oxml.ns import qn 
import re

# Open an existing document
doc = Document("./testing.docx")
editted_doc = Document("./result.docx")
def add_page_num(doc, editted_doc, page_count):
    doc = Document(doc)
    for para in doc.paragraphs:
        for run in para.runs:
            for br in run._element.findall(qn("w:br")):
                if br.get(qn("w:type")) == "page":
                    page_count +=1
                    run._element.remove(br)
                    run.add_text(f"\n[Page {page_count}]")
    doc.save(editted_doc)

add_page_num("./testing.docx", "./result.docx", 0)

def make_page_heading(doc_path, editted_doc):
    doc = Document(doc_path)

    new_doc = Document()
    # Iterate through all paragraphs
    for para in doc.paragraphs:
        match = re.search(r"\[Page \d+\]", para.text)
        if match:
            # Split the paragraph into two parts
            before_text = para.text[:match.start()]

            page_text = match.group(0)  # This is the [Page x] part

            new_doc.add_paragraph()
            page_heading = new_doc.add_paragraph(page_text)
            page_heading.style = "Heading 6"
        else:
            new_para = new_doc.add_paragraph(para.text)
            new_para.style = para.style

    new_doc.save(editted_doc)
# Call the function with paths to your document
make_page_heading("./result.docx", "./final-result.docx")

final_doc = Document("./final-result.docx")

for para in final_doc.paragraphs:
    print("===========")
    print(para.text)