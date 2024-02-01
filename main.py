from bs4 import BeautifulSoup
from datetime import datetime
import requests
import csv

'''
This application will scrape the headlines data from lrt.lt. 
The headline, the time it was posted and the theme of the news are collected.
The inforamtion is written in to a csv file.
'''


def collect_headlines():

    # connect to lrt.lt
    html_url = requests.get('https://www.lrt.lt/')


    # update the encoding so lithuanian letters would be recognized
    html_url.encoding = html_url.apparent_encoding

    html_text = html_url.text

    soup = BeautifulSoup(html_text, 'lxml')

    # headline divs are in a class 'news__content' - select only those
    headlines = soup.find_all('div', class_='news__content')


    # empty array to store all headlines after scraping for easier writing to csv
    headlines_for_writing = []


    for headline in headlines: 

        headline_title = headline.find('h3').text

        try:
            headline_time = headline.find('span', class_='info-block__text').text
        except AttributeError:
            continue       
        
        headline_theme = headline.find('a', class_='info-block__link').text


        row = [headline_title.strip(), headline_time.strip(),headline_theme.strip()]
        headlines_for_writing.append(row)


    # write the information into a file which is named with the date and time of scraping   
    file_name = '-'.join([datetime.today().strftime('%Y-%m-%d'),datetime.today().strftime('%H-%M-%S')])
    with open(f'''headlines/{file_name}.csv''', 'w', encoding=html_url.encoding) as f:
            print('Starting to write to a file...')
            writer = csv.writer(f)
            writer.writerows(headlines_for_writing) 
            print('The file is ready')

    


if __name__ == '__main__':
    collect_headlines()

