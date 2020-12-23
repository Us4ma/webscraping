import requests
from bs4 import BeautifulSoup as bs

url="https://thegreatestbooks.org/?page="

for pages in range(1,53):

    req=requests.get(url + str(pages))
    soup=bs(req.text,'html.parser')
    container=soup.find('div',attrs={'class':'container'})
    books=container.find_all('h4')

    for book in books:
        links=book.find_all('a')
        title = links[0].get_text()
        author=""
        try:
            author=links[1].get_text()
        except:
            pass
        import pandas as pd

        pd.DataFrame({
            'title': title,
            'author': author,
        }, index=[]).to_csv('Top Books')


