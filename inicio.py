#importar la libreria flask,redirect
from flask import Flask, render_template, request, redirect

app = Flask(__name__)
 
#Areglo que almacenara la ruta
 # funcion del controlador 
@app.route("/")
def home():
	return render_template("index.html")


#metodo principal
if __name__ == "__main__":
	app.run(debug=True)

