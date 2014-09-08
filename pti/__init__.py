from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfdevice import PDFDevice

def import_transcripts():
	pdf_input_filename = '/home/georges/Dev/parliament-transcript-importer/data/trans_s_2014_04_23_16_5609_al.pdf'

	txt_output_filename = '/home/georges/Dev/parliament-transcript-importer/data/trans_s_2014_04_23_16_5609_al.txt' 

	rsrcmgr = PDFResourceManager()

	outtype = 'text'
	outfp = file(txt_output_filename, 'w')	

	device = TextConverter(rsrcmgr, outfp, codec='utf-8')

	fp = file(pdf_input_filename, 'rb')
	interpreter = PDFPageInterpreter(rsrcmgr, device)
	for page in PDFPage.get_pages(fp, check_extractable=True):
		interpreter.process_page(page)

	# Close resources.
	fp.close()
	device.close()
	outfp.close()

