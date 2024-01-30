from bs4 import BeautifulSoup
import requests

# This application will scrape the data of the headline from lrt.lt

# connect to lrt.lt
html_url = requests.get('https://www.lrt.lt/')

# update the encoding so lithuanian letters would be recognized
html_url.encoding = html_url.apparent_encoding

# get the html text from website
html_text = html_url.text

soup = BeautifulSoup(html_text, 'lxml')

# select only headline divs
headline = soup.find('div', class_='news__content')

# get the title of the headline
headline_title = headline.find('h3').text

# get the time the headline was entered
headline_time = headline.find('span', class_='info-block__time-before')['title']

# get the theme the headline is posted under
headline_theme = headline.find('a', class_='info-block__link').text

print(f'''
      Pavadinimas:  {headline_title},
      Laikas: {headline_time},
      Tema: {headline_theme}
      ''')