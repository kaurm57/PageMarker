# main_web.py
from flask import Flask, request, send_file, render_template, redirect, url_for, flash
import os
from doc_processing import add_page_num
from formatting import clear_formatting, format_text, remove_style_borders

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # A secret key is needed to use flash messages

# Define folders for uploads and outputs
UPLOAD_FOLDER = 'uploads'
OUTPUT_FOLDER = 'outputs'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if 'file' not in request.files:
            flash("No file part")
            return redirect(request.url)
        file = request.files['file']
        if file.filename == "":
            flash("No selected file")
            return redirect(request.url)
        if file:
            # Save the uploaded file to the UPLOAD_FOLDER
            input_path = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(input_path)
            
            # Run your document processing pipeline
            page_count = 1
            # Define intermediate and final file paths in the OUTPUT_FOLDER
            intermediate1 = os.path.join(OUTPUT_FOLDER, "final-result.docx")
            intermediate2 = os.path.join(OUTPUT_FOLDER, "final-result.docx")
            intermediate3 = os.path.join(OUTPUT_FOLDER, "final-result.docx")
            output_path = os.path.join(OUTPUT_FOLDER, "final-result.docx")
            
            # Step 1: Add slide markers and copy content (including images)
            page_count = add_page_num(input_path, intermediate1, page_count)
            # Step 2: Clear formatting (keeping style names)
            clear_formatting(intermediate1, intermediate2)
            # Step 3: Apply custom formatting
            format_text(intermediate2, intermediate3)
            # Step 4: Remove unwanted style borders
            remove_style_borders(intermediate3, output_path, "Title")
            
            # Serve the final processed file for download
            return send_file(output_path, as_attachment=True)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
