# Projeto SQLite para Gerir um watchlist

A WatchList é um projeto que permite adicionar, ler, apagar e atualizar  não só animes dentro de uma lista de animes, mas também os visualizadores.

O projeto feito com Python, SQLite e InquirerPy.

## Estrutura do Projeto

A estrutura do diretório está organizada da seguinte forma:

watchlist
|
├───app
|    |
|    ├───sqlite-database
|    |   └───watchlist.db               # Arquivo principal da base de dados SQLite
|    |   └───watchlist_backup_1.db      # Cópia de segurança do banco de dados
|    |   └───watchlist_backup_2.db      # Outra cópia de segurança do banco de dados
|    |   └───watchlist_backup_3.db      # Outra cópia de segurança do banco de dados
|    |
|    └───src   # Diretório principal do projeto (código-fonte)
|    |    ├───create
|    |    │   └───create_visualizadores.py # Cria a tabela `visualizadores`
|    |    |   └───create_animes.py         # Cria a tabela `animes`
|    |    |
|    |    ├───delete
|    |    |   └───delete_visualizadores.py # Remove registros na tabela `visualizadores`
|    |    |   └───delete_animes.py         # Remove registros na tabela `animes`
|    |    |
|    |    ├───drop
|    |    │   └───drop_visualizadores.py   # Remove a tabela `visualizadores`
|    |    |   └───drop_animes.py           # Remove a tabela `animes`
|    |    |
|    |    ├───insert
|    |    │   └───insert_visualizador.py   # Insere registos na tabela `visualizadores`
|    |    |   └───insert_anime.py          # Insere registos na tabela `animes`
|    |    |
|    |    ├───read
|    |    │   └───read_visualizadores.py   # manipula a leitura da tabela `visualizadores`
|    |    |   └───read_animes.py           # manipula a leitura da tabela `animes`
|    |    |
|    |    ├───update
|    |    |   └───update_visualizadores.py # Atualiza dados na tabela `visualizadores`
|    |    |   └───update_animes.py         # Atualiza dados na tabela `animes`
|    |    |
|    |    |───__init__.py                  # Arquivo de inicialização
|    |    |───connection.py                # Manipula a conexão com a base de dados
|    |
|    └───main.py    # Script principal que inicializa e interage com a base de dados
|
|
|
|───README.md   # Documentação do projeto



## Esquema da Base de Dados

A base de dados SQLite `watchlist.db` consiste nas seguintes tabelas:

1. **visualizadores**
   - `id` (INTEGER, Chave Primária)
   - `nome_visualizador` (TEXT, Obrigatório)
   - `idade_visualizador` (INTEGER, Chave Estrangeira para a tabela `roles`) ##############
   - `animes` (TEXT, Chave Estrangeira para a tabela `animes`)

2. **animes**
   - `id` (INTEGER, Chave Primária)
   - `anime` (TEXT, Obrigatório)
   - `genero` (TEXT, Obrigatório)
   - `episodios` (INTEGER, Obrigatório)
   - `visualizadores` (TEXT, Chave Estrangeira para a tabela `visualizadores`)

## Funcionalidades

- **Criação de tabelas:** Cria automaticamente as tabelas `visualizadores` e `animes`, caso ainda não existam.
- **Inserção de dados:** Permite adicionar registros manualmente em todas as tabelas.
- **Consulta de dados:** Realiza consultas SELECT para:
  - Buscar todos os animes na watchlist.
  - Realizar joins entre tabelas para obter detalhes combinados.
  - buscar todos os visualizadores.
- **Exclusão de dados:** Remove registos específicos das tabelas `visualizadores` e `animes`.
- **Atualização de dados:** Atualiza campos existentes nas tabelas `visualizadores` e `animes`.

## Utilização

### Pré-requisitos

- Python 3.x instalado no sistema.
- Módulo SQLite3 (incluído por padrão na maioria das distribuições Python).
- Modulo InquirePy

### Passos para Executar

1. Clone este repositório ou copie os ficheiros para o seu computador local.
2. Navegue até o diretório do projeto.
3. Execute o script principal para interagir com a base de dados:

   ```bash
   python app/main.py
   ```

### Scripts Individuais

- **`create_visualizadores.py`:** Cria a tabela `visualizadores` na base de dados.
- **`create_animes.py`:** Cria a tabela `animes` na base de dados.

- **`insert_visualizadores.py`:** Insere dados na tabela `visualizadores`.
- **`insert_anime.py`:** Insere dados na tabela `animes`.

- **`read_visualizador.py`:** Le os dados da tabela `visualizadores`.
- **`read_animes.py`:** Le os dados da tabela `animes`.

- **`update_visualizadores.py`:** Atualiza dados na tabela `visualizadores`.
- **`update_animes.py`:** Atualiza dados na tabela `animes`.

- **`delete_visualizadores.py`:** Remove registros na tabela `visualizadores`.
- **`delete_animes.py`:** Remove registros na tabela `animes`.

- **`drop_visualizadores.py`:** Remove a tabela `visualizadores` da base de dados.
- **`drop_animes.py`:** Remove a tabela `animes` da base de dados.

## Exemplos de Consultas

Abaixo estão exemplos de consultas realizadas pelos scripts:

1. Buscar todos os animes na watchlist:
   ```sql
   SELECT * FROM animes;
   ```

2. Buscar todos os visualizadores:
   ```sql
   SELECT * FROM visualizadores;
   ```

3. Realizar join para obter detalhes combinados:
   ```sql
   SELECT * FROM animes
   INNER JOIN visualizadores
   ON animes.id = visualizadores.animes; ####################################################
   ```

## Contribuições

Contribuições são bem-vindas! Por favor, abra uma *issue* ou envie um *pull request* se desejar sugerir melhorias ou adicionar novas funcionalidades.