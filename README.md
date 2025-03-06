# PageMarker
# Accessible Transcription Automation for LAS

This project automates the process of converting and formatting Word documents (especially those converted from PDFs) to make them accessible. The tool leverages [python-docx](https://python-docx.readthedocs.io/) to handle document processing and formatting.

## Features

- **Automatic Page Numbering:**  
  Inserts slide markers (e.g., `[Slide 1]`, `[Slide 2]`, etc.) at each page break in the document. The page breaks are detected from the PDF-to-Word conversion process, where a new line is added before a new page.

- **Image Handling and Alt Text Retention:**  
  Copies images from the original document into the new document. The project extracts and retains the alt text from the source image (if available) and applies it to the corresponding image in the final document. This ensures that images remain accessible for screen readers.

- **Preservation of Styles and Custom Formatting:**  
  - **Clearing Formatting:** The script removes unnecessary formatting from text runs and paragraphs while preserving the underlying style name.
  - **Custom Formatting:** It reapplies a custom set of formatting rules (such as font type, size, spacing, and boldness) based on the paragraph style. This ensures uniformity across the document and improves readability.

- **Style Border Removal:**  
  For styles that automatically include borders (like the "Title" style), the tool can remove these borders by modifying the underlying XML. This helps in preventing unwanted formatting artifacts in the final document.

- **Modular Design:**  
  The code is organized into separate modules for cleaner presentation and easier maintenance:
  - `doc_processing.py`: Handles copying text, images, and inserting slide markers.
  - `formatting.py`: Contains functions for clearing formatting, applying custom formatting, and removing unwanted style borders.
  - `main.py`: The main script that imports functions from the other modules and executes the full document processing pipeline.

## How It Works

1. **Add Page Numbers and Copy Content:**  
   The `add_page_num` function reads the source document, detects page breaks, inserts slide markers, and copies text and images (including alt text for images) into a new document.

2. **Clear Formatting:**  
   The `clear_formatting` function removes extra formatting from the document while preserving text and style names, ensuring a clean slate for custom formatting.

3. **Apply Custom Formatting:**  
   The `format_text` function applies a uniform set of formatting rules based on the style (e.g., Title, Heading 1, Heading 2) to improve document readability and ensure accessibility.

4. **Remove Style Borders:**  
   The `remove_style_borders` function edits the underlying style XML to remove unwanted borders (e.g., from the "Title" style).

## Prerequisites

- Python 3.x
- [python-docx](https://pypi.org/project/python-docx/) library (Install via `pip install python-docx`)

## File Structure

