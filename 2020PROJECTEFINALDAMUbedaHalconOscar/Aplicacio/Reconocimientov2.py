#!/usr/bin/python3
# -*- coding: utf-8 -*-
import speech_recognition as sr
from claseSpeaker import Hablar
from claseTraductor import Traductor
from claseControlTecl import ControlTeclado
from claseLecWeb import lecturaWeb
from claseBuscador import Buscador
from claseGames import Games

r = sr.Recognizer()

mic = sr.Microphone()
habla=Hablar()
traducir=Traductor()
controlador=ControlTeclado()
leectorWeb=lecturaWeb()
busqueda=Buscador()
juegos=Games()

while True:
    print("Puedes Hablar")
    while True:
        habla.engine_speakES("Hola, como quieres que me llame?")
        with mic as source:
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
        a = r.recognize_google(audio, language='es-ES')
        nombre=a
        habla.engine_speakES("Entendido me llamo "+nombre)
        print(a)
        break
    with mic as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    c = r.recognize_google(audio, language='es-ES')
    if nombre in c:
        while True:
            print("En que puedo ayudarte? ")
            habla.engine_speakES("En que puedo ayudarte? ")
            with mic as source:
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source)
            b = r.recognize_google(audio)
            print(b)
            if "cómo" in b and "me llamo" in b:
                habla.engine_speakES("No lo se. Como te llamas?")
                while True:
                    with mic as source:
                        r.adjust_for_ambient_noise(source)
                        audio = r.listen(source)
                    q = r.recognize_google(audio, language='es-ES')
                    nombreCre=q
                habla.engine_speakES("Te llamas "+nombreCre)
            if "búscame" in b:
                if "youtube" in b:
                    #usar sobre al preguntar para poder saber que parte escojer
                    search_term = b.split("sobre")[-1]
                    busqueda.busqYoutube(search_term)
                    habla.engine_speakES("Esto es lo que he podido encontrar")
                else:
                    search_term = b.split("sobre")[-1]
                    busqueda.busqGoogle(search_term)
                    habla.engine_speakES("Esto es lo que he podido encontrar")
            if "léeme" in b and "web" in b:
                leectorWeb.lecturaPaginaWeb("https://www.elmundo.es/economia/2020/05/15/5ebe95c121efa063468b4646.html")
            if "Toma" in b and "control" in b:
                controlador.movimiento()
            if "traduce" in b and "español" in b:
                traducir.traduccionEsToEn()
            if "traduce" in b and "ingles" in b:
                traducir.traduccionEnToEs()
            if "Juguemos" in b:
                while True:
                    habla.engine_speakES("Que quieres jugar?")
                    with mic as source:
                        r.adjust_for_ambient_noise(source)
                        audio = r.listen(source)
                    o = r.recognize_google(audio, language='es-ES')
                    if "moneda" in o:
                        juegos.LanzarMoneda()
                    if "piedra" in o or "papel" in o or "tijera" in o:
                        juegos.PPT()
                    if "nada" in o:
                        break
            if "apágate" in b:
                print("Finalizar reconocimiento")
                habla.engine_speakES("Finalizar reconocimiento")
                break
        break