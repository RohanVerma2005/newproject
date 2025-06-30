import pyttsx3
from PyPDF2 import PdfReader
from tkinter.filedialog import askopenfilename

# Ask user to select a PDF file
book = askopenfilename()
pdfreader = PdfReader(book)
pages = len(pdfreader.pages)

# Initialize TTS engine
player = pyttsx3.init()

# Set speech rate (you can adjust it if needed)
player.setProperty('rate', 170)

# Ask user for voice preference
print("Choose a voice:")
print("1. Female")
print("2. Male")
choice = input("Enter 1 or 2: ")

# Get available voices
voices = player.getProperty('voices')

# Function to find a voice based on gender keyword
def find_voice(gender_keyword):
    for voice in voices:
        if gender_keyword in voice.name.lower():
            return voice
    return None

# Set the chosen voice
if choice == '1':
    female_voice = find_voice("female") or find_voice("zira") or find_voice("aria") or find_voice("jenny")
    if female_voice:
        player.setProperty('voice', female_voice.id)
        print(f"Using female voice: {female_voice.name}")
    else:
        print("No female voice found. Using default.")
        player.setProperty('voice', voices[0].id)

elif choice == '2':
    male_voice = find_voice("male") or find_voice("david") or find_voice("mark") or find_voice("guy")
    if male_voice:
        player.setProperty('voice', male_voice.id)
        print(f"Using male voice: {male_voice.name}")
    else:
        print("No male voice found. Using default.")
        player.setProperty('voice', voices[0].id)

else:
    print("Invalid input. Using default voice.")
    player.setProperty('voice', voices[0].id)

# Speak the PDF content
for num in range(pages):
    text = pdfreader.pages[num].extract_text()
    if text:
        player.say(text)

player.runAndWait()
