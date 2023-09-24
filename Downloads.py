#Downloads 
from pytube import Playlist,YouTube  
def Downloads_Video(Url):
    Video = YouTube(f"{Url}") #Pegar Url
    Video.streams.get_highest_resolution().download("Downloads/") #Baixar Video 

def Downloads_Music(Url):
    Music = YouTube(f"{Url}") #Pegar Url
    titulo = Music.title 
    Titulo = titulo.replace("|", "").replace(":", "").replace("?", "").replace("♪", "").replace("-","") #Tirando todos os simbulos
    print(f"{Titulo}_Video_Downloads") # Adicionando Um prefix (Para evitar bugs por contas de emojis em titulos)
    Music.streams.filter(only_audio=True).first().download(f"Downloads/",filename=f'{Titulo}.mp3') # Convertendo Para Mp3 , Dando o nome para o arquivo,Baixando o Arquivo
    
def Downloads(url,Formato):
    Playlists = Playlist(f"{url}") #Pegando Url
    try: # Se For Playlist
        for Url in Playlists.video_urls:
            if Formato == "Mp3": # Se o formato selecionado for mp3: Baixar Musica caso contario baixar video
                Downloads_Music(Url)
            else: 
                Downloads_Video(Url)
    except: # Se Não for playlist
            if Formato == "Mp3":
                Downloads_Music(url)
            else: 
                Downloads_Video(url)



