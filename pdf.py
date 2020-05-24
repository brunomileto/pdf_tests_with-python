import PyPDF2
import sys


# inputs = sys.argv[1:]  # the 0 is the archive name

# Basics of PyPDF2


# with open('dummy.pdf.pdf', mode='rb') as file:     # Need the read binary "rb" mode
#     reader = PyPDF2.PdfFileReader(file)     # Create a pdf reader object
#     print(reader.numPages)
#     print(reader.getPage(0))
#     page = reader.getPage(0)    # get the page 01 of the pdf and store it in a variable
#
#     print(page.rotateCounterClockwise(90))  # rotate the page clockwise counter
#
#     writer_object = PyPDF2.PdfFileWriter()  # creates a writer object
#
#     writer_object.addPage(page)     # Use the method addPage, to add a page to the writer object
#
#     with open('tilt.pdf', 'wb') as new_file:    # Creating a new pdf file to write in it
#         writer_object.write(new_file)   # Use the method write of the writer object to write the page into the new file
# ---------
# Merge PDFs
# ------
# Merge PDFs


def pdf_combiner(pdf_list):
    merger = PyPDF2.PdfFileMerger()  # Creating a merger object
    for pdf in pdf_list:
        print(pdf)
        merger.append(pdf)  # Using the append method, to append all pdf of the pdf_list

    merger.write('super.pdf')  # Creating the new pdf with the merged pdfs


# pdf_combiner(inputs)

# -------
# Watermark all pdfs in the directory

def watermark(pdf_input, water_mark):
    with open(pdf_input, 'rb') as file:  # open the input pdf
        input_reader = PyPDF2.PdfFileReader(file)  # Creating a pdf reader object for the input pdf
        with open(water_mark, 'rb') as file_2:  # open the watermark pdf
            water_mark_reader = PyPDF2.PdfFileReader(file_2)  # Creating a pdf reader object for the watermark pdf
            input_reader_num_pages = input_reader.numPages  # Get the number of pages of the input pdf, for the loop
            watermark_page = water_mark_reader.getPage(0)  # Get the watermark page, to create a Page Object for merge
            writer_object = PyPDF2.PdfFileWriter()  # Creating the writer object
            for page_num in range(input_reader_num_pages):  # Loop, for each page of the input pdf
                page = input_reader.getPage(page_num)  # Creating the Page Object for each page of the input pdf
                page.mergePage(watermark_page)  # Merging pages using the method of the Page Object
                writer_object.addPage(page)  # Passing the merged page to the writer object with addPage method
                with open('super_watermarked.pdf', 'wb') as result_file:  # Creating the new archive, with merged page
                    writer_object.write(result_file)  # Writing each merged page into new archive


# watermark('super.pdf', 'wtr.pdf.pdf')

template_pdf = PyPDF2.PdfFileReader(open('super.pdf', 'rb'))
watermark_pdf = PyPDF2.PdfFileReader(open('wtr.pdf.pdf', 'rb'))
writer_object = PyPDF2.PdfFileWriter()

for i in range(template_pdf.numPages):
    page = template_pdf.getPage(i)
    page.mergePage(watermark_pdf.getPage(0))
    writer_object.addPage(page)
    with open('watermarked_output.pdf', 'wb') as file:
        writer_object.write(file)

