# main_web.py
from flask import Flask, request, send_file, render_template, redirect, url_for, flash
import os
from doc_processing import add_page_num
from formatting import clear_formatting, format_text, remove_style_borders

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for flash messages

UPLOAD_FOLDER = 'uploads'
OUTPUT_FOLDER = 'outputs'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
# main_web.py (modified section in index route)
@app.route("/", methods=["GET", "POST"])
def index():
    processed_file = None  # Processed file name
    uploaded_file = None   # Uploaded file name

    if request.method == "POST":
        if 'file' not in request.files:
            flash("No file part")
            return redirect(request.url)

        file = request.files['file']
        if file.filename == "":
            flash("No selected file")
            return redirect(request.url)

        if file:
            input_filename = file.filename
            input_path = os.path.join(UPLOAD_FOLDER, input_filename)
            file.save(input_path)
            
            # Generate dynamic output file name
            output_filename = f"{os.path.splitext(input_filename)[0]}_formatted.docx"
            output_path = os.path.join(OUTPUT_FOLDER, output_filename)

            # Process the document
            page_count = 1
            intermediate1 = os.path.join(OUTPUT_FOLDER, "temp1.docx")
            intermediate2 = os.path.join(OUTPUT_FOLDER, "temp2.docx")
            intermediate3 = os.path.join(OUTPUT_FOLDER, "temp3.docx")
            
            page_count = add_page_num(input_path, intermediate1, page_count)
            clear_formatting(intermediate1, intermediate2)
            format_text(intermediate2, intermediate3)
            remove_style_borders(intermediate3, output_path, "Title")

            flash("File processed successfully!")
            # Pass both the processed file and the original uploaded file name
            return redirect(url_for("index", processed_file=output_filename, uploaded_file=input_filename))

    # Retrieve processed file and uploaded file name from URL query parameters
    processed_file = request.args.get("processed_file")
    uploaded_file = request.args.get("uploaded_file")
    return render_template("index.html", processed_file=processed_file, uploaded_file=uploaded_file)


    # Retrieve processed file name from URL query parameters
    processed_file = request.args.get("processed_file")
    return render_template("index.html", processed_file=processed_file)

@app.route("/download/<filename>")
def download(filename):
    file_path = os.path.join(OUTPUT_FOLDER, filename)
    return send_file(file_path, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)