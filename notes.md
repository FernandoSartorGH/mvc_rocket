# MVC (Model-View-Controller)
A arquitetura MVC (Model-View-Controller) é um padrão de arquitetura de software que separa uma aplicação em três componentes principais: Modelo (Model), Visão (View), Controlador (Controller). 
O MVC é uma abordagem amplamente utilizada no desenvolvimento de aplicações web e desktop. 

# SQL Alchemy
https://docs.sqlalchemy.org/en/20/core/engines.html


# Singleton
O Singleton é um padrão de projeto criacional que permite a você garantir que uma classe tenha apenas uma instância, enquanto provê um ponto de acesso global para essa instância.

*refactoring.guru*


# pytest
terminal: 
* cd path 
* pytest -s -v 

*O final do nome do arquivo sendo _test e o nome da função de teste iniciando com test_permite ao pytest entender que estamos tratando de testes.*


# Entities
Espelho de todos os elementos de armazenamento.


# Session

# Repositories
Açoes do banco de dados. Select, insert ...


# Run pytest
path: pytest -s -c

unique file: path pytest -s -c src/models/sqlite/repositories/repositories_test.py


# MockConnection
Simula um asessão para não ficar indo no banco de dados

Os teste que batem diretamente no banco de dados são testes de integração comn o banco.
Nos testes unitários, vamos barrar essas conexão e entrar em um abiente controlado, estabelecendo uma conexão fictícia para entender o que o código está fazendo.



# Controllers
Ações e funções das funcionalidades do projeto.

# Models
Interações de armazenamento e busca de dados com interação ao banco.

# Views
Interação com o usuário do sistema
teste para as views: mocar o controler >> cria um http_request >> valida o retorno


# Fluxo
view >> controlers > model > view

# Main
Conecta o projeto à framework.
Obs.: É diferente de construir o projeto sobree a framework.

# Blueprint
Consegue a partie da blueprint é possível daer nomes pra uma certa capacidade de rotas