# Accessible Transcription Automation for LAS

This project was born out of my work as a transcription assistant at McMaster Library’s Library Accessibility Services. I built this tool to automate the repetitive task of reformatting Word documents (converted from PDFs) into a standardized, accessible format.

## Why I Made This

- **Save Time:** I was spending too much time manually cleaning up documents after converting them from PDFs.
- **Ensure Accessibility:** Making sure that documents meet accessibility standards (including proper image handling) is crucial.
- **Automate the Workflow:** Curiosity and the need for automation drove me to create a tool that streamlines the entire process.

## How It Works

1. **PDF Conversion:**  
   Use ABBYY FineReader to convert your PDFs into Word documents. **Important:** Make sure to select the option to "create a new page for each page."

2. **Upload:**  
   Upload the converted Word file via the web interface.

3. **Processing:**  
   - **Formatting:** Clears existing formatting and applies consistent styles for titles, headings, and regular text.
   - **Page Numbers:** Automatically adds page numbers.
   - **Accessibility:** Retains images and their text (including alt text) to ensure accessibility remains intact.

4. **Download:**  
   Download the newly formatted document from the web app.

## Built With

- **[python-docx](https://python-docx.readthedocs.io/):** Manipulate and format Word documents.
- **Flask:** Provides the simple web interface.
- **Tailwind CSS:** Creates a clean, responsive UI.
## Prerequisites

- Python 3.x
- [python-docx](https://pypi.org/project/python-docx/) library (Install via `pip install python-docx`)
- Flask 3.10
- Tailwind CSS

