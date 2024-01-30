from bs4 import BeautifulSoup
import requests


html_url = requests.get('https://www.lrt.lt/')

# Make the guessed encoding official
html_url.encoding = html_url.apparent_encoding

html_text = html_url.text

soup = BeautifulSoup(html_text, 'lxml')

headline = soup.find('div', class_='news__content')

headline_title = headline.find('h3').text

headline_time = headline.find('span', class_='info-block__time-before')['title']

headline_theme = headline.find('a', class_='info-block__link').text

print(f'''
      Pavadinimas:  {headline_title},
      Laikas: {headline_time},
      Tema: {headline_theme}
      ''')