from flaskwebsite import app, database

# with app.app_context():
#     database.drop_all()
#     database.create_all()

# with app.app_context():
#     usuario = Usuario(username="Admin", email="admin@admin.com", senha="123456")
#     database.session.add(usuario)
#     database.session.commit()

# with app.app_context():
#     meus_usuarios = Usuario.query.all()
#     print(meus_usuarios)

# with app.app_context():
#     meu_post = Post(id_usuario=1, titulo="Primeiro post de teste", corpo="Texto aqui")
#     database.session.add(meu_post)
#     database.session.commit()
