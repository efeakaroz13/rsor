import wikipedia
from bs4 import BeautifulSoup
import requests
from selenium import webdriver


def searchwikipedia(keyword):
	data = []
	result = wikipedia.search(str(keyword), results = 10)
	

	return result

def searchgoogle(keyword):
	output = []
	for i in range(5):

		page = requests.get("https://www.google.com/search?q={}&start={}0".format(keyword.replace(" ","+"),i))
		soup = BeautifulSoup(page.content,"html.parser")
		all_h3= soup.find_all("h3")
		for a in all_h3:
			try:
				data = {
				"title":a.get_text(),
				"url":a.parent.parent.find_all("a")[0].get("href").replace("/url?q=","")
				}
				output.insert(0,data)
			except:
				pass


	return output


def searchyandex(keyword):
	#searchyandex
	driver = webdriver.Chrome("./chromedriver")

	driver.get("https://yandex.com.tr/search/?text={}".format(keyword.replace(" ","+")))
	soup = BeautifulSoup(page.content,"html.parser")
	all_li= soup.find_all("li")

	return page.content

def searchpinterest(keyword):
	#searchpinterest

	pass


def searchtorch(keyword):
	#searchtorch

	pass


def searchstackoverflow(keyword):
	#searchstackoverflow

	pass

def searchgoogleimages(keyword):
	#searchgoogleimages

	pass



print(searchyandex("Lana del rey"))