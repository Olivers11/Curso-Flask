from flask import Flask, render_template, request



aplicacion = Flask(__name__)

#Rutas
@aplicacion.route("/home", methods=['GET'])
def home():
    #http://127.0.0.1:3000/home?parametro1=Oliver
    # return f"El parametro es: {param}"
    try:
        nombre = request.args.get('nombre')
        print(nombre)
        return render_template("home.html", nombre=nombre)
    except:
        return render_template("index.html")




@aplicacion.route("/")
def principal():
    #   <input type="text" placeholder="Ingrese su nombre" />
    return render_template("index.html" )




if __name__ == "__main__":
    #Ejecutar la aplicacion en el archivo principal
    aplicacion.run(port=3000, debug=True)
















