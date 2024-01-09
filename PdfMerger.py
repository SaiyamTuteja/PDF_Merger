# simple pdf file merger by adding the files location 
"""import PyPDF2
# pdf_files = ["1.pdf", "2.pdf"]
merger = PyPDF2.PdfMerger()

for filename in pdf_files:
    merger.append(filename)

merger.write("merged.pdf")
merger.close()"""

# pdf merger for taking the pdf from the user path of the pdf and then it will use to merge the pdf which was named given by user 
import PyPDF2

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
        print(f"PDF files merged successfully into {output_file}")
