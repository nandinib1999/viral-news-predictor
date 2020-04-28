import requests
from bs4 import BeautifulSoup
import time
import pandas as pd

def get_content(url):
	text = []
	page = requests.get(url)
	soup = BeautifulSoup(page.text, 'html.parser')
	content = soup.find_all("p")
	for para in content:
		text.append(para.text)
	return ' '.join(text)

def main():
	data = []
	BASE_URL = 'https://newspunch.com/page/'
	for page_no in range(1, 11):
		page_url = BASE_URL + str(page_no)+'/'
		print(page_url)
		page = requests.get(page_url)

		soup = BeautifulSoup(page.text, 'html.parser')
		news_block = soup.find_all("div", class_="mh-posts-list-content clearfix")
		print(len(news_block))
		for block in news_block:
			title = block.a['title']
			url = block.a['href']
			content = get_content(url)
			content = content.replace("Copyright © 2020 News Punch. All rights reserved | News Punch", "")
			print(title)
			print(url)
			print(content)
			print()
			data.append([title, content])

	df = pd.DataFrame(data, columns=["title", "text"])
	df.to_csv("scrape_news_newspunch.csv", index=False)


if __name__ == '__main__':
	main()