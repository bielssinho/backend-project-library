# BiblioteKA - Project Backend

## Passos ncessários para funcionamento

### Windows

- Iniciar um ambiente virtual com o seguinte comando:
```shell
python -m venv venv
```

- Abrir um ambiente virtual com o seguinte comando:
```shell
source venv/Scripts/activate
```

- Instalando dependencias do projeto:
```shell
pip install -r requirements.txt
```

- Rodar migrações que tem no projeto:
```shell
python manage.py migrate
```

- Inicializar o servidor:
```shell
python manage.py runserver
```

- Criar e preencher os dados do arquivo .env seguindo o .env.example:
```shell
SECRET_KEY=

POSTGRES_USERNAME=
POSTGRES_PASSWORD=
POSTGRES_DB_NAME=
POSTGRES_DB_HOST=
POSTGRES_DB_PORT=

EMAIL_HOST= 
EMAIL_PORT= 
EMAIL_HOST_USER= 
EMAIL_HOST_PASSWORD= 
```


Esta aplicação contém relacionamentos com banco de dados. O objetivo dela é permitir a interação do cliente, possibilitando a solicitação de empréstimos de livros e a visualização dos livros listados no banco de dados.

## Infos da Api

Caso queira ter uma visão ampla das rotas e fazer testes da mesma acesse o link abaixo:<br>
<a href= https://biblioteka-grupo33.onrender.com/api/schema/swagger/ target_blank=true>Documentação Api</a><br>
É importante deixar claro que algumas rotas requer permissão de admin ou seja usuários normais não consiguirão fazer algumas requisições

## Contribuidores
Emanuel Luiz de Adrade<br>
Linkedin: <a href=https://www.linkedin.com/in/emanuelluiz/ target_blank=true>Linkedin Emanuel</a><br>
Github: <a href=https://github.com/emanuelluiz01 target_blank=true>Github Emanuel<a/>

Gabriel de Lima Santana<br>
Linkedin: <a href=https://www.linkedin.com/in/gabrieldelimasantana/ target_blank=true>Linkedin GAbriel de Lima</a><br>
Github: <a href=https://github.com/Gabriel-Dev target_blank=true>Github Gabriel de Lima<a/>

Gabriel dos Santos<br>
Linkedin: <a href=https://www.linkedin.com/in/gabrieldossantosmachado target_blank=true>Linkedin Gabriel dos Santos</a><br>
Github: <a href=https://github.com/bielssinho target_blank=true>Github Gabriel dos Santos<a/>

Iarley Lopes Cavalcante<br>
Linkedin: <a href=https://www.linkedin.com/in/iarley-lopes-b19100246/ target_blank=true>Linkedin Iarley</a><br>
Github: <a href=https://github.com/iarley1 target_blank=true>Github Iarley<a/>
