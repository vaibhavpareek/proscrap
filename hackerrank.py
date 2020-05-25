import requests
from bs4 import BeautifulSoup
try:
	data = requests.get("http://www.hackerrank.com/eternityvp?hr_r=1").text
	soup = BeautifulSoup(data,'html.parser')
	print(soup.find_all(class_="history-list-item"))
except Exception as e:
	print(e)
	print("Might be issue with the username (Try Again)")