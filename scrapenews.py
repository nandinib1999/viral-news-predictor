import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
import lxml
import pandas as pd

BASE_URL = "https://www.nytimes.com"

chrome_path = r"chromedriver_win32/chromedriver.exe"

option = Options()
option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")

# Pass the argument 1 to allow and 2 to block
option.add_experimental_option("prefs", { 
    "profile.default_content_setting_values.notifications": 2 
})
driver = webdriver.Chrome(chrome_options=option, executable_path=chrome_path)

def fetch_article(url):
	page = requests.get(url)
	soup = BeautifulSoup(page.text, 'html.parser')
	article_text = soup.find_all("div", class_="css-1fanzo5 StoryBodyCompanionColumn")
	content = []
	for article in article_text:
		text = article.text
		print(text)
		content.append(text)

	return " ".join(content)

def press_show_more(n_times):
	while n_times!=0:
		driver.find_element_by_xpath('//*[@id="stream-panel"]/div[1]/div/div/div/button').click()
		time.sleep(5)
		n_times -= 1
	page_source = driver.page_source
	return page_source

def fetch_list_of_articles(page_source):
	data = []
	soup = BeautifulSoup(page_source, 'lxml')
	news_table = soup.find_all("div", class_="css-13mho3u")
	# print(news_table)

	news = news_table[0].find_all("li", class_="css-ye6x8s")
	print(len(news))

	for x in news:
		link = x.a['href']
		title = x.find_all("h2", class_="css-1j9dxys e1xfvim30")[0].text
		article_url = BASE_URL+link
		if '/video/' not in article_url:
			content = fetch_article(article_url)
			print(article_url)
			print(title)
			print(content)
			data.append([title, content])

	df = pd.DataFrame(data, columns=['title', 'text'])
	return df

def start_scraping():
	POL_URL = BASE_URL + "/section/politics"
	driver.get(POL_URL)
	time.sleep(5)
	page_source = press_show_more(10)
	data = fetch_list_of_articles(page_source)
	driver.close()
	data.to_csv('scraped_news_nytimes.csv', index=False)

if __name__ == '__main__':
	start_scraping()
