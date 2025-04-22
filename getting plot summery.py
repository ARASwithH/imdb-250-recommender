import requests
from bs4 import BeautifulSoup as bfs
import csv

# making a csv file for saving datas
outfile = open('web scraping/dirty_datas.csv', 'w', encoding="utf-8", newline='')
writer = csv.writer(outfile)


# the requesting process
header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'}
url = "https://www.imdb.com/chart/top/"
response = requests.get(url,headers=header).text


# accessing the summaries by the html tags of the website:
soup= bfs(response , 'html.parser')
links = soup.find_all('a' , {'class': 'ipc-title-link-wrapper'} ,href = True)[:250]


for i,link in enumerate(links) :
    u_url=f'https://www.imdb.com/{link['href']}'
    u_response=requests.get(u_url,headers=header).content
    u_soup= bfs(u_response , 'html.parser')
    u_name= u_soup.find(class_='hero__primary-text').get_text(strip=True)
    u_text = u_soup.find(class_='sc-7193fc79-2 kpMXpM').get_text(strip=True)
    print(i,u_name,u_text)
    writer.writerow([u_name, u_text])