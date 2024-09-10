# API_Biblioteca
API criada com Django e Rest Framework para um sistema de bibliotecas.


#### 1. Modelagem de Dados

Os seguintes modelos de dados foram implementados para representar o sistema de bibliotecas:

- Livro: Título, Autor, Categoria, Data de Publicação.
- Leitor: Nome, Idade, Cidade
- Empréstimo: Livro, Data de Empréstimo, Data de Devolução, Usuário.

#### 2. Serializers

Foram criados serializers para cada modelo criado. 

#### 3. Autenticação e Permissões

Autenticação por POR TOKEN para API. Com os seguintes grupos de permissões:

- Grupo "Leitores": Acesso para listar e pegar detalhes de livros e empréstimos.
- Grupo "Bibliotecários": Acesso para listar, criar, atualizar e excluir livros, leitores e empréstimos.
- Outros grupos com permissões podem ser criados no interesse do programador.

OBS: Para essa API as permissões são as mesmas do DjangoModelPermissions para fins didáticos

#### 4. Endpoints e Views

Foram criados os seguintes endpoints e suas respectivas views:

- `/livros/`: Listagem de todos os livros. 
- `/livros/<id>/`: Detalhes de um livro específico. 
- `/leitores/`: Listagem de todos os leitores. 
- `/leitores/<id>/`: Detalhes de um leitor específico. 
- `/leitores/<id>/emprestimos/`: Lista todos os empréstimos de um leitor específico 
- `/emprestimos/`: Listagem de todos os empréstimos. 
- `/emprestimos/<id>/`: Detalhes dos emprestimos

OBS: quem está no grupo Bibliotecários pode fazer CRUD completo nos endpoints.

#### Formas de acesso:
- http://127.0.0.1:8000/api/v1/leitores
- http://127.0.0.1:8000/api/v1/leitores/id/
- http://127.0.0.1:8000/api/v1/leitores/id/emprestimos
- http://127.0.0.1:8000/api/v1/livros/
- http://127.0.0.1:8000/api/v1/livros/id/
- http://127.0.0.1:8000/api/v1/emprestimos/
- http://127.0.0.1:8000/api/v1/emprestimos/id/

#### 5. Funcionalidades novas

- http://127.0.0.1:8000/api/v1/livros/?titulo=titulo&isbn=isbn
