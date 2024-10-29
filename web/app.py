import web
import requests

API_URL = "https://api-rest-7nlb.onrender.com/peliculas"  


# Rutas 
urls = ("/", "Index")

app = web.application(urls, globals())
render = web.template.render("web/views/")

class Index:
    try:
        def GET(self):
            
            response = requests.get(API_URL)
        
            if response.status_code == 200:
                data = response.json()  
                print("RESPUESTA API:",data)
                
            else:
                data = [] 

            return render.index(data)
    except Exception as e:
        print(f"ERROR ENCONTRADO:{e}")
        
if __name__ == "__main__":
    app.run()