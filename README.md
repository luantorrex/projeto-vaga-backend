# Instruções API ACMEVita

## Sobre a API

A API ACMEVita funciona como gerenciadora dos departamentos, colaboradores e dependentes.

A partir dela é possível cadastrar e consultar informações sobre os colaboradores e departamentos da companhia.

### Configurações

Para executar a aplicação, é recomendado executá-la em uma máquina Linux e criar um ambiente virtual, onde serão instaladas as dependências da aplicação. Para isso, é necessário executar os seguintes comandos no diretório raíz da aplicação:
* pip install virtualenv
* virtualenv venv
* source venv/bin/activate

Criada e iniciada máquina virtual, precisamos instalar as dependências da aplicação. Para isso, iremos executar o seguinte comando:
* pip install -r requirements.txt

Para iniciar a aplicação, basta executá-la por meio do comando:
* flask run

### Instruções

Iniciada a aplicação, podemos fazer uso dela por meio dos seguintes endpoints:

##### Listar departamentos:
* http://127.0.0.1:5000/departments/list_departments (Método GET)

##### Listar colaboradores de um departamento:
* http://127.0.0.1:5000/departments/list_collaborators/<<department_id>> (Método GET)

Exemplo de Path: http://127.0.0.1:5000/departments/list_collaborators/3

##### Cadastrar departamentos:
* http://127.0.0.1:5000/departments/register (Método POST)

Exemplo de Body: {"name": "SSC"}

##### Cadastrar colaboradores:
* http://127.0.0.1:5000/collaborators/register (Método POST)

Exemplo de Body: {"full_name": "Jorge Alcantara","department_id": 4,"dependents": 0}

### Swagger

Para fazer requisições à aplicação via Swagger, basta acessar a seguinte URL, nela é possível consultar as listas de colaboradores e departamentos:
* http://127.0.0.1:5000/swagger