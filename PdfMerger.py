# simple pdf file merger by adding the files location 
"""import PyPDF2
# pdf_files = ["1.pdf", "2.pdf"]
merger = PyPDF2.PdfMerger()

for filename in pdf_files:
    merger.append(filename)

merger.write("merged.pdf")
merger.close()"""

# pdf merger for taking the pdf from the user path of the pdf and then it will use to merge the pdf which was named given by user 
"""import PyPDF2

def merge_pdfs(pdf_files, output_file):
    merger = PyPDF2.PdfMerger()

    for filename in pdf_files:
        merger.append(filename)

    merger.write(output_file)
    merger.close()

if __name__ == "__main__":
    pdf_files = []
    while True:
        file_path = input("Enter the path of the PDF file to merge (or type 'done' to finish): ")
        if file_path.lower() == 'done':
            break
        pdf_files.append(file_path)

    if len(pdf_files) < 2:
        print("Please provide at least two PDF files for merging.")
    else:
        output_file = input("Enter the output file name (e.g., merged.pdf): ")
        merge_pdfs(pdf_files, output_file)
        print(f"PDF files merged successfully into {output_file}")"""

from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import PyPDF2
import os

app = Flask(__name__)

UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

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

@app.route('/download/<filename>')
def download(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=True)


@app.route('/merge_pdfs', methods=['POST'])
def merge_pdfs():
    pdf_files = request.files.getlist('pdf_files[]')

    if len(pdf_files) < 2:
        return "Please provide at least two PDF files for merging."

    output_file = request.form.get('output_file', 'merged.pdf')

    merger = PyPDF2.PdfMerger()

    for pdf_file in pdf_files:
        merger.append(pdf_file)

    output_path = os.path.join(app.config['UPLOAD_FOLDER'], output_file)
    merger.write(output_path)
    merger.close()

    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
