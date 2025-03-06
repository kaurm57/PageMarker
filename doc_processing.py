from docx import Document
from docx.oxml.ns import qn
from docx.shared import Inches
import re
import io

def add_page_num(doc_path, edited_doc, page_count):
    """
    Copies text and images from the source document to a new document,
    inserts [Slide x] markers at page breaks, and applies Heading 6 style to those markers.
    """
    doc = Document(doc_path)
    new_doc = Document()

    for para in doc.paragraphs:
        for run in para.runs:
            for br in run._element.findall(qn("w:br")):
                if br.get(qn("w:type")) == "page":
                    page_count += 1
                    run._element.remove(br)
                    run.add_text(f"[Slide {page_count}]")

        match = re.search(r"\[Slide \d+\]", para.text)
        if match:
            new_doc.add_paragraph()  # Empty paragraph for spacing
            page_heading = new_doc.add_paragraph(match.group(0))
            page_heading.style = "Heading 6"
        else:
            new_para = new_doc.add_paragraph()
            new_para.style = para.style

            for run in para.runs:
                if run._element.xpath('.//w:drawing'):
                    blip_elements = run._element.xpath('.//a:blip')
                    if blip_elements:
                        rId = blip_elements[0].get(qn('r:embed'))
                        image_part = doc.part.related_parts[rId]
                        image_stream = io.BytesIO(image_part.blob)
                        new_doc.add_picture(image_stream, width=Inches(4))
                else:
                    new_para.add_run(run.text)

    new_doc.save(edited_doc)
    return page_count
