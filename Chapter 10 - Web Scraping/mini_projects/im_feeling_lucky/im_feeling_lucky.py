# im_feeling_lucky.py - Opens several Google search results


import requests, sys, webbrowser, bs4


print('Googling...')
res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()


# Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text)


# Open a browser tab for each result.
link_elems = soup.select('.r a')


# Open a browser tab for each result.
num_open = min(5, len(link_elems))
for i in range(num_open):
    webbrowser.open('http://google.com' + link_elems[i].get('href'))