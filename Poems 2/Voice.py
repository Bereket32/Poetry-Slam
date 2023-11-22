import os
from gtts import gTTS
from Creation import Creation

#https://www.geeksforgeeks.org/convert-text-speech-python/
#https://gtts.readthedocs.io/en/latest/module.html

class Voice:

    def speaking(text):
        file = open(text, "r").read()
        TheVoice = gTTS(text = str(file), lang='en', slow= True)
        TheVoice.save("AudFile.mp3")
        #os.system("mpyg321 AudFile.mp3")


def main():
    Voice.speaking('created_poem.txt')
    print("")



if __name__ == "__main__":
    main()
    



