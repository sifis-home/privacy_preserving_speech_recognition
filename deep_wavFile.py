# This module is imported so that we can
# play the converted audio
import os
import wave

import numpy as np
import spacy
from deepspeech import Model

# Import the required module for text
# to speech conversion
from gtts import gTTS

nlp = spacy.load("en_core_web_sm")

entity_types = [
    "PERSON",
    "NORP",
    "FAC",
    "ORG",
    "GPE",
    "LOC",
    "PRODUCT",
    "EVENT",
    "WORK_OF_ART",
    "LAW",
    "LANGUAGE",
    "DATE",
    "TIME",
    "PERCENT",
    "MONEY",
    "QUANTITY",
    "ORDINAL",
    "CARDINAL",
]
entity_desc = [
    "People, including fictional.",
    "Nationalities or religious or political groups.",
    "Buildings, airports, highways, bridges, etc.",
    "Companies, agencies, institutions, etc.",
    "Countries, cities, states.",
    "Non-GPE locations, mountain ranges, bodies of water.",
    "Objects, vehicles, foods, etc. (Not services.)",
    "Named hurricanes, battles, wars, sports events, etc.",
    "Titles of books, songs, etc.",
    "Named documents made into laws.",
    "Any named language.",
    "Absolute or relative dates or periods.",
    "Times smaller than a day.",
    'Percentage, including "%".',
    "Monetary values, including unit.",
    "Measurements, as of weight or distance.",
    '"first", "second", etc.',
    "Numerals that do not fall under another type.",
]

for (item, desc) in zip(entity_types, entity_desc):
    print(item, ": ", desc)

model_file_path = "deepspeech-0.9.3-models.pbmm"
lm_file_path = "deepspeech-0.9.3-models.scorer"
beam_width = 500  # how many different word sequences that needs to be evaluated by acoustic model
lm_alpha = 0.93  # optimum parameter suggested in the repo
lm_beta = 1.18

model = Model(model_file_path)
model.enableExternalScorer(lm_file_path)


def read_wav_file(filename):
    with wave.open(filename, "rb") as w:
        rate = w.getframerate()
        frames = w.getnframes()
        buffer = w.readframes(frames)
        print(rate)
        print(frames)
    return buffer, rate


def transcribe(audio_file):
    buffer, rate = read_wav_file(audio_file)
    data = np.frombuffer(buffer, dtype=np.int16)
    return model.stt(data)


text = transcribe("sample2.wav")
print("Original Text:", text)

doc = nlp(text)
text2 = text

print("------Entities------")
for ent in doc.ents:
    print(ent.text, ent.start, ent.end, ent.start_char, ent.end_char, ent.label_)
    length = ent.end_char - ent.start_char
    text2 = text2[: ent.start_char] + "x" * length + text2[ent.end_char :]

Final_Text = ""

for item in text2.split():
    if item.count("xx") >= 1:
        # print(item, item.count('xx'))
        Final_Text = Final_Text + "Privat Data "
    else:
        # print(item, item.count('xx'))
        Final_Text = Final_Text + item + " "

print("Modified Text:", Final_Text)

# Language in which you want to convert
language = "en"

myobj = gTTS(text=Final_Text, lang=language, slow=False)

myobj.save("Output_Audio.mp3")

# Playing the converted file
os.system("mpg321 Output_Audio.mp3")
