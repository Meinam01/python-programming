from bs4 import BeautifulSoup
import requests, openpyxl

try:
    url = "https://www.imdb.com/chart/top/"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    #print(soup)
    movies = soup.find_all('div',class_='sc-fc35a1ef-0 hTMtRz')
    for movie in movies:
        #print(movie)
        movie_name=movie.find('h3',class_='ipc-title__text').text
        movie_rating = movie.find('span',class_='ipc-rating-star--rating').text
        print(movie_name + " -- " + movie_rating)

except Exception as error:
    print(error)
