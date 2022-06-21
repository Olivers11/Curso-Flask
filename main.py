from flask import Flask, render_template



aplicacion = Flask(__name__)

#Rutas
@aplicacion.route("/home")
def home():
    #Crear un template para la ruta 'home'
    #Pasarle datos al <home.html>
    nombres = ["Oliver", "Carlos", "Estuardo", "Casie"]
    return render_template("home.html", nombres=nombres)



@aplicacion.route("/")
def principal():
    #   <input type="text" placeholder="Ingrese su nombre" />
    data = { 'titulo': 'Index', 'bienvenida': 'queonda'}
    return render_template("index.html", data=data)




if __name__ == "__main__":
    #Ejecutar la aplicacion en el archivo principal
    aplicacion.run(port=3000, debug=True)
















