import os
import pandas as pd
from PyPDF2 import PdfReader
from nltk import FreqDist, word_tokenize

def main():
    current_directory = os.getcwd()
    myfiles = os.listdir(current_directory)
    pdf_names = list(filter(lambda f: '.pdf' in f, myfiles))
    for pdf_name in pdf_names:
        pdf_path = os.path.join(current_directory, pdf_name)
        getWords(pdf_path, pdf_name)


def getWords (pdf_path, pdf_name):
    text = ""
    result = []
    pdf_reader = PdfReader(pdf_path)
    for page in pdf_reader.pages:
        text += page.extract_text() 
        text += "\n"
    words = word_tokenize(text)
    dist = FreqDist(words)
    for k, v in dist.items(): 
        result.append([k, v])
    col_name = ['Words','Counts']
    result.insert(0, col_name)
    df = pd.DataFrame(result)
    file_name = pdf_name + "-words.csv"
    df.to_csv(file_name, index=False)


if __name__ == "__main__":
    main()