from bs4 import BeautifulSoup
import requests as req
import re


def all_img(link):
	resp = req.get(link)
	soup = BeautifulSoup(resp.text, 'lxml')
	spa = soup.findAll('img')
	ret = []
	for x in spa:
		a = str(x).split('>')
		for l in a:
			b = str(a).split('=')
			try:

				price = re.sub(r'\s', ' ', b[3])
				command = re.split(r'[\'"]', price)
				if len(command[1]) <= 5:
					pass
				else:
					ret.append(command[1])
			except:
				pass
	return ret


def all_link(link):
	resp = req.get(link)
	soup = BeautifulSoup(resp.text, 'lxml')
	spa = soup.findAll('a')
	ret = []
	for x in spa:
		a = str(x).split('>')
		for l in a:
			b = str(a).split('=')
			try:
				price = re.sub(r'\s', ' ', b[1])
				command = re.split(r'[\'"]', price)
				if command[1].startswith('http') != True or command[1].startswith('https') != True:
					pass
				else:
					ret.append(command[1])
			except:
				pass

