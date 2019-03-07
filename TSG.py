#!/usr/bin/env python
# -*- coding: utf-8 -*-

from argparse import ArgumentParser
from glob import glob
from PyPDF2 import PdfFileReader, PdfFileWriter
import os
import arcpy

# path = r'O:\TSG_book_projects\B_size\2018\python_test\KingKittitas'
# stream = r'O:\TSG_book_projects\B_size\2018\python_test\KingKittitas\merge.pdf'
# listdata = r'O:\TSG_book_projects\B_size\2018\python_test\KingKittitas\ListData.txt'

pdfFolder = r"path to pdfs"
pdfList = r"O:\TSG_book_projects\B_size\2019\BSizeTOC.csv"


def merge(path, output_filename):
    output = PdfFileWriter()

    for pdffile in glob(path + os.sep + '*.pdf'):
        if pdffile == output_filename:
            continue
        print("Parse '%s'" % pdffile)
        document = PdfFileReader(open(pdffile, 'rb'))
        for i in range(document.getNumPages()):
            output.addPage(document.getPage(i))

    print("Start writing '%s'" % output_filename)
    with open(output_filename, "wb") as f:
        output.write(f)


merge(path, stream)

with open(pdfList) as pdfs:
    mainPDF = arcpy.mp.PDFDocumentOpen(os.path.join(pdfFolder, pdfs[0].strip()))
    for pdf in pdfs.readlines()[1:]:
        newpage = os.path.join(pdfFolder, pdf.strip())
        mainPDF.appendPages(newpage)
    mainPDF.saveAndClose()
#
# with open(pdfList) as pdfs:
#     for pdf in pdfs.readlines():
#         print(pdf.strip())
