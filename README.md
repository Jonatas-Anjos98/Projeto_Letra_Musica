🎵 Buscador de Letras de Músicas

Uma aplicação simples e interativa desenvolvida em Python com Streamlit, que permite pesquisar letras de músicas informando o nome da banda/artista e o título da música. O projeto utiliza a API pública lyrics.ovh para obter as letras automaticamente.

📸 Demonstração da Interface

A aplicação exibe uma imagem ilustrativa no topo da página, localizada na pasta images/.

📁 projeto/
 ├── images/
 │    └── fender-2409274_1280.jpg
 ├── venv/
 ├── app.py
 └── README.md

🚀 Tecnologias Utilizadas

Python 3

Streamlit

Requests

API Lyrics.ovh

🔍 Funcionalidades

Campo de texto para digitar:

Nome da banda/artista

Nome da música

Botão de pesquisa

Consumo de API para obter a letra

Exibição da letra diretamente na tela

Mensagens de sucesso ou erro para melhor experiência do usuário

📦 Como Executar o Projeto
1️⃣ Clone o repositório
git clone https://github.com/seu-usuario/nome-do-repo.git

2️⃣ Instale as dependências

Recomenda-se usar um ambiente virtual:

pip install streamlit requests

3️⃣ Execute o projeto
streamlit run app.py

Como Funciona

O app envia uma requisição GET para:

https://api.lyrics.ovh/v1/<banda>/<música>


Se a API encontrar a letra, ela é exibida no Streamlit.
Caso contrário, o usuário recebe uma mensagem de erro informando que a letra não foi encontrada.

Estrutura do Código (app.py)

O arquivo principal contém:

Função para consumir a API

Configuração da interface com Streamlit

Entrada de dados do usuário

Tratamento da resposta e exibição da letra