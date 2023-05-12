import requests
from bs4 import BeautifulSoup as bs


def get_links():
    # URL de la página de la que se quieren extraer los links
    url = 'https://www.pagina12.com.ar/secciones/el-pais'
    try:
        # Hacer la petición GET a la página
        response = requests.get(url)

    # Verificar que la petición fue exitosa (código 200)
        if response.status_code == 200:
            # Obtener el contenido HTML de la página
            html = response.content

        # Crear un objeto BeautifulSoup (bs) a partir del contenido HTML
            soup = bs(html, 'html.parser')
            s_nota = bs(response.text, 'lxml')
            print('s_nota', s_nota)
        # Encontrar el titulo
            titulo = s_nota.find('h1').text
            print(titulo)

        # Encontrar fecha de la publicación
            fecha_publicacion = s_nota.find(
                'div', class_='date hide-on-mobile')
            print(fecha_publicacion.text)

        # Encontrar imagen
            media = s_nota.find(
                'div', class_='article-item__header deco-bar-here')
            print(media)

            if len(media):
                imagen = media.img.get('src')
                print('imagen', imagen)
            else:
                print('No image')

        # Solicitamos por medio de request la imagen de la nota
        imagen_request = requests.get(imagen)
        print(imagen_request.status_code)

        # Encontrar todos los elementos 'a' que estén dentro de una etiqueta 'h2'
        # con la clase 'article-title'
        links = soup.find_all('h2', class_='h1 title-list') + soup.find_all(
            'h3', class_='h2 title-list featured-article') + soup.find_all('h4', class_='h2 is-display-inline title-list')

        # Iterar sobre la lista de links encontrados para obtener su href
        for link in links:
            # Obtener el href del link
            href = link.find('a')['href']

            # Imprimir el href del link
            print(href)
        else:
            # Si la petición no fue exitosa, imprimir el código de estado recibido
            print(f'Status code error: {response.status_code}')
    except Exception as e:
        print(str(e))


if __name__ == '__main__':
    get_links()
