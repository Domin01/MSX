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
  for b in datos:
    if int(b.get("id")) == int(identificador):
        lista.append(b)
  return render_template("juego.html")



app.run(debug=True)



#Como ves, estamos volviendo a hacer el patrón de diseño : Lista - detalle. 
# La lista está en 
#la página /listajuegos y el detalle está en la página /juego/<identificador> donde aparecerán 
#todos los datos del juego que tenga ese identificador. Si el identificador no existe devolverá un 404. Tendrá un enlace que me devuelve a la página /juegos.

#La aplicación hay que desplegarla en heroku