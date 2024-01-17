from flask import Flask, render_template, request, send_file, jsonify
import os
from PyPDF2 import PdfMerger
from PIL import Image
from docx2pdf import convert
from fpdf import FPDF

app = Flask(__name__)

UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

ALLOWED_EXTENSIONS = {'pdf', 'jpg', 'jpeg', 'png', 'docx'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def merge_pdfs_files(uploaded_files, output_path):
    if len(uploaded_files) < 2:
        return render_template('index.html', error="Please select at least two files to merge.")

    merger = PdfMerger()

    for file in uploaded_files:
        if allowed_file(file.filename):
            if file.filename.lower().endswith('.pdf'):
                merger.append(file)
            elif file.filename.lower().endswith(('.jpg', '.jpeg', '.png')):
                img = Image.open(file)
                pdf_output_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename.rsplit('.', 1)[0] + '.pdf')
                img.save(pdf_output_path, 'PDF')
                merger.append(pdf_output_path)
                close_and_remove(pdf_output_path)  # Close and remove temporary PDF image file
            elif file.filename.lower().endswith('.docx'):
                docx_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
                pdf_output_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename.rsplit('.', 1)[0] + '.pdf')
                file.save(docx_path)
                convert(docx_path, pdf_output_path)
                merger.append(pdf_output_path)
                close_and_remove(docx_path)  # Close and remove temporary DOCX file
                close_and_remove(pdf_output_path)  # Close and remove temporary PDF file

    # Ensure the output file has a .pdf extension
    if not output_path.lower().endswith('.pdf'):
        output_path += '.pdf'

    with open(output_path, 'wb') as output_file:
        merger.write(output_file)

    merger.close()

    return output_path

def close_and_remove(file_path):
    try:
        with open(file_path, 'rb') as file:
            file.close()
        os.remove(file_path)
    except PermissionError:
        # Log the error or handle it as needed
        pass

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check_file/<filename>')
def check_file(filename):
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    if os.path.exists(file_path):
        return '', 200
    else:
        return '', 404

@app.route('/merge_files', methods=['POST'])
def merge_files():
    uploaded_files = request.files.getlist('files[]')

    output_file = request.form.get('output_file', 'merged.pdf')
    output_path = os.path.join(app.config['UPLOAD_FOLDER'], output_file)

    result = merge_pdfs_files(uploaded_files, output_path)

    if isinstance(result, str):
        return send_file(result, as_attachment=True, mimetype='application/pdf', download_name=os.path.basename(result))
    else:
        return result

# Run the Flask application
if __name__ == "__main__":
    app.run(debug=True)
