# Sistema Especialista de Doação de Sangue

Este é um sistema especialista para auxiliar na doação de sangue. Ele permite realizar consultas sobre compatibilidade de tipos sanguíneos e fatores Rh utilizando Prolog, integrado a uma interface gráfica desenvolvida em Python.

## Alunos:

- Ayrton Finicelli Lemes - 22053242
- Caroline Soares Braz - 22051417
- Jakeline Gimaque de Mesquita - 22050618
- Luiz Gabriel Favacho de Almeida - 22153921

## Funcionalidades

- Determinar quem está apto a doar para um receptor específico.
- Verificar para quem uma pessoa pode doar ou de quem pode receber sangue.
- Identificar pessoas com um determinado tipo sanguíneo ou fator Rh.

## Requisitos

- Python 3.12 ou superior.
- SWI-Prolog instalado e configurado no PATH do sistema.
- Bibliotecas Python:
  - `pyswip`
  - `tk`

## Configuração do Ambiente

1. Clone este repositório:

   ```bash
   git clone <url-do-repositorio>
   cd <nome-do-repositorio>
   ```

2. Crie um ambiente virtual:

   ```bash
   python -m venv venv
   ```

3. Ative o ambiente virtual:

   - **Windows**:
     ```bash
     .\venv\Scripts\activate
     ```
   - **Linux/MacOS**:
     ```bash
     source venv/bin/activate
     ```

4. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

## Execução do Programa

1. Certifique-se de que o arquivo **Prolog** (`sistema_sangue.pl`) está no mesmo diretório que `main.py`.

2. Execute o programa:

   ```bash
   python main.py
   ```

3. Uma interface gráfica será aberta, onde você pode realizar as seguintes consultas:

   - **Quem pode doar para**: Insira o nome de um receptor.
   - **Para quem pode doar**: Insira o nome de um doador.
   - **Pessoas com tipo sanguíneo**: Insira o tipo sanguíneo (ex.: `a`, `b`, `o`, `ab`).
   - **Pessoas com fator Rh**: Insira o fator Rh (`+` ou `-`).

## Exemplo de Uso

1. Insira `joao` no campo de entrada e clique em "Para quem pode doar".
2. O sistema exibirá todos os receptores compatíveis com `joao`.

## Problemas Comuns

- **Erro `SwiPrologNotFoundError`**:

  - Certifique-se de que o SWI-Prolog está instalado e configurado no PATH do sistema.

- **Erro ao ativar o ambiente virtual**:
  - Em sistemas Windows, configure a política de execução de scripts, executando o PowerShell como administrador e inserindo:
    ```bash
    Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
    ```

## Perguntas da Letra D

As perguntas 1 à 4 da letra D da questão estão respondidas ao final do arquivo `sistema_sangue.pl`.
