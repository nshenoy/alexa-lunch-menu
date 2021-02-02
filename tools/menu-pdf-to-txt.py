import sys
import json
from pdfminer.high_level import extract_text

def main():
    # read in arguments
    menuFile = sys.argv[1]
    txtFile = menuFile.replace(".pdf", ".txt")

    # convert the menu PDF file to text
    convertMenuToText(menuFile, txtFile)

def convertMenuToText(menuFile, textFile):
    # read in the contents of the menu txt file
    menuRawText = extract_text(menuFile)

    # save the text file
    with open(textFile, "w", encoding="utf-8") as fout:
        fout.write(menuRawText)

if __name__ == "__main__":
    main()
