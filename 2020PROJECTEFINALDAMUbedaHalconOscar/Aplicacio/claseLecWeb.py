import requests
from bs4 import BeautifulSoup
from claseSpeaker import Hablar

class lecturaWeb:
    def lecturaPaginaWeb(self,url): 
        
        #open with GET method 
        resp=requests.get(url) 
        
        #http_respone 200 means OK status 
        if resp.status_code==200: 
            print("Successfully opened the web page") 
        
            # we need a parser,Python built-in HTML parser is enough . 
            soup=BeautifulSoup(resp.text,'html.parser')     
    
            # l is the list which contains all the text i.e news  
            l=soup.find("div",{"class":"ue-l-article__body ue-c-article__body"}) 
        
            p=0
            habla= Hablar()
            for i in l.findAll("p"): 
                print(i.text)
                habla.engine_speakEN(i.text)
                p=1+p
                if p == 3:
                    break 
        else: 
            print("Error") 