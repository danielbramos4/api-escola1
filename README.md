# API Escola

API REST para gestão de estudantes, cursos e matrículas de uma instituição de ensino, desenvolvida com Django REST Framework. Criada como projeto de estudo sobre construção de APIs RESTful em Python, aplicando autenticação, validação de dados, versionamento de API e testes automatizados.

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=flat&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-5.0.3-092E20?style=flat&logo=django&logoColor=white)
![DRF](https://img.shields.io/badge/Django%20REST%20Framework-3.15.0-A30000?style=flat&logo=django&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-Database-003B57?style=flat&logo=sqlite&logoColor=white)

## Sobre o Projeto

O **API Escola** é uma aplicação backend que expõe endpoints RESTful para o gerenciamento de três entidades centrais de um contexto escolar: **estudantes**, **cursos** e **matrículas**. O projeto foi construído sobre o Django REST Framework, utilizando `ViewSets` e roteamento automático para reduzir boilerplate, ao mesmo tempo em que adiciona regras de negócio específicas — como validação de CPF, controle de acesso por autenticação e versionamento de respostas da API.

O sistema modela o relacionamento entre estudantes e cursos por meio de matrículas, permitindo consultar quais cursos um estudante está fazendo e quais estudantes estão matriculados em um determinado curso, além das operações padrão de criação, leitura, atualização e remoção (CRUD) para cada entidade.

## Funcionalidades

- **CRUD de Estudantes**: criação, listagem, detalhamento, atualização e remoção de estudantes, com validação de CPF (via `validate-docbr`), validação de nome (apenas letras) e validação de formato de celular.
- **CRUD de Cursos**: gerenciamento de cursos com código único (mínimo de 3 caracteres), descrição e nível (Básico, Intermediário, Avançado).
- **CRUD de Matrículas**: vínculo entre um estudante e um curso, com definição de período (Matutino, Vespertino, Noturno).
- **Listagem de matrículas por estudante**: endpoint dedicado que retorna os cursos e períodos em que um estudante específico está matriculado.
- **Listagem de matrículas por curso**: endpoint dedicado que retorna os estudantes matriculados em um curso específico.
- **Versionamento de API**: o endpoint de estudantes possui uma segunda versão (`v2`) que retorna um subconjunto reduzido de campos, selecionada via parâmetro de query (`?version=v2`).
- **Busca, ordenação e filtros**: o endpoint de estudantes permite busca textual por nome ou CPF e ordenação por nome.
- **Paginação automática** das listagens, com 20 itens por página.
- **Autenticação obrigatória**: todos os endpoints da API exigem autenticação (Basic Authentication).
- **Django Admin customizado**: interface administrativa configurada para gerenciar estudantes, cursos e matrículas com busca, ordenação e paginação.
- **Scripts de povoamento do banco**: scripts auxiliares (`popular_banco_cursos.py` e `popular_banco_estudantes.py`) para gerar dados de cursos fixos e estudantes fictícios (via `Faker`, em português do Brasil) para testes manuais.

## Tecnologias Utilizadas

### Linguagem
- **Python**

### Framework e Bibliotecas
- **Django 5.0.3** — framework web principal, responsável pelo ORM, roteamento, admin e ciclo de requisição/resposta.
- **Django REST Framework 3.15.0** — construção dos endpoints REST, serialização, autenticação, permissões, paginação e versionamento.
- **django-filter** — filtros dinâmicos aplicados ao endpoint de estudantes.
- **validate-docbr** — validação de documentos brasileiros (CPF).
- **Faker** — geração de dados fictícios em português do Brasil para os scripts de povoamento do banco.

### Banco de Dados
- **SQLite** — banco de dados relacional utilizado em desenvolvimento (`db.sqlite3`).

### Outras Ferramentas
- **Markdown** — suporte à renderização de documentação/browsable API do DRF.
- **sqlparse** — dependência utilizada pelo Django para formatação de SQL.

> **Nota sobre dependências:** o repositório contém dois arquivos de dependências (`requirements.txt` e `requirementes.txt`), com listas de pacotes e versões diferentes entre si. Recomenda-se consolidar em um único arquivo `requirements.txt` — veja a seção de Roadmap.

## Arquitetura e Estrutura do Projeto

O projeto segue a arquitetura padrão do Django (MVT — Model, View, Template, adaptado para API com DRF no lugar de Templates), separando o projeto de configuração (`setup/`) do aplicativo de domínio (`escola/`):

```text
api-escola1/
├── setup/                     # Configuração do projeto Django
│   ├── settings.py            # Configurações gerais, apps instalados, DRF, banco de dados
│   ├── urls.py                # Roteamento principal e registro das rotas da API
│   ├── asgi.py / wsgi.py      # Pontos de entrada para servidores ASGI/WSGI
│
├── escola/                    # Aplicativo de domínio (regras de negócio)
│   ├── models.py              # Entidades: Estudante, Curso, Matricula
│   ├── serializers.py         # Serialização e validação de dados de entrada/saída
│   ├── views.py                # ViewSets e views de listagem customizadas
│   ├── validators.py          # Validações customizadas (CPF, nome, celular)
│   ├── admin.py                # Configuração do Django Admin
│   ├── apps.py                 # Configuração do app
│   ├── migrations/            # Histórico de migrações do banco de dados
│   └── tests/                 # Testes automatizados (autenticação, estudantes, cursos, matrículas, models, serializers)
│
├── popular_banco_cursos.py    # Script para popular o banco com cursos fixos
├── popular_banco_estudantes.py # Script para popular o banco com estudantes fictícios
├── manage.py                  # Utilitário de linha de comando do Django
└── requirements.txt           # Dependências do projeto
```

**Responsabilidades principais:**
- `setup/`: configuração global do projeto (banco de dados, apps instalados, autenticação/permissões padrão da API, versionamento, paginação).
- `escola/models.py`: definição das entidades e seus relacionamentos.
- `escola/serializers.py`: conversão entre objetos Python/ORM e JSON, além de validações de negócio aplicadas na entrada de dados.
- `escola/views.py`: exposição das entidades como endpoints REST, incluindo lógica de seleção de serializer por versão de API.
- `escola/validators.py`: regras de validação isoladas e reutilizáveis, separadas da camada de serialização.
- `escola/admin.py`: interface administrativa para gerenciamento manual dos dados.

## Conceitos e Boas Práticas Aplicados

- **API REST**: recursos expostos via métodos HTTP padrão (GET, POST, PUT, DELETE) através de `ModelViewSet` e roteador automático do DRF.
- **ORM (Object-Relational Mapping)**: uso do ORM do Django para definição de modelos e relacionamentos (`ForeignKey`, `on_delete=CASCADE`).
- **Serialização de dados**: uso de `ModelSerializer` para conversão entre modelos e JSON, incluindo serializers derivados/especializados (`ListaMatriculasEstudanteSerializer`, `EstudanteSerializerV2`).
- **Validação de dados**: validações customizadas separadas em módulo próprio (`validators.py`) e aplicadas no método `validate()` do serializer.
- **Separação de responsabilidades**: divisão clara entre configuração do projeto (`setup/`), modelos, serializers, views e validações (`escola/`).
- **Versionamento de API**: implementado via `QueryParameterVersioning`, permitindo evoluir contratos de resposta sem quebrar consumidores da v1.
- **Autenticação e controle de acesso**: uso de `BasicAuthentication` e `IsAuthenticated` como padrão de segurança da API.
- **Testes automatizados**: uso de `APITestCase` do DRF para testes de integração dos endpoints, e `TestCase` do Django para testes unitários de models e serializers.
- **Migrações versionadas**: histórico de alterações do schema do banco de dados rastreado via migrações do Django.

## Como Executar o Projeto

### Pré-requisitos
- Python 3.x instalado
- pip

### Passo a passo

1. Clone o repositório:
```bash
git clone https://github.com/danielbramos4/api-escola1.git
cd api-escola1
```

2. Crie e ative um ambiente virtual:
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```
> Se encontrar erros de importação relacionados a `django_filters` ou `validate_docbr`, instale-os manualmente, já que não constam no `requirements.txt` atual:
> ```bash
> pip install django-filter validate-docbr Faker
> ```

4. Aplique as migrações do banco de dados:
```bash
python manage.py makemigrations
python manage.py migrate
```

5. (Opcional) Crie um superusuário para acessar o Admin e autenticar-se na API:
```bash
python manage.py createsuperuser
```

6. (Opcional) Popule o banco com dados de exemplo:
```bash
python popular_banco_cursos.py
python popular_banco_estudantes.py
```

7. Inicie o servidor de desenvolvimento:
```bash
python manage.py runserver
```

A API estará disponível em `http://localhost:8000/`. Como os endpoints exigem autenticação, é necessário informar usuário e senha (Basic Authentication) nas requisições.

## Exemplos de Uso

Todos os endpoints abaixo exigem autenticação (Basic Auth).

### Listar estudantes