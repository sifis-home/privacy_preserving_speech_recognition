# -*- coding: utf-8 -*-
"""
Created on Sat Jul 16 19:40:16 2022

@author: wisam
"""


# This module is imported so that we can
# play the converted audio
import os

# Import the required module for text
# to speech conversion
from gtts import gTTS

# The text that you want to convert to audio
mytext = "My name is Wisam!"

# Language in which you want to convert
language = "en"

# Passing the text and language to the engine,
# here we have marked slow=False. Which tells
# the module that the converted audio should
# have a high speed
myobj = gTTS(text=mytext, lang=language, slow=False)

# Saving the converted audio in a mp3 file named
# welcome
myobj.save("welcome.mp3")

# Playing the converted file
os.system("mpg321 welcome.mp3")
