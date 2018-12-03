import requests, bs4

url = 'https://automatetheboringstuff.com/chapter11/'

res = requests.get(url)
res.raise_for_status()
print(res.text)
soup = bs4.BeautifulSoup(res.text, features="html.parser")
links = soup.select('a')

bad_links = []
for link in links:
    try:
        if link.get('href') != 'None':
            res = requests.get(link.get('href'))
            print(res.status_code)
            if res.status_code == 404:
                bad_links.append(link.get('href'))
    except:
        pass

print(bad_links)