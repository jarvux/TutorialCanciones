from flaskr import create_app
from .modelos import db, Cancion

app = create_app('default')
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()

#prueba
with app.app_context():
    c = Cancion(titulo='Prueba', minutos=2, segundos=35, interprete='JarviZ')
    c2 = Cancion(titulo='Prueba 2', minutos=3, segundos=37, interprete='JarviZ')
    db.session.add(c)
    db.session.add(c2)
    db.session.commit()
    print(Cancion.query.all())