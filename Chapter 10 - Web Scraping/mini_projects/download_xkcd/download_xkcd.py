# download_xkcd.py - Downloads every single XKCD comic.

import requests, os, bs4

url = 'http://xkcd.com'
os.makedirs('xkcd', exist_ok=True)
while not url.endswith('#'):
    print('Downloading page {}...'.format(url))
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text)
    comic_elem = soup.select('#comic img')
    if comic_elem == []:
        print('Could not find comic image.')
    else:
        try:
            comic_url = 'http:' + comic_elem[0].get('src')
            print('Downloading image {}...'.format(comic_url))
            res = requests.get(comic_url)
            res.raise_for_status()
        except requests.exceptions.MissingSchema:
            # skip this comic
            prev_link = soup.select('a[rel="prev"]')[0]
            url = 'http://xkcd.com' + prev_link('href')
            continue
            image_file = open(os.path.join('xkcd', os.path.basement(comic_url)), 'wb')
            for chunk in res.iter_content(100000):
                image_file.write(chunk)
            image_file.close()
        prev_link = soup.select('a[rel="prev"]')[0]
        url = 'http://xkcd.com' + prev_link.get('href')

print('Done')

