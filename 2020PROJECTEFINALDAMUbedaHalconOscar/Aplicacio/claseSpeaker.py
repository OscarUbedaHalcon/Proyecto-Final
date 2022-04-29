from gtts import gTTS
import os
import random
import playsound

class Hablar:
    def engine_speakES(self,audio_string):
        audio_string = str(audio_string)
        tts = gTTS(text=audio_string, lang='es-ES') # text to speech(voice)
        r = random.randint(1,20000000)
        audio_file = 'audio' + str(r) + '.mp3'
        tts.save(audio_file) # save as mp3
        playsound.playsound(audio_file) # play the audio file
        os.remove(audio_file) # remove audio file
    def engine_speakEN(self,audio_string):
        audio_string = str(audio_string)
        tts = gTTS(text=audio_string, lang='en') # text to speech(voice)
        r = random.randint(1,20000000)
        audio_file = 'audio' + str(r) + '.mp3'
        tts.save(audio_file) # save as mp3
        playsound.playsound(audio_file) # play the audio file
        os.remove(audio_file) # remove audio file
