import requests
from bs4 import BeautifulSoup
from datetime import datetime

url = "https://news.google.com/topics/CAAqLQgKIidDQkFTRndvSkwyMHZNR1ptZHpWbUVnWmxjeTAwTVRrYUFrRlNLQUFQAQ?hl=es-419&gl=AR&ceid=AR%3Aes-419"

response = requests.get(url)

document = response.text

object_soup = BeautifulSoup(document, "html.parser")

current_date = datetime.now().strftime("%d_%m_%Y")

with open(f"google_news_{current_date}.txt", 'w+') as file:
	for tag_h3 in object_soup.find_all("h3", class_="ipQwMb ekueJc RD0gLb", limit=20):
		news_title = tag_h3.a.text + "\n\n"

		file.write(news_title)


