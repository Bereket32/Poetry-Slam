import os
from gtts import gTTS
from Creation import Creation
#sources
#https://www.geeksforgeeks.org/convert-text-speech-python/
#https://gtts.readthedocs.io/en/latest/module.html

class Voice:

    def speaking(text):
        '''Uses google Text to Speech to create an auido file of gtts reading created_poem'''
        text = open(text, "r").read()
        TheVoice = gTTS(text = str(text), lang='en', slow= True)
        TheVoice.save("AudFile.mp3")
     





