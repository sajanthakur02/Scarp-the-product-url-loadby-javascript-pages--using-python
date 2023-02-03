from bs4 import BeautifulSoup
import requests


def scrap(url):
    searchURL = url

    headers = {
        'authority': 'www.google.com',
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'dnt': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'none',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-dest': 'document',
        'accept-language': 'en-US,en;q=0.9',
        'sec-gpc': '1',
    }
    params = (
        ('hl', 'en-US'),
        ('gl', 'us'),
    )

    array = []
    pageNumber = 1
    while True:
        
        page = requests.get(searchURL, headers=headers, params=params)
        soup = BeautifulSoup(page.content, 'html.parser')
        mainDiv = soup.find('div', class_='columns')
        product = mainDiv.find("div",class_="products wrapper grid products-grid")
    
        for link in product.find_all('li'):
            productLink = link.find('a', class_= 'product photo product-item-photo').get('href')
            array.append(productLink)

        if len(array) % 12 != 0 :
            print(searchURL)
            print(len(array))
            print('if')
            break
        else :
            print(searchURL)
            pageNumber += 1
            searchURL = url+"?p="+str(pageNumber)
            print(len(array))
            print('else')
    for line in array:
        print(line)
        # open("test.txt", "w", encoding="utf-8").write(line+'\n')

if __name__ == '__main__':
    scrap("enter the category page url to get the product link")
