

# PDF Merger

This Python script allows you to merge multiple PDF files into a single PDF file using the PyPDF2 library. The project provides two versions of the PDF merger:

## Simple PDF Merger

The `simple_pdf_merger.py` script merges a predefined list of PDF files.

### Usage:

```bash
python PdfMerger.py
```

1. Open the script in a text editor.
2. Edit the `pdf_files` list to include the paths of the PDF files you want to merge.
3. Run the script.

The merged PDF file will be saved as "merged.pdf" in the same directory.

## User-Provided PDF Merger

The `PdfMerger.py` script prompts the user to enter the paths of PDF files to merge and the desired output file name.

### Usage:

```bash
python PdfMerger.py
```

1. Run the script and follow the prompts to enter the paths of the PDF files to merge.
2. Type 'done' when you've entered all files.
3. Enter the desired output file name.

The merged PDF file will be saved in the same directory as the script.

## Dependencies:

- Python 3.x
- PyPDF2 library

## License:

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
