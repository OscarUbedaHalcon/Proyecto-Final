import pyautogui
import speech_recognition as sr
class ControlTeclado:
    def movimiento(self):
        r = sr.Recognizer()
        mic = sr.Microphone()
        while True:
            with mic as source:
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source)
            a = r.recognize_google(audio, language='es-ES')
            print(a)
            if "diagonal" in a:
                if "derecha" in a:
                    if "arriba" in a:
                        if "poquito" in a:
                            x,y=pyautogui.position()
                            pyautogui.moveTo(x+100, y-10)
                        else:
                            x,y=pyautogui.position()
                            pyautogui.moveTo(x+100, y-100)
                    if "abajo" in a:
                        if "poquito" in a:
                            x,y=pyautogui.position()
                            pyautogui.moveTo(x+100, y+100)
                        else:
                            x,y=pyautogui.position()
                            pyautogui.moveTo(x+1000, y+1000)
                if "izquierda" in a:
                    if "arriba" in a:
                        if "poquito" in a:
                            x,y=pyautogui.position()
                            pyautogui.moveTo(x-10, y-10)
                        else:
                            x,y=pyautogui.position()
                            pyautogui.moveTo(x-100, y-100)
                    if "abajo" in a:
                        if "poquito" in a:
                            x,y=pyautogui.position()
                            pyautogui.moveTo(x-10, y+10)
                        else:
                            x,y=pyautogui.position()
                            pyautogui.moveTo(x-100, y+100)
            else:
                if "arriba" in a:
                    if "poquito" in a:
                        x,y=pyautogui.position()
                        pyautogui.moveTo(x, y-10)
                    else:     
                        x,y=pyautogui.position()
                        pyautogui.moveTo(x, y-100)
                if "abajo" in a:
                    if "poquito" in a:
                        x,y=pyautogui.position()
                        pyautogui.moveTo(x, y+10) 
                    else:
                        x,y=pyautogui.position()
                        pyautogui.moveTo(x, y+100)
                if "derecha" in a:
                    if "poquito" in a:
                        x,y=pyautogui.position()
                        pyautogui.moveTo(x+10, y)
                    else: 
                        x,y=pyautogui.position()
                        pyautogui.moveTo(x+100, y)
                if "izquierda" in a:
                    if "poquito" in a:
                        x,y=pyautogui.position()
                        pyautogui.moveTo(x-10, y) 
                    else:
                        x,y=pyautogui.position()
                        pyautogui.moveTo(x-100, y)
            if "pulsa" in a:
                pyautogui.click()
            if "termina" in a:
                break
    def teclas(self):
        r = sr.Recognizer()
        mic = sr.Microphone()
        while True:
            with mic as source:
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source)
            a = r.recognize_google(audio, language='es-ES')
            print(a)
            if "manten" in a:
                if "adelante" in a:
                    for i in range (0,5):
                        pyautogui.press("w")
                if "atras" in a:
                    for i in range (0,5):
                        pyautogui.press("s")    
                if "derecha" in a:
                    for i in range (0,5):
                        pyautogui.press("d")
                if "izquierda" in a:
                    for i in range (0,5):
                        pyautogui.press("a")
            else:
                if "adelante" in a:
                    pyautogui.press("w")
                if "atras" in a:
                    pyautogui.press("s")    
                if "derecha" in a:
                    pyautogui.press("d")
                if "izquierda" in a:
                    pyautogui.press("a")
            if "termina" in a:
                break    

pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True