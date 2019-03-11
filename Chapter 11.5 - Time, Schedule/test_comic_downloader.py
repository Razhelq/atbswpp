from unittest import TestCase
from .comic_downloader import downloadComics, URL
import requests

class TestComicDownloader(TestCase):
    def test_check_website(self):
        response = requests.get(URL)

        self.assertEqual(response.status_code, 200)

    def test_comic_image_finder(self):
        response = requests.get(URL)
        soup = bs4.BeautifulSoup(response.text)
        comic_elem = soup.select('#comic img')

        self.assertDictEqual(comic_elem, [])
        self.assertNotEqual(response.status_code, 200)

    def test_check_if_exists(self):
        response = requests.get(URL)
        soup = bs4.BeautifulSoup(response.text)
        comic_elem = soup.select('#comic img')
        comic_url = 'http:' + comic_elem[0].get('src')
        picture_name = os.path.basename(comic_url)
        test_check_if_exists = os.path.isfile(os.path.join('xkcd', os.path.basename(comic_url)))
        check_if_exists = downloadComics.check_if_exists()

        self.assertEqual(check_if_exists, test_check_if_exists)

    def test_download_comic(self):
        response = requests.get(URL)
        soup = bs4.BeautifulSoup(response.text)
        comic_elem = soup.select('#comic img')
        comic_url = 'http:' + comic_elem[0].get('src')
        with open(os.path.join('xkcd', os.path.basename(comic_url), 'wb') as picture:
            for chunk in res.iter_content(100000):
                picture.write(chunk)


