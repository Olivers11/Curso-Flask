from flask import Flask, render_template, request



aplicacion = Flask(__name__)

#Rutas
@aplicacion.route("/home")
def home():
    #http://127.0.0.1:3000/home?parametro1=Oliver
    param = request.args.get('parametro1', '')
    return f"El parametro es: {param}"

    #Crear un template para la ruta 'home'
    #Pasarle datos al <home.html>
    # nombres = ["Oliver", "Carlos", "Estuardo", "Casie"]
    # return render_template("home.html", nombres=nombres)



@aplicacion.route("/")
def principal():
    #   <input type="text" placeholder="Ingrese su nombre" />
    return render_template("index.html" )




if __name__ == "__main__":
    #Ejecutar la aplicacion en el archivo principal
    aplicacion.run(port=3000, debug=True)
















