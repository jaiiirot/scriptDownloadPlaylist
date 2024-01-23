# Descargador de Videos de YouTube

Este script en Python utiliza la biblioteca `pytube` para descargar videos de YouTube, ya sea de un enlace único o de una playlist.

## Requisitos

- Python 3.x
- Instalar las dependencias ejecutando: `pip install pytube`

## Código

### `helloword.py`

```python
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
obtener_lista("https://youtube.com/playlist?list=PL65OIoU7mGjKrKnd7anVKTzN9x8gDbdEU&si=aIY0A_x2oYGDQo4r")
```

## Explicación del Código

1. descargar_video función:
- Esta función toma un enlace de YouTube como parámetro.
- Crea un objeto YouTube con el enlace proporcionado.
- Obtiene la mejor resolución disponible del video.
- Descarga el video en la carpeta de trabajo actual.
- Imprime un mensaje indicando que el video se ha descargado correctamente.

2. obtener_lista función:
- Toma una URL de una playlist de YouTube como parámetro.
- Utiliza la biblioteca pytube para obtener una lista de enlaces de video desde la playlist.
- Itera sobre los enlaces y llama a la función descargar_video para descargar cada video.

3. Ejemplo de Uso:
- Llama a obtener_lista con la URL de una playlist de YouTube como ejemplo.

### Uso
1. Clona o descarga este repositorio.
2. Abre una terminal y navega al directorio del proyecto.
3. Ejecuta el script con el comando: python helloword.py.

### Agradecimientos
Agradecemos a la comunidad de desarrolladores de pytube por proporcionar una herramienta útil para trabajar con YouTube en Python.
Si tienes alguna pregunta o sugerencia, no dudes en contactarnos.