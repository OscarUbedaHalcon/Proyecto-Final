from claseSpeaker import Hablar
import random
import speech_recognition as sr
class Games:
    def LanzarMoneda(self):
        habla=Hablar()
        moves=["cara", "cruz"]   
        cmove=random.choice(moves)
        habla.engine_speakES("Ha salido " + cmove)
    def PPT(self):
        r = sr.Recognizer()
        mic = sr.Microphone()
        habla=Hablar()
        habla.engine_speakES("Escoje entre piedra, papel o tijeras")
        while True:
            with mic as source:
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source)
            q = r.recognize_google(audio, language='es-ES')
            pmove=q
            break
        moves=["piedra", "papel", "tijeras"]
    
        cmove=random.choice(moves)

        habla.engine_speakES("El ordenador ha sacado " + cmove)
        habla.engine_speakES("Tu has sacado " + pmove)
        if pmove==cmove:
            habla.engine_speakES("Empate")
        elif pmove== "piedra" and cmove== "tijeras":
            habla.engine_speakES("Jugador gana")
        elif pmove== "piedra" and cmove== "papel":
            habla.engine_speakES("Ordenador gana")
        elif pmove== "papel" and cmove== "piedra":
            habla.engine_speakES("Jugador gana")
        elif pmove== "papel" and cmove== "tijeras":
            habla.engine_speakES("Ordenador gana")
        elif pmove== "tijeras" and cmove== "papel":
            habla.engine_speakES("Jugador gana")
        elif pmove== "tijeras" and cmove== "piedra":
            habla.engine_speakES("Ordenador gana")