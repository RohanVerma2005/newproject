import pyttsx3
from PyPDF2 import PdfReader
from tkinter.filedialog import askopenfilename

book = askopenfilename()
pdfreader = PdfReader(book)
pages = len(pdfreader.pages)

player = pyttsx3.init()

player.setProperty('rate', 160)


for num in range(pages):
    text = pdfreader.pages[num].extract_text()
    if text:
        player.say(text)

player.runAndWait()
