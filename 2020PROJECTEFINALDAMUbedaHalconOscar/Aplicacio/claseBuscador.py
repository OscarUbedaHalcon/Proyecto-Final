import webbrowser
class Buscador:
    def busqGoogle(self,busqueda):
        url = "https://google.com/search?q=" + busqueda
        webbrowser.get().open(url)
    def busqYoutube(self,busqueda):
        url = "https://www.youtube.com/results?search_query=" + busqueda
        webbrowser.get().open(url)
