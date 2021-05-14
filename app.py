from flask import Flask, render_template,abort,json
import os
app = Flask(__name__)

f = open('msx.json',)

datos = json.load(f)

@app.route('/',methods=["GET","POST"])
def inicio():
	return render_template("index.html")

@app.route('/listajuegos/')
def listajuegos():
    return render_template("listajuegos.html")

@app.route('/juegos/')
def juegos():
    return render_template("juegos.html")

@app.route('/categorias/<tipo>')
def categoria(tipo):
    listacategorias=[]
    for cate in datos:
        for lista in cate.get("categories"):
            if lista==tipo:
                listacategorias.append(cate)
    return render_template("categorias.html",categoria=tipo,lista_categorias=listacategorias,lista_libros=datos)

#La página /juegos nos mostrara un buscador, para ello pon un formulario con un cuadro de 
#texto donde puedas poner el nombre de un juego que quieres buscar. Cuando pulséis el botón de 
#buscar enviará la información a la página /listajuegos. El formulario enviará los datos con el 
#método POST.

#En la página /listajuegos (qué sólo se puede acceder por el método POST) aparecerán los juegos 
#cuyo nombre empiezan por la cadena que hemos añadido al formulario. Si no hemos indicado ninguna 
#cadena mostrará todos los juegos.

#La página /listajuegos mostrará una tabla generada dinámicamente a partir de los datos del 
#fichero msx.json y la búsqueda que se haya realizado.

#La tabla tendrá tres columnas: en la primera aparecerá el nombre, en la segunda el desarrollador 
#y en la tercera habrá un enlace con la palabra “Detalle” que me llevará a la página del juego 
#con la ruta /juego/<identificador>.

#Como ves, estamos volviendo a hacer el patrón de diseño : Lista - detalle. La lista está en 
#la página /listajuegos y el detalle está en la página /juego/<identificador> donde aparecerán 
#todos los datos del juego que tenga ese identificador. Si el identificador no existe devolverá un 404. Tendrá un enlace que me devuelve a la página /juegos.

#La aplicación hay que desplegarla en heroku

app.run(debug=True)
