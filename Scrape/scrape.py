from bs4 import BeautifulSoup
import requests

def genereWise(genere_name):
    movie_list=[]
    html_page = requests.get('https://www.imdb.com/search/title?genres='+genere_name.lower()+'&explore=title_type,genres')
    soup = BeautifulSoup(html_page.content, 'lxml')
    name = soup.find_all('h3', class_ = 'lister-item-header')
    imgs = soup.find_all('img', class_='loadlate')
    for i in name:
        names = i.find_all('a')
        movie_list.append(names[0].text if len(names) == 1 else names[0].text+'-'+names[1].text)
    return "%%".join(movie_list[:5])



