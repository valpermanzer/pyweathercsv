import requests
import pandas as pd
from bs4 import BeautifulSoup
url = input ("Enter the url from forecast.weather.gov of your place: ")
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
week = soup.find(id="seven-day-forecast-body")
items = week.find_all(class_= "tombstone-container")
period_names = [item.find(class_='period-name').get_text() for item in items]
short_desc = [item.find(class_='short-desc').get_text() for item in items]
temp = [item.find(class_='temp').get_text() for item in items]
weather_stuff  = pd.DataFrame(
  {'period': period_names,
   'short_descricptions': short_desc,
   'temperatures': temp,
  }
)
print(weather_stuff)
ans = input("Do you want a csv file of this data (y/n): ")
if ans == 'y':
  weather_stuff.to_csv('weather.csv')
