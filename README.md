# 🎵 Buscador de Letras de Músicas - **LyricFinder**

Aplicação desenvolvida em **Python + Streamlit**, permitindo buscar letras de músicas utilizando a API pública **Lyrics.ovh**.  
Possui uma interface simples, intuitiva e rápida, permitindo ao usuário encontrar uma letra informando apenas o **nome da banda/artista** e o **título da música**.

---

## 📘 Descrição

O **LyricFinder** é uma aplicação que consome uma API externa para disponibilizar letras de músicas em tempo real.

O fluxo funciona assim:

1. O usuário digita o nome da **banda/artista**
2. Digita o nome da **música**
3. O sistema envia uma requisição HTTP à API
4. A letra é exibida na tela — ou uma mensagem de erro caso não exista

O projeto foi criado com foco didático, aplicando conceitos de:

- Consumo de **APIs REST**
- Interface com **Streamlit**
- Tratamento de **requisições HTTP**
- Estrutura simples e clara de aplicações Python

---

## 🧩 Funcionalidades

### 1. **Entrada de Dados**
- Campo para nome da banda/artista  
- Campo para nome da música  

### 2. **Consulta Automática**
- Botão para buscar a letra  
- Requisições via **requests**  
- Retorno direto da letra se encontrada  

### 3. **Exibição da Letra**
- Exibição em formato de texto  
- Mensagens de sucesso e erro com Streamlit  

### 4. **Interface Visual**
- Imagem ilustrativa musical  
  - Local: `images/fender-2409274_1280.jpg`
- Título e interface estilizados com componentes Streamlit

---

## 📁 Estrutura do Projeto

Projeto_Letra_Musica/
├── app.py<br>                 # Arquivo principal da aplicação Streamlit
├── README.md<br>              # Documentação do projeto
├── images/<br>
│   └── fender-2409274_1280.jpg<br>  # Imagem usada na interface
└── venv/                  # Ambiente virtual (opcional)


---

## 📦 Requisitos

Para executar o projeto, são necessários:

- **Python 3.8+**
- **Pip atualizado**
- Bibliotecas:
  - streamlit
  - requests

Instalação das dependências:


---

## 🚀 Instalação e Execução

### **Passo 1 – Clonar o Projeto**

git clone https://github.com/seu-usuario/LyricFinder.git


### **Passo 2 – Criar Ambiente Virtual (Opcional)**

python -m venv venv
Ativar o ambiente virtual:

#### Windows:
venv\Scripts\activate

shell
Copiar código

#### Linux/Mac:
source venv/bin/activate

markdown
Copiar código

### **Passo 3 – Instalar Dependências**

pip install streamlit requests

markdown
Copiar código

### **Passo 4 – Executar a Aplicação**

streamlit run app.py

css
Copiar código

O Streamlit abrirá automaticamente o navegador em:

http://localhost:8501

yaml
Copiar código

---

## 🧠 Arquivo Principal — `app.py`

O arquivo contém:

- Função que faz requisição à API (`Buscar_Letra()`)
- Inputs de texto para banda e música
- Botão para buscar
- Exibição da letra ou mensagem de erro
- Carregamento da imagem de abertura

Fluxo geral:

1. Usuário digita banda e música  
2. O sistema chama a API:  
https://api.lyrics.ovh/v1/<banda>/<musica>

yaml
Copiar código
3. A API retorna JSON com a letra  
4. A letra é exibida na tela

---

## 🌐 Estrutura da API

API utilizada:

https://api.lyrics.ovh/

yaml
Copiar código

Endpoint principal:

/v1/<artista>/<musica>

makefile
Copiar código

Exemplo:

https://api.lyrics.ovh/v1/Coldplay/Yellow

css
Copiar código

Retorno esperado:

```json
{
  "lyrics": "Look at the stars..."
}
🧱 Padrão de Código
Funções separadas da interface

Uso de requests.get()

Validação do retorno da API

Uso de componentes Streamlit:

st.text_input()

st.button()

st.text()

st.success()

st.error()

Estrutura organizada e simples

🎧 Como Usar
Digite o nome da banda

Digite o nome da música

Clique em Pesquisar

A letra é exibida (se encontrada)

⚠️ Limitações da API
A API Lyrics.ovh é gratuita e possui limitações:

Algumas letras podem estar incompletas

Músicas menos conhecidas podem não ser encontradas

A API pode ficar fora do ar

Não fornece capa do álbum

🔮 Melhorias Futuras
Exibir capa do álbum usando outra API (Last.fm, Spotify, etc.)

Histórico de pesquisas

Tema claro/escuro

Download da letra em TXT ou PDF

Deploy na nuvem (Streamlit Cloud)

🆘 Suporte
Caso a aplicação não funcione:

Verifique sua conexão

Confirme se digitou banda e música corretamente

Veja se as dependências estão instaladas

Atualize o Streamlit

Teste a API no navegador

📄 Licença
Projeto livre para fins educacionais, focado em:

Consumo de APIs

Python

Streamlit

Projetos simples e funcionais

👨‍💻 Autor
Projeto desenvolvido com foco em estudo e prática de desenvolvimento web.

Versão: 1.0
Ano: 2025
Tecnologias: Python, Streamlit, Requests, Lyrics.ovh