# umpbrella_deminder.py - Checks common weather forcast website.
# If it is going to rain next day it will send a text message to remind me about ubrella.
import bs4, requests, re, schedule, time
from twilio.rest import Client


def text_myself():
    account_SID = ''
    auth_token = ''
    my_number = ''
    twilio_number = ''

    message = "Jutro będzie padać. It's gonna rain tomorrow."

    twilioCli = Client(account_SID, auth_token)
    twilioCli.messages.create(body=message, from_=twilio_number, to=my_number)


def check_the_weather():
    url = "http://www.pogodynka.pl/polska/prognoza_synoptyczna/wroclaw_wroclaw"

    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, features='html.parser')
    weather = soup.select('.k2 .zjawisko_container')[0].getText()
    print(weather)
    try:
        if re.search(r'deszczu', weather).group():
            text_myself()
    except:
        pass


schedule.every().day.at('19:00').do(check_the_weather)

while True:
    schedule.run_pending()
    time.sleep(1)