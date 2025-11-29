import requests
import streamlit as st

def Buscar_Letra(Nome_Banda, Nome_Musica):
    Endpoint = f'https://api.lyrics.ovh/v1/{Nome_Banda}/{Nome_Musica}'
    Response = requests.get(Endpoint)
    Letra_Musica = Response.json()['lyrics'] if Response.status_code ==200 else''
    return Letra_Musica

st.image('images/fender-2409274_1280.jpg')
st.title('Letras de Músicas')

Nome_Banda = st.text_input('Digite o nome da banda: ', key='banda')
Nome_Musica = st.text_input('Digite o nome da música: ', key='musica')
pesquisar = st.button('Pesquisar')

if pesquisar:
    Letra_Musica = Buscar_Letra(Nome_Banda, Nome_Musica)
    if Letra_Musica:
        st.success('Encontramos a letra da sua música')
        st.text(Letra_Musica)
    else:
        st.error('Não encontramos a letra desta música').vem