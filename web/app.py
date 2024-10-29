import web
import requests

API_URL = ""  

# Rutas 
urls = ("/", "Index")

app = web.application(urls, globals())
render = web.template.render("web/views/")

class Index:

    def GET(self):
        try:
            response = requests.get(API_URL)
        
            if response.status_code == 200:
                data = response.json()  
                print("RESPUESTA API:",data)
                
            else:
                data = "No hay peliculas"

            return render.index(data)
        
        except Exception as e:
            print(f"ERROR al insertar la pelicula: {e}")

if __name__ == "__main__":
    app.run()