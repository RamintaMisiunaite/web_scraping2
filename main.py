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
headlines = soup.find_all('div', class_='news__content')



print('koks zodis turi but antrasteje?')
word =  input('>')
print(f"filtruojamos naujienos su zodziu {word}")


for headline in headlines: 
    # get the title of the headline
    headline_title = headline.find('h3').text

    # get the time the headline was entered
    try:
       headline_time = headline.find('span', class_='info-block__text').text
    except AttributeError:
        continue       
    
    # get the theme the headline is posted under
    headline_theme = headline.find('a', class_='info-block__link').text

    if word in headline_title:
        print(f"Pavadinimas:  {headline_title}")
        print(f"Laikas:  {headline_time}")
        print(f"Tema:  {headline_theme}")
        print('')
    
    




