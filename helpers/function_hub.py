from io import StringIO
from typing import List, Union
import werkzeug.datastructures
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
import nltk, re

def clean_text(corpus):
    a = 'i.e.'
    corpus = re.sub(r'\n', ' ', corpus)
    corpus = re.sub(r'\xa0', ' ', corpus)
    # corpus = re.sub(r'i.e.', 'ie', corpus)
    sent_lst = nltk.sent_tokenize(corpus)

    return sent_lst

def convert_pdf_to_text_sentences(file: Union[str, werkzeug.datastructures.FileStorage],
                                  from_file_object: bool = True) -> List[str]:
    """
    :param file: either file path as string or gridfs.grid_file.GridOut object
    :param from_file_object: if set to True then function will consider gridfs.grid_file.GridOut object else file path

    :return: coverts pdf to text as list of sentences, returns that list of sentences
    """
    fp = file if from_file_object else open(file, 'rb')
    rsrcmgr = PDFResourceManager()
    # codec = 'utf-8'
    laparams = LAParams()
    retstr = StringIO()
    device = TextConverter(rsrcmgr, retstr, laparams=laparams)
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos = set()
    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages,
                                  password=password,
                                  caching=caching,
                                  check_extractable=True):
        interpreter.process_page(page)
    text = retstr.getvalue()
    retstr.close()
    return clean_text(text)