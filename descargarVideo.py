from pytube import Playlist, YouTube

def descargar_video(link):
    try:
        video = YouTube(link)
        descarga = video.streams.get_highest_resolution()
        descarga.download()
        print(f"Video descargado: {video.title}")
    except Exception as e:
        print(f"Error al descargar el video: {e}")

def obtener_lista(url):
    try:
        links = Playlist(url)
        if links:
            for link in links:
                descargar_video(link)
        else:
            print("No se encontraron videos")
    except Exception as e:
        raise Exception(f"Error al obtener la lista de videos {e}")

# Ejemplo de uso
obtener_lista("https://youtube.com/playlist?list=PLjrXqm46I4pMaZkGLoUW-q46EW6TsAMsu&si=2CQxOUmMyzgYNYFc")
    
# descargar_video()
