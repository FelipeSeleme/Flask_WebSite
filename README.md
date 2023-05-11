# FlaskWebSite
Criando um site em Python com Flask e Bootstrap.  
  
O site é uma simuação bem-humorada de rede social para heróis aposentados que passam tempo demais na internet.
     <hr>
    </div>
    <div class="container mt-2">
        {% for post in posts %}
        <div class="row mt-4 p-3 meupost">
            <div class="col col-2">
                <div class="image pe-2">
                    <img src="{{ url_for('static', filename='fotos_perfil/{}'.format(post.autor.foto_perfil)) }}" class="rounded" width="100" >
                </div>
                <strong>{{ post.autor.username }}</strong>
            </div>
            <div class="col col-10">
                <a style="text-decoration: none" href="{{ url_for('exibir_post', post_id=post.id) }}"><h3>{{ post.titulo }}</h3></a>
                <p> {{ post.corpo }}</p>
            </div>
        </div>
        {% endfor %}
    </div>
