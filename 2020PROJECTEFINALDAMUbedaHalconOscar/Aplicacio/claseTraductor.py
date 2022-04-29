from claseSpeaker import Hablar
from translate import Translator
import speech_recognition as sr

class Traductor:
    def traduccionEnToEs(self):
        mic = sr.Microphone()
        r = sr.Recognizer()
        habla=Hablar()
        translator= Translator(to_lang="es-ES",from_lang="en")
        while True:
            with mic as source:
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source)
            a = r.recognize_google(audio, language='en')
            print(a)
            habla.engine_speakES(translator.translate(a))
            break
    
    def traduccionEsToEn(self):
        mic = sr.Microphone()
        r = sr.Recognizer()
        habla=Hablar()
        translator= Translator(to_lang="en",from_lang="es-ES")
        while True:
            with mic as source:
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source)
            a = r.recognize_google(audio, language='es-ES')
            print(a)
            habla.engine_speakEN(translator.translate(a))
            break
