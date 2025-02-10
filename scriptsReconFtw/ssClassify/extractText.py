import pytesseract
from PIL import Image
from pathlib import Path
import os, json, re, sys

def processImage(arg1):
    folder_dir = arg1
    folder_path = Path(folder_dir)
    images = [p for p in folder_path.glob('*') if p.suffix in ('.png', '.jpg', '.jpeg', '.img')]

    with open('extractedStrings.txt', 'w') as file:

        for image in images:

            imageToProcess = Image.open(image)
            text = pytesseract.image_to_string(imageToProcess)
            print(f'--------------{image}--------------')
            file.write(repr(text))
            print(repr(text))
    file.close()


def main():

#-----------------------------------------------------------------------

    if len(sys.argv)!=2:
        print("Provide directory containing images")
        print("Usage:\npython3 script.py screenshots")
        sys.exit()

    arg1 = sys.argv[1]

#-----------------------------------------------------------------------

    processImage(arg1)

if __name__ == "__main__":
    main()
