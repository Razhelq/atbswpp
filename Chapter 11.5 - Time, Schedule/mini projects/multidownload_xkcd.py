# multidownload_xkcd.py - Downloads every single XKCD comic.


import requests, os, bs4, shutil, threading
from requests.exceptions import MissingSchema, HTTPError

if os.path.isdir('xkcd') == True:
    shutil.rmtree('xkcd')
    os.makedirs('xkcd', exist_ok=True)
else:
    os.makedirs('xkcd', exist_ok=True)

def download_xkcd(start_comic, end_comic):
    url = 'http://xkcd.com/'
    for url_num in range(start_comic, end_comic):
        print('Downloading page {}...'.format(url_num))
        res = requests.get(url + str(url_num))
        try:
            res.raise_for_status()
        except HTTPError:
            print('Picture not found')

        soup = bs4.BeautifulSoup(res.text)

        comic_elem = soup.select('#comic img')
        if comic_elem == []:
            print('Could not find comic image.')
        else:
            comic_url = 'http:' + comic_elem[0].get('src')
            print('Downloading image {}...'.format(comic_url))
            res = requests.get(comic_url)
            res.raise_for_status()

            image_file = open(os.path.join('xkcd', os.path.basename(comic_url)), 'wb')
            for chunk in res.iter_content(100000):
                image_file.write(chunk)
            image_file.close()

download_treads = []
for i in range(1, 1400, 100):
    download_tread = threading.Thread(target=download_xkcd, args=(i, i + 99))
    download_treads.append(download_tread)
    download_tread.start()

for download_tread in download_treads:
    download_tread.join()

print('Done')

