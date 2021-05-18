from flask import Flask,render_template,abort,json,request
import os

app = Flask(__name__)

f = open('msx.json',)

datos = json.load(f)

@app.route('/',methods=["GET","POST"])
def inicio():
	return render_template("index.html")

@app.route('/juegos',methods=["GET"])
def juegos():
    return render_template("juegos.html")

@app.route('/listajuegos',methods=["POST"])
def listajuegos():
  listajuegos=[]
  formulario=request.form.get("informacion")
  for a in datos:
  	if str(formulario) == "" or str(a["nombre"]).startswith(formulario) :
	   listajuegos.append(a)
  return render_template("listajuegos.html",listajuegos=listajuegos)

@app.route('/juego/<identificador>')
def juego(identificador):
  lista=[]
  ind=False
  for b in datos:
    if int(b.get("id")) == int(identificador):
      ind=True
      lista.append(b)
  if ind:
    return render_template("juego.html",lista=lista)
  else:
    abort(404)

app.run(debug=True)


#La aplicación hay que desplegarla en heroku

#Realizar la búsqueda utilizando una sola ruta: Es decir que en la página /juegos este el 
# formulario de búsqueda y la lista de juegos seleccionado. La información del formulario 
# se enviará a la misma página. No existirá la página /listajuegos.

#Como el protocolo HTTP no tiene estado, no es capaz de acordarse de los datos anteriores, 
#por lo tanto cada vez que hagáis una búsqueda aparecerá la lista de juegos pero el formulario 
# estará vacío, no recuerda lo que pusimos. Modifica el programa para que aparezca en el formulario 
# la cadena que habías introducido en la búsqueda (Pista: tendrá que utilizar el atributo value del 
# elemento input).

#Añade otro criterio de búsqueda, es decir vas a poder buscar por nombre y por categoría. 
#Para buscar por categoría vas a generar dinámicamente una lista desplegable (elemento select) 
# en el formulario con las categorías de los juegos). Por lo tanto podremos buscar un juego que 
# empiece por una cadena de una determinada categoría.
#De la misma forma que en el apartado 1 programar la lista desplegable para que recuerde la opción 
# elegida en la búsqueda. (Pista: Usar el atributo selected del elemento option del elemento select)