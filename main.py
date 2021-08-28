# Web scraper using BeautifulSoup, lxml parsing, and requests
# ------------------------------------------------------------------------
from bs4 import BeautifulSoup
import requests
import PySimpleGUI as PSG

prayer_times = [['Fajr', ], ['Zhur', ], ['Asr', ], ['Maghreb', ], ['Isha', ]]

source = requests.get('https://windsorislamicassociation.com').text
soup = BeautifulSoup(source, 'lxml')
soup = soup.find('div', class_='widget-area')
times = soup.find_all('td', class_='begins')

for index, time in enumerate(times):
    prayer_times[index].append(time.text)

# GUI used to display information from web scraper using PySimpleGUI
# ------------------------------------------------------------------------

o1 = [PSG.Text(prayer_times[0][0] + ' at ' + prayer_times[0][1] + '\n')]
o2 = [PSG.Text(prayer_times[1][0] + ' at ' + prayer_times[1][1] + '\n')]
o3 = [PSG.Text(prayer_times[2][0] + ' at ' + prayer_times[2][1] + '\n')]
o4 = [PSG.Text(prayer_times[3][0] + ' at ' + prayer_times[3][1] + '\n')]
o5 = [PSG.Text(prayer_times[4][0] + ' at ' + prayer_times[4][1] + '\n')]

layout = [
    [o1 + o2 + o3 + o4 + o5]
]

window = PSG.Window('Prayer Times', layout, margins=(100, 50))

while True:
    event, values = window.read()

    if event == PSG.WIN_CLOSED:
        break

window.close()
